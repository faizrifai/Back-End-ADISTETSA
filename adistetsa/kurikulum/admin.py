from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin, ExportMixin
from .filter_admin import *
from .models import *
from .importexportresources import *

# Register your models here.
admin.site.register(BulanMinggu)
admin.site.register(KegiatanPekanTidakEfektif)
admin.site.register(JadwalPekanTidakEfektif)
admin.site.register(JadwalPekanAktif)
admin.site.register(Mengajar)
admin.site.register(AbsensiSiswa)
admin.site.register(Jurusan)
admin.site.register(TipeKelas)

# utility function

def deskripsi_materi(obj):
    name = "%s" % obj.DESKRIPSI_MATERI
    return Truncator(name).chars(10)

def deskripsi_tata_tertib(obj):
    name = "%s" % obj.KETERANGAN
    return Truncator(name).chars(50)

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


# custom admin page

class TahunAjaranAdmin(admin.ModelAdmin):
    search_fields = ['TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN_AKHIR']

    def get_ordering(self, request):
        return ['TAHUN_AJARAN_AWAL']

admin.site.register(TahunAjaran, TahunAjaranAdmin)

class KTSPAdmin(admin.ModelAdmin):
    list_display = ('TAHUN_AJARAN', 'NAMA_FILE')
    list_per_page = 10
    search_fields = ['TAHUN_AJARAN']
    list_filter = (TahunFilter,)

admin.site.register(KTSP, KTSPAdmin)

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

class WaktuPelajaranAdmin(admin.ModelAdmin):
    search_fields = ['WAKTU_MULAI', 'WAKTU_BERAKHIR', 'JAM_KE']

admin.site.register(WaktuPelajaran, WaktuPelajaranAdmin)
    
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
    list_display = ('aksi', 'get_mata_pelajaran', 'get_tahun_ajaran', 'get_semester', 'TANGGAL_MENGAJAR',  deskripsi_materi, 'FILE_DOKUMENTASI')
    list_per_page = 10
    search_fields = ['TANGGAL_MENGAJAR', 'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI']
    # list_filter = (JadwalMengajarFilter,)
    autocomplete_fields = ['GURU', 'JADWAL_MENGAJAR']
    
    def aksi(self, obj):
        return "Edit"
    
    def jadwal_mengajar(self, obj):
        jadwal_mengajar = JadwalMengajar.objects.get(pk=obj.JADWAL_MENGAJAR.ID)

        base_url = reverse('admin:kurikulum_jadwalmengajar_changelist')
        
        return mark_safe(u'<a href="%s?Jpk__exact=%d">%s</a>' % (base_url, jadwal_mengajar.ID, str(obj.JADWAL_MENGAJAR)))
    
    def get_mata_pelajaran(self, obj):
        return obj.JADWAL_MENGAJAR.MATA_PELAJARAN
    def get_tahun_ajaran(self, obj):
        return obj.JADWAL_MENGAJAR.TAHUN_AJARAN
    def get_semester(self, obj):
        return obj.JADWAL_MENGAJAR.SEMESTER
    
    
    get_mata_pelajaran.short_description = 'MATA PELAJARAN'
    get_tahun_ajaran.short_description = 'TAHUN AJARAN'
    get_semester.short_description = 'SEMESTER'

    # def pelajaran(self, obj):
    #     pelajaran = Pelajaran.objects.get(ID=obj.PELAJARAN.ID)

    #     base_url = reverse('admin:kurikulum_pelajaran_changelist')
        
    #     return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, pelajaran.ID, str(pelajaran)))

admin.site.register(JurnalBelajar, JurnalBelajarAdmin)

class KelasSiswaAdmin(admin.ModelAdmin):
    search_fields = ['NIS__NIS', 'NIS__NAMA']
    list_display = ('get_nis','get_nama', 'KELAS')
    list_per_page = 10 
    list_filter = (KelasFilter,)
    autocomplete_fields = ['NIS', 'KELAS']
    
    def get_nis(self, obj):
        return obj.NIS.NIS
    def get_nama(self, obj):
        return obj.NIS.NAMA
    
    
    get_nis.short_description = 'NIS'
    get_nama.short_description = 'NAMA'
    
admin.site.register(KelasSiswa, KelasSiswaAdmin)

class KategoriTataTertibAdmin(admin.ModelAdmin):
    search_fields = ['NAMA']
    list_per_page = 10

admin.site.register(KategoriTataTertib, KategoriTataTertibAdmin)

class TataTertibAdmin(ImportExportModelAdmin):
    search_fields = ['KETERANGAN', 'KATEGORI']
    list_display = (deskripsi_tata_tertib, 'KATEGORI',)
    list_per_page = 10
    list_filter = [KategoriTataTertibFilter]

    resource_class = TataTertibResource

admin.site.register(TataTertib, TataTertibAdmin)

class PoinPelanggaranAdmin(ImportExportModelAdmin):
    search_fields = ['KETERANGAN','POIN', ]
    list_display = (deskripsi_tata_tertib,'POIN',)
    list_per_page = 10

    resource_class = PoinPelanggaranResource

admin.site.register(PoinPelanggaran, PoinPelanggaranAdmin)

class JadwalHarianAdmin(admin.ModelAdmin):
    search_fields = ['HARI']
    list_per_page = 10
    filter_horizontal = ('PELAJARAN',)
    list_display = ('HARI', 'KELAS')
    list_filter = ['HARI', KelasFilter,]
    
    def aksi(self, obj):
        return "Detail"

admin.site.register(JadwalHarian, JadwalHarianAdmin)

class JadwalMengajarAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['GURU__NAMA_LENGKAP', 'TAHUN_AJARAN__TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR', 'SEMESTER__KE', 'KELAS__NAMA', 'MATA_PELAJARAN__NAMA']
    list_per_page = 10
    filter_horizontal = ('WAKTU_PELAJARAN',)
    exclude = ('JUMLAH_WAKTU',)
    list_display = ('GURU', 'TAHUN_AJARAN', 'SEMESTER', 'KELAS', 'MATA_PELAJARAN', 'HARI', 'jam_pelajaran')
    list_filter = [TahunFilter ,SemesterFilter ,'HARI', KelasFilter, MataPelajaranFilter,WaktuPelajaranFIlter, GuruFilter]

    resource_class = JadwalMengajarResource

    def jam_pelajaran(self, obj):
        daftar = ""
        for data in obj.WAKTU_PELAJARAN.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(JadwalMengajar, JadwalMengajarAdmin)

class JadwalPekanEfektifSemesterAdmin(admin.ModelAdmin):
    filter_horizontal = ('BANYAK_MINGGU',)
    
admin.site.register(JadwalPekanEfektifSemester, JadwalPekanEfektifSemesterAdmin)