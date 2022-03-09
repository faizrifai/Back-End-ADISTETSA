from cgitb import lookup
import django_filters
from admin_auto_filters.filters import AutocompleteFilter
from kurikulum.models import Kelas
from kurikulum.models import KelasSiswa
from django.contrib import admin
from kurikulum.models import Jurusan
from django_filters import rest_framework as filters
from .models import KatalogKonselor, PeminatanLintasMinat
from django.utils.translation import gettext_lazy as _
from dataprofil.models import DataSiswa


# class JurusanFilter(AutocompleteFilter):
#     title = 'Jurusan'  # Filter Title
#     field_name = 'JURUSAN'  # Book.<field_name> --> Book.course

# class KelasFilter(AutocompleteFilter):
#     title = 'Kelas'  # Filter Title
#     field_name = 'KELAS'  # Book.<field_name> --> Book.course

class GenerateFilter(admin.SimpleListFilter):
    lookup_model = None
    lookup_field = None
    filter_parameter = None
    is_choices = False
    
    def lookups(self, request, model_admin):
        filter_list_value = []
        
        if self.lookup_model:
            if self.is_choices:
                return self.lookup_model._meta.get_field(self.lookup_field).choices
            
            for data in self.lookup_model.objects.all():
                if not self.lookup_field:
                    filter_list_value.append((
                        str(data.pk), str(data))
                    )
                else:
                    filter_list_value.append((
                        getattr(data, self.lookup_field), getattr(data, self.lookup_field))
                    )
            
            return tuple(filter_list_value)
    
    def get_filter_parameter(self):
        filter_parameter = {
            self.filter_parameter: self.value()
        }
        
        return filter_parameter

    def queryset(self, request, queryset):
        filter_parameter = self.get_filter_parameter()
        if self.value():
            return queryset.filter(**filter_parameter)
        

class JurusanFilter(GenerateFilter):
    title = 'JURUSAN'
    parameter_name = 'JURUSAN'
    
    lookup_model = Jurusan
    lookup_field = 'NAMA'
    filter_parameter = 'KELAS_SISWA__KELAS__KELAS__JURUSAN__NAMA'
    
class TingkatanFilter(GenerateFilter):
    title = 'TINGKATAN'
    parameter_name = 'TINGKATAN'
    
    lookup_model = Kelas
    lookup_field = 'TINGKATAN'
    filter_parameter = 'KELAS_SISWA__KELAS__KELAS__TINGKATAN'
    is_choices = True

# class JurusanFilter(admin.SimpleListFilter):
#     title = _('JURUSAN')
#     # field_name = ''
#     parameter_name = 'JURUSAN'
#     filter_field_name = 'KELAS_SISWA__KELAS__KELAS__JURUSAN__NAMA'
    
#     def lookups(self, request, model_admin):
#         obj = PeminatanLintasMinat()
#         jurusan = []
        
#         for data in Jurusan.objects.all():
#             jurusan.append((
#                 data.NAMA, data.NAMA)
#             )
        
#         return tuple(jurusan)
    
#     def get_filter_field(self):
#         filter_field = {
#             self.filter_field_name: self.value()
#         }
        
#         return filter_field

#     def queryset(self, request, queryset):
#         filter_field = self.get_filter_field()
#         if self.value():
#             return queryset.filter(**filter_field)
        

    
class PeminatanLintasMinatFilter(django_filters.FilterSet):
    JURUSAN = django_filters.ModelChoiceFilter(
        field_name="KELAS_SISWA__KELAS__KELAS__JURUSAN__NAMA",
        queryset=Jurusan.objects.all())
    # KELAS = django_filters.ChoiceFilter(
    #     choices=JadwalMengajar._meta.get_field('HARI').choices,
    #     field_name='JADWAL_MENGAJAR__HARI')

    class Meta:
        model = PeminatanLintasMinat
        fields = ('JURUSAN',)


# class JadwalMengajarGuruFilter(django_filters.FilterSet):
#     TAHUN_AJARAN = django_filters.ModelChoiceFilter(
#         field_name="TAHUN_AJARAN",
#         queryset=TahunAjaran.objects.all())
#     HARI = django_filters.ChoiceFilter(
#         choices=JadwalMengajar._meta.get_field('HARI').choices,
#         field_name='HARI')

#     class Meta:
#         model = JadwalMengajar
#         fields = ('TAHUN_AJARAN', 'HARI')