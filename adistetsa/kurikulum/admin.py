from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html
from admin_auto_filters.filters import AutocompleteFilter

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from .importexportresources import *

from django.contrib.admin import ModelAdmin, SimpleListFilter

# Register your models here.
# admin.site.register(KTSP)
# admin.site.register(MataPelajaran)
# admin.site.register(SilabusRPB)
admin.site.register(BulanMinggu)
admin.site.register(JadwalPekanEfektifSemester)
admin.site.register(KegiatanPekanTidakEfektif)
admin.site.register(JadwalPekanTidakEfektif)
admin.site.register(JadwalPekanAktif)
admin.site.register(Mengajar)
# admin.site.register(Pelajaran)
# admin.site.register(JadwalPelajaran)
# admin.site.register(KelasSiswa)
admin.site.register(AbsensiSiswa)
# admin.site.register(JurnalBelajar)
# admin.site.register(TahunAjaran)
admin.site.register(Jurusan)
admin.site.register(TipeKelas)

def deskripsi_materi(obj):
    name = "%s" % obj.DESKRIPSI_MATERI
    return Truncator(name).chars(10)

def deskripsi_tata_tertib(obj):
    name = "%s" % obj.KETERANGAN
    return Truncator(name).chars(50)

class TahunAjaranAdmin(admin.ModelAdmin):
    search_fields = ['TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN_AKHIR']

admin.site.register(TahunAjaran, TahunAjaranAdmin)

class PelajaranAdmin(admin.ModelAdmin):
    search_fields = ['MATA_PELAJARAN__NAMA', 'MATA_PELAJARAN__KODE' ]
    list_display = ('MATA_PELAJARAN', 'jam_pelajaran', 'GURU')
    filter_horizontal = ('WAKTU',)
    
    def jam_pelajaran(self, obj):
        daftar = ""
        for data in obj.WAKTU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)
    
admin.site.register(Pelajaran, PelajaranAdmin)

class KelasAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_KELAS']
    list_per_page = 10
    exclude = ['KODE_KELAS']
    
admin.site.register(Kelas, KelasAdmin)

class DataSemesterAdmin(admin.ModelAdmin):
    search_fields = ['KE', 'NAMA']
    exclude = ['NAMA']
    
admin.site.register(DataSemester, DataSemesterAdmin)

class MataPelajaranAdmin(admin.ModelAdmin):
    search_fields = ['KODE', 'NAMA']
    
admin.site.register(MataPelajaran, MataPelajaranAdmin)

# class TahunFilter(SimpleListFilter):
#     title = "Tahun Ajaran"  
#     parameter_name = "tahun_ajaran"

#     def lookups(self, request, model_admin):
#         ktsp = TahunAjaran.objects.all()
#         tahun_ajaran = []
#         for data in ktsp.values():
#             str_tahun = str(data['TAHUN_AJARAN_AWAL']) + '/' + str(data['TAHUN_AJARAN_AKHIR'])
#             tahun_ajaran.append((str_tahun, str_tahun))
            
#         return tahun_ajaran

#     def queryset(self, request, queryset):
#         nama_model = queryset.model.__name__
#         if self.value() and (nama_model == 'KTSP' or nama_model == 'SilabusRPB' or nama_model):
#             print(queryset.model.__name__)
#             tahun_ajaran = self.value().split('/')
#             return queryset.filter(TAHUN_AJARAN__TAHUN_AJARAN_AWAL=tahun_ajaran[0], TAHUN_AJARAN__TAHUN_AJARAN_AKHIR=tahun_ajaran[1])
#         elif self.value() and (nama_model == 'JurnalBelajar'):
#             print(queryset.model.__name__)
#             tahun_ajaran = self.value().split('/')
#             return queryset.filter(KELAS__TAHUN_AJARAN__TAHUN_AJARAN_AWAL=tahun_ajaran[0], KELAS__TAHUN_AJARAN__TAHUN_AJARAN_AKHIR=tahun_ajaran[1])
        
class TahunFilter(AutocompleteFilter):
    title = 'TAHUN AJARAN'
    field_name = 'TAHUN_AJARAN'

class KelasFilter(AutocompleteFilter):
    title = 'KELAS'
    field_name = 'KELAS'

class MataPelajaranFilter(AutocompleteFilter):
    title = 'MATA PELAJARAN'
    field_name = 'MATA_PELAJARAN'

class SemesterFilter(AutocompleteFilter):
    title = 'SEMESTER'
    field_name = 'SEMESTER'

class PelajaranFilter(AutocompleteFilter):
    title = 'PELAJARAN'
    field_name = 'PELAJARAN'
    
class NamaOfferingKelasFilter(AutocompleteFilter):
    title = 'OFFERING'
    field_name = 'OFFERING'

class WaktuPelajaranFIlter(AutocompleteFilter):
    title = 'WAKTU PELAJARAN'
    field_name = 'WAKTU_PELAJARAN'

class WaktuPelajaranAdmin(admin.ModelAdmin):
    search_fields = ['WAKTU_MULAI', 'WAKTU_BERAKHIR', 'JAM_KE']

admin.site.register(WaktuPelajaran, WaktuPelajaranAdmin)

class KTSPAdmin(admin.ModelAdmin):
    list_display = ('TAHUN_AJARAN', 'NAMA_FILE')
    list_per_page = 10
    search_fields = ['TAHUN_AJARAN']
    list_filter = (TahunFilter,)

admin.site.register(KTSP, KTSPAdmin)
    
class JadwalPelajaranAdmin(ImportExportModelAdmin):
    filter_horizontal = ('JADWAL_HARIAN',)
    list_per_page = 10
    search_fields = ['JADWAL_HARIAN__PELAJARAN__MATA_PELAJARAN__NAMA']
    list_display = ('TAHUN_AJARAN',)
    list_filter = (TahunFilter,)

    def aksi(self, obj):
        return 'Detail'
    
admin.site.register(JadwalPelajaran, JadwalPelajaranAdmin)

class SilabusRPBAdmin(admin.ModelAdmin):
    list_display = ('MATA_PELAJARAN', 'TAHUN_AJARAN', 'NAMA_FILE', 'KELAS')
    list_per_page = 10
    search_fields = ['MATA_PELAJARAN__NAMA', 'KELAS__KODE_KELAS', 'SEMESTER_NAMA']
    list_filter = (TahunFilter, MataPelajaranFilter, KelasFilter, SemesterFilter)

admin.site.register(SilabusRPB, SilabusRPBAdmin)

class NamaOfferingKelasAdmin(admin.ModelAdmin):
    search_fields = ['NAMA']
    list_per_page = 10

admin.site.register(NamaOfferingKelas, NamaOfferingKelasAdmin)

class OfferingKelasAdmin(admin.ModelAdmin):
    search_fields = ['KELAS__KODE_KELAS']
    list_per_page = 10
    list_filter = (KelasFilter, NamaOfferingKelasFilter,)
    list_display = ('KELAS', 'OFFERING',)

admin.site.register(OfferingKelas, OfferingKelasAdmin)

class JurnalBelajarAdmin(admin.ModelAdmin):
    list_display = ('aksi', 'kelas', 'TANGGAL_MENGAJAR', 'pelajaran', deskripsi_materi, 'FILE_DOKUMENTASI')
    list_per_page = 10
    search_fields = ['KELAS__KODE_KELAS', 'TANGGAL_MENGAJAR', 'SEMESTER__KE', 'PELAJARAN__MATA_PELAJARAN__KODE', 'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI']
    list_filter = (KelasFilter, SemesterFilter, PelajaranFilter,)
    
    def aksi(self, obj):
        return "Edit"
    
    def kelas(self, obj):
        daftar = KelasSiswa.objects.filter(pk=obj.KELAS.ID)

        base_url = reverse('admin:kurikulum_offeringkelas_changelist')
        
        return mark_safe(u'<a href="%s?KELAS__pk__exact=%d&OFFERING__pk__exact=%s">%s</a>' % (base_url, obj.KELAS.ID, obj.KELAS.OFFERING.ID, str(obj.KELAS)))
    
    def pelajaran(self, obj):
        pelajaran = Pelajaran.objects.get(ID=obj.PELAJARAN.ID)

        base_url = reverse('admin:kurikulum_pelajaran_changelist')
        
        return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, pelajaran.ID, str(pelajaran)))

admin.site.register(JurnalBelajar, JurnalBelajarAdmin)

class KelasSiswaAdmin(admin.ModelAdmin):
    search_fields = ['NIS__NIS', 'NIS__NAMA']
    list_display = ('get_nis','get_nama', 'KELAS')
    list_per_page = 10 
    list_filter = (KelasFilter,)
    
    def get_nis(self, obj):
        return obj.NIS.NIS
    def get_nama(self, obj):
        return obj.NIS.NAMA
    
    
    get_nis.short_description = 'NIS'
    get_nama.short_description = 'NAMA'
    
admin.site.register(KelasSiswa, KelasSiswaAdmin)

class TataTertibAdmin(admin.ModelAdmin):
    search_fields = ['KETERANGAN', 'POIN',]
    list_display = (deskripsi_tata_tertib, 'POIN',)
    list_per_page = 10

admin.site.register(TataTertib, TataTertibAdmin)

class JadwalHarianAdmin(admin.ModelAdmin):
    search_fields = ['HARI']
    list_per_page = 10
    filter_horizontal = ('PELAJARAN',)
    list_display = ('HARI', 'KELAS')
    list_filter = ['HARI', KelasFilter,]
    
    def aksi(self, obj):
        return "Detail"

admin.site.register(JadwalHarian, JadwalHarianAdmin)

class JadwalMengajarAdmin(admin.ModelAdmin):
    # search_fields = ['']
    list_per_page = 10
    filter_horizontal = ('WAKTU_PELAJARAN',)
    list_display = ('GURU', 'TAHUN_AJARAN', 'KELAS', 'MATA_PELAJARAN', 'HARI', 'jam_pelajaran')
    list_filter = [TahunFilter ,'HARI', KelasFilter, MataPelajaranFilter,WaktuPelajaranFIlter, ]
    
    def jam_pelajaran(self, obj):
        daftar = ""
        for data in obj.WAKTU_PELAJARAN.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)
    

admin.site.register(JadwalMengajar, JadwalMengajarAdmin)

    

