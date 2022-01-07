from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from .importexportresources import *

from django.contrib.admin import ModelAdmin, SimpleListFilter

# Register your models here.
# admin.site.register(KTSP)
admin.site.register(MataPelajaran)
# admin.site.register(SilabusRPB)
admin.site.register(BulanMinggu)
admin.site.register(JadwalPekanEfektifSemester)
admin.site.register(KegiatanPekanTidakEfektif)
admin.site.register(JadwalPekanTidakEfektif)
admin.site.register(JadwalPekanAktif)
admin.site.register(DeskripsiTataTertib)
admin.site.register(TataTertib)
admin.site.register(Mengajar)
admin.site.register(WaktuPelajaran)
admin.site.register(Pelajaran)
admin.site.register(JadwalHarian)
# admin.site.register(JadwalPelajaran)
admin.site.register(KelasSiswa)
admin.site.register(AbsensiSiswa)
# admin.site.register(JurnalBelajar)
admin.site.register(TahunAjaran)
admin.site.register(DataSemester)

class KelasAdmin(ImportExportModelAdmin):
    list_per_page = 10
    exclude = ['KODE_KELAS']
    
admin.site.register(Kelas, KelasAdmin)

class TahunFilter(SimpleListFilter):
    title = "Tahun Ajaran"  
    parameter_name = "filter"

    def lookups(self, request, model_admin):
        ktsp = TahunAjaran.objects.all()
        tahun_ajaran = []
        for data in ktsp.values():
            str_tahun = str(data['TAHUN_AJARAN_AWAL']) + '/' + str(data['TAHUN_AJARAN_AKHIR'])
            tahun_ajaran.append((str_tahun, str_tahun))
            
        return tahun_ajaran

    def queryset(self, request, queryset):
        if self.value():
            tahun_ajaran = self.value().split('/')
            return queryset.filter(TAHUN_AJARAN_AWAL=tahun_ajaran[0], TAHUN_AJARAN_AKHIR=tahun_ajaran[1])

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

    def aksi(self, obj):
        return 'Detail'
    
admin.site.register(JadwalPelajaran, JadwalPelajaranAdmin)


class SilabusMataPelajaranFilter(SimpleListFilter):
    title = "Mata Pelajaran"  
    parameter_name = "filter"

    def lookups(self, request, model_admin):
        silabus = SilabusRPB.objects.all()
        mata_pelajaran = []
        for data in silabus.values():
            mapel = MataPelajaran.objects.get(KODE=data['MATA_PELAJARAN_id'])
            str_mapel = mapel.NAMA
            
            mata_pelajaran.append((str_mapel, str_mapel))
            
        return mata_pelajaran

    def queryset(self, request, queryset):
        if self.value():
            mata_pelajaran = self.value()
            return queryset.filter(MATA_PELAJARAN__NAMA = mata_pelajaran )


class SilabusRPBAdmin(admin.ModelAdmin):
    list_display = ('MATA_PELAJARAN', 'TAHUN_AJARAN', 'NAMA_FILE', 'KELAS')
    list_per_page = 10
    search_fields = ['MATA_PELAJARAN__NAMA', 'KELAS__KODE_KELAS']
    list_filter = (TahunFilter, SilabusMataPelajaranFilter,)

admin.site.register(SilabusRPB, SilabusRPBAdmin)



class JurnalBelajarAdmin(admin.ModelAdmin):
    list_display = ('KELAS', 'TANGGAL_MENGAJAR', 'PELAJARAN', 'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI')
    list_per_page = 10
    search_fields = ['KELAS__KODE_KELAS', 'TANGGAL_MENGAJAR', 'SEMESTER__KE', 'PELAJARAN__MATA_PELAJARAN__KODE', 'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI']
    list_filter = (TahunFilter,)

admin.site.register(JurnalBelajar, JurnalBelajarAdmin)