from import_export.forms import ExportForm
from import_export.formats.base_formats import DEFAULT_FORMATS
from import_export.signals import post_export

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.files.base import ContentFile
from django.utils import timezone
from django.urls.conf import path
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin
from subadmin import SubAdmin, SubAdminHelper

class BaseSubAdminExport(SubAdmin):
    change_list_template = 'export/change_list.html'

    def get_model_info(self):
        app_label = self.model._meta.app_label
        return (app_label, self.model._meta.model_name)

    def get_permission_codename(action, opts):
        """
        Return the codename of the permission for the specified action.
        """
        return '%s_%s' % (action, opts.model_name)

    def has_export_permission(self, request):
        """
        Returns whether a request has export permission.
        """
        EXPORT_PERMISSION_CODE = getattr(settings, 'IMPORT_EXPORT_EXPORT_PERMISSION_CODE', None)
        if EXPORT_PERMISSION_CODE is None:
            return True

        opts = self.opts
        codename = self.get_permission_codename(EXPORT_PERMISSION_CODE, opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def changelist_view(self, request, *args, **kwargs):
        response = super().changelist_view(request, *args, **kwargs)
        extra_context = {
            'export_url': request.build_absolute_uri(request.get_full_path() + 'export')
        }
        try:
            response.context_data.update(extra_context)
        except:
            pass

        return response

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export/',
                self.admin_site.admin_view(self.export_action),
                name='%s_%s_export' % self.get_model_info()),
        ]
        return my_urls + urls

    def get_export_queryset(self, request):
        """
        Returns export queryset.

        Default implementation respects applied search and filters.
        """
        list_display = self.get_list_display(request)
        list_display_links = self.get_list_display_links(request, list_display)
        list_filter = self.get_list_filter(request)
        search_fields = self.get_search_fields(request)
        if self.get_actions(request):
            list_display = ['action_checkbox'] + list(list_display)

        ChangeList = self.get_changelist(request)
        changelist_kwargs = {
            'request': request,
            'model': self.model,
            'list_display': list_display,
            'list_display_links': list_display_links,
            'list_filter': list_filter,
            'date_hierarchy': self.date_hierarchy,
            'search_fields': search_fields,
            'list_select_related': self.list_select_related,
            'list_per_page': self.list_per_page,
            'list_max_show_all': self.list_max_show_all,
            'list_editable': self.list_editable,
            'model_admin': self,
        }

        changelist_kwargs['sortable_by'] = self.sortable_by
        changelist_kwargs['search_help_text'] = self.search_help_text
        cl = ChangeList(**changelist_kwargs)

        return cl.get_queryset(request)

    def get_data_for_export(self, queryset, *args, **kwargs):
        resource_class = self.resource_class
        return resource_class().export(queryset, *args, **kwargs)

    def get_export_data(self, file_format, queryset, *args, **kwargs):
        """
        Returns file_format representation for given queryset.
        """
        request = kwargs.pop("request")
        if not self.has_export_permission(request):
            raise PermissionDenied

        data = self.get_data_for_export( queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        encoding = kwargs.get("encoding")
        if not file_format.is_binary() and encoding:
            export_data = export_data.encode(encoding)
        return export_data

    def get_export_filename(self, file_format):
        date_str = timezone.now().strftime('%Y-%m-%d')
        filename = "%s-%s.%s" % (self.model.__name__,
                                 date_str,
                                 file_format.get_extension())
        return filename

    def export_action(self, request, *args, **kwargs):
        if not self.has_export_permission(request):
            raise PermissionDenied

        request.subadmin = SubAdminHelper(self, args)

        formats = DEFAULT_FORMATS
        form = ExportForm(formats, request.POST or None)
        if form.is_valid():
            file_format = formats[
                int(form.cleaned_data['file_format'])
            ]()

            queryset = self.get_export_queryset(request)
            export_data = self.get_export_data(file_format, queryset, request=request, encoding=None)
            content_type = file_format.get_content_type()
            response = HttpResponse(export_data, content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="%s"' % (
                self.get_export_filename(file_format),
            )

            post_export.send(sender=None, model=self.model)
            return response

        context = {}

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Export")
        context['form'] = form
        context['opts'] = self.model._meta
        request.current_app = self.admin_site.name

        return TemplateResponse(request, 'export/export.html',
                                context)


class SubAdminExportDataWithFile(BaseSubAdminExport):
    formats = DEFAULT_FORMATS
    export_template_name = 'export/export.html'
    post_export_redirect_url = None

    def get_export_context_data(self, **kwargs):
        return self.get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        return {}

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        return [f for f in self.formats if f().can_export()]

    def get_export_file(self, request, file_format):
        queryset = self.get_export_queryset(request)
        export_data = self.get_export_data(file_format, queryset, request=request, encoding=None)

        file = ContentFile(export_data, name=self.get_export_filename(file_format))

        return file, queryset

    def pre_export(self, request, file_format):
        return self.get_export_file(request, file_format)

    def export_action(self, request, *args, **kwargs):
        if not self.has_export_permission(request):
            raise PermissionDenied

        request.subadmin = SubAdminHelper(self, args)

        formats = DEFAULT_FORMATS
        form = ExportForm(formats, request.POST or None)
        if form.is_valid():
            file_format = formats[
                int(form.cleaned_data['file_format'])
            ]()

            response = HttpResponseRedirect(reverse(self.post_export_redirect_url))

            self.pre_export(request, file_format)

            post_export.send(sender=None, model=self.model)
            return response

        context = {}

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Export")
        context['form'] = form
        context['opts'] = self.model._meta
        request.current_app = self.admin_site.name

        return TemplateResponse(request, 'export/export.html',
                                context)

class ImportExportWithFile(ImportExportModelAdmin):
    post_export_redirect_url = None

    def get_export_filename(self, file_format):
        date_str = timezone.now().strftime('%Y-%m-%d')
        filename = "%s-%s.%s" % (self.model.__name__,
                                 date_str,
                                 file_format.get_extension())
        return filename

    def get_export_file(self, request, file_format):
        queryset = self.get_export_queryset(request)
        export_data = self.get_export_data(file_format, queryset, request=request, encoding=None)

        file = ContentFile(export_data, name=self.get_export_filename(file_format))

        return file, queryset

    def pre_export(self, request, file_format):
        return self.get_export_file(request, file_format)

    def export_action(self, request, *args, **kwargs):
        if not self.has_export_permission(request):
            raise PermissionDenied

        formats = self.get_export_formats()
        form = ExportForm(formats, request.POST or None)
        if form.is_valid():
            file_format = formats[
                int(form.cleaned_data['file_format'])
            ]()

            response = HttpResponseRedirect(reverse(self.post_export_redirect_url))

            self.pre_export(request, file_format)

            post_export.send(sender=None, model=self.model)
            return response

        context = self.get_export_context_data()

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Export")
        context['form'] = form
        context['opts'] = self.model._meta
        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.export_template_name],
                                context)