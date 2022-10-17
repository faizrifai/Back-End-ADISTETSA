from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ExportForm
from import_export.signals import post_export


class ExportDataWithFile(ImportExportModelAdmin):
    def export_action(self, request, *args, **kwargs):
        if not self.has_export_permission(request):
            raise PermissionDenied

        formats = self.get_export_formats()
        form = ExportForm(formats, request.POST or None)
        if form.is_valid():
            file_format = formats[int(form.cleaned_data["file_format"])]()

            queryset = self.get_export_queryset(request)
            export_data = self.get_export_data(
                file_format, queryset, request=request, encoding=self.to_encoding
            )
            content_type = file_format.get_content_type()
            response = redirect("admin/kurikulum/rekapjurnalbelajar")
            print(type(export_data))
            # response = HttpResponse(export_data, content_type=content_type)
            # response['Content-Disposition'] = 'attachment; filename="%s"' % (
            #     self.get_export_filename(request, queryset, file_format),
            # )

            post_export.send(sender=None, model=self.model)
            return response

        context = self.get_export_context_data()

        context.update(self.admin_site.each_context(request))

        context["title"] = _("Export")
        context["form"] = form
        context["opts"] = self.model._meta
        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.export_template_name], context)
