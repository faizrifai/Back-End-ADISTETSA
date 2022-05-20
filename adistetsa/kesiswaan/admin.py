from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin, ExportMixin
from kesiswaan.importexportresources import *
from kesiswaan.filter_admin import TahunAjaranFilter, SemesterFilter, DataSiswaFilter, EkskulFilter
from kustom_autentikasi.models import DataPelatihUser
from .models import *
from subadmin import SubAdmin, RootSubAdmin
from .importexportresources import *
from utility.subadminexport import BaseSubAdminExport
from utility.permissions import is_in_group

class PengajuanLaporanPelanggaranAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA',)
    list_display = ('DATA_SISWA', 'BUKTI_PELANGGARAN', 'JENIS_PELANGGARAN', 'TANGGAL_PENGAJUAN','status_pengajuan')
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PELANGGARAN',]
    actions = ('accept_action', 'decline_action',)
    list_filter = (DataSiswaFilter,)
    exclude = ('STATUS_PENGAJUAN',)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanLaporanPelanggaran.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan laporan"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanLaporanPelanggaran.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan laporan"
    
    def status_pengajuan(self, obj):
        return (obj.STATUS_PENGAJUAN == 'Disetujui')       
        
    status_pengajuan.boolean = True
    
    # def setuju(self, obj):
    #     data = PengajuanLaporanPelanggaran.objects.get(ID=obj.ID)
    #     data.STATUS_PENGAJUAN = 'Disetujui'
    #     data.save()


admin.site.register(PengajuanLaporanPelanggaran, PengajuanLaporanPelanggaranAdmin)


class PelanggaranSiswaAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA',)
    list_display = ('DATA_SISWA', 'POIN',)
    list_per_page =  10 
    list_filter = (DataSiswaFilter,)
    resource_class = PelanggaranSiswaResource
    autocomplete_fields = ['DATA_SISWA', ]

admin.site.register(PelanggaranSiswa, PelanggaranSiswaAdmin)

class RiwayatLaporanPelanggaranAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA',)
    list_display = ('DATA_SISWA', 'BUKTI_PELANGGARAN', 'JENIS_PELANGGARAN','TANGGAL_PENGAJUAN', 'STATUS_PENGAJUAN')
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PELANGGARAN',]
    list_filter = (DataSiswaFilter,)
    resource_class = RiwayatLaporanPelanggaranResource
    
    
admin.site.register(RiwayatLaporanPelanggaran, RiwayatLaporanPelanggaranAdmin)

class KategoriProgramKebaikanAdmin(ImportExportModelAdmin):
    search_fields = ('NAMA',)
    list_display = ('NAMA',)
    list_per_page = 10 
    resource_class = KategoriProgramKebaikanResource
    
admin.site.register(KategoriProgramKebaikan, KategoriProgramKebaikanAdmin)

class ProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('KETERANGAN', 'KATEGORI__NAMA',)
    list_display = ('KETERANGAN', 'KATEGORI',)
    list_per_page = 10 
    autocomplete_fields = ('KATEGORI',)

admin.site.register(ProgramKebaikan, ProgramKebaikanAdmin)

class PoinProgramKebaikanAdmin(ImportExportModelAdmin):
    search_fields = ('KETERANGAN', 'POIN',)
    list_display = ('KETERANGAN', 'POIN',)
    list_per_page = 10 
    resource_class = PoinProgramKebaikanResource

admin.site.register(PoinProgramKebaikan, PoinProgramKebaikanAdmin)

class PengajuanProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA',)
    list_display = ['DATA_SISWA', 'BUKTI_PROGRAM_KEBAIKAN', 'JENIS_PROGRAM_KEBAIKAN','TANGGAL_PENGAJUAN', 'status_pengajuan',]
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PROGRAM_KEBAIKAN',]
    actions = ('accept_action', 'decline_action',)
    list_filter = (DataSiswaFilter,)
    exclude = ('STATUS_PENGAJUAN',)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanProgramKebaikan.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan program kebaikan"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanProgramKebaikan.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan program kebaikan"
    
    def status_pengajuan(self, obj):
        return (obj.STATUS_PENGAJUAN == 'Disetujui')       
        
    status_pengajuan.boolean = True
    
    # def setuju(self, obj):
    #     data = PengajuanLaporanPelanggaran.objects.get(ID=obj.ID)
    #     data.STATUS_PENGAJUAN = 'Disetujui'
    #     data.save()


admin.site.register(PengajuanProgramKebaikan, PengajuanProgramKebaikanAdmin)

class RiwayatProgramKebaikanAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA',)
    list_display = ['DATA_SISWA', 'BUKTI_PROGRAM_KEBAIKAN', 'JENIS_PROGRAM_KEBAIKAN','TANGGAL_PENGAJUAN', 'STATUS_PENGAJUAN',]
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PROGRAM_KEBAIKAN',]
    list_filter = (DataSiswaFilter,)
    resource_class = RiwayatProgramKebaikanResource
    
admin.site.register(RiwayatProgramKebaikan, RiwayatProgramKebaikanAdmin)

class AnggotaEkskulAdmin(BaseSubAdminExport):
    model = AnggotaEkskul
    search_fields = ('KELAS_SISWA__NIS__NAMA',)
    list_display = ('KELAS_SISWA', 'EKSKUL','TAHUN_AJARAN', 'STATUS')
    list_per_page = 10
    list_filter = ('STATUS', TahunAjaranFilter,)
    resource_class = AnggotaEkskulResource
    autocomplete_fields = ['KELAS_SISWA', 'TAHUN_AJARAN','EKSKUL',]
    # readonly_fields = ('NIS', 'JURNAL_EKSKUL')


class KatalogEkskulAdmin(RootSubAdmin , ImportExportModelAdmin):
    search_fields = ['NAMA', 'KATEGORI',]
    list_per_page = 10
    list_display = ('NAMA', 'KATEGORI', 'DESKRIPSI', 'DOKUMENTASI', 'aksi')
    list_filter = ('KATEGORI', )
    resource_class = KatalogEkskulResource
    subadmins = [AnggotaEkskulAdmin]

    def aksi(self, obj):
        base_url = reverse('admin:kesiswaan_katalogekskul_changelist')
        
        return mark_safe(u'<a href="%s%d/anggotaekskul">%s</a>' % (base_url, obj.ID, 'Buka Anggota'))

admin.site.register(KatalogEkskul, KatalogEkskulAdmin)


class JadwalEkskulAdmin(ImportExportModelAdmin):
    search_fields = ('PELATIH__NAMA','EKSKUL__NAMA','TAHUN_AJARAN__TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR','SEMESTER__NAMA',)
    list_display = ['PELATIH', 'TAHUN_AJARAN', 'SEMESTER', 'EKSKUL','HARI','WAKTU_MULAI','WAKTU_BERAKHIR',]
    list_per_page = 10 
    autocomplete_fields = ('PELATIH', 'TAHUN_AJARAN', 'SEMESTER', 'EKSKUL',)
    list_filter = (TahunAjaranFilter,SemesterFilter,EkskulFilter,'HARI')
    resource_class = JadwalEkskulResource
    

admin.site.register(JadwalEkskul, JadwalEkskulAdmin)

class AbsensiEkskulAdmin(SubAdmin):
    model = AbsensiEkskul
    search_fields = ('NIS__NAMA',)
    list_display = ('NIS', 'KETERANGAN', 'FILE_KETERANGAN', 'ekskul', 'pertemuan')
    list_per_page = 10
    readonly_fields = ('NIS', 'JURNAL_EKSKUL')
    autocomplete_fields = ['NIS', 'JURNAL_EKSKUL',]
    
    def ekskul(self, obj):
        return obj.JURNAL_EKSKUL.DAFTAR.EKSKUL
    
    def pertemuan(self, obj):
        return obj.JURNAL_EKSKUL.PERTEMUAN

class JurnalEkskulAdmin(BaseSubAdminExport):
    model = JurnalEkskul
    list_display = ('aksi', 'PELATIH', 'PERTEMUAN', 'TANGGAL_MELATIH',  'DESKRIPSI_KEGIATAN', 'FILE_DOKUMENTASI', 'absensi')
    list_per_page = 10
    search_fields = ['TANGGAL_MELATIH', 'DESKRIPSI_KEGIATAN', 'FILE_DOKUMENTASI']
    autocomplete_fields = ['DAFTAR','PELATIH']
    exclude = ('PELATIH',)
    resource_class = JurnalEkskulResource

    subadmins = [AbsensiEkskulAdmin]

    def aksi(self, obj):
        return "Edit"
    
    def absensi(self, obj):
        base_url = reverse('admin:kesiswaan_daftarjurnalekskul_changelist')
        
        return mark_safe(u'<a href="%s%d/jurnalekskul/%d/absensiekskul">%s</a>' % (base_url, obj.DAFTAR.ID, obj.ID, 'Buka Absensi'))

# class JurnalEkskulAdmin(admin.ModelAdmin):
#     search_fields = ('',)
#     list_display = ['PELATIH', 'PERTEMUAN', 'TANGGAL_MELATIH', 'DESKRIPSI_KEGIATAN','FILE_DOKUMENTASI','DAFTAR',]
#     list_per_page = 10 
#     # autocomplete_fields = ['',]
#     # list_filter = (DataSiswaFilter,)
    
# admin.site.register(JurnalEkskul, JurnalEkskulAdmin)

class DaftarJurnalEkskulAdmin(RootSubAdmin):
    search_fields = ('PELATIH__NAMA','EKSKUL__NAMA',)
    list_per_page = 10
    list_display = ('PELATIH', 'EKSKUL', 'SEMESTER', 'JADWAL_EKSKUL', 'aksi')
    # list_filter = []
    autocomplete_fields = ['PELATIH', 'EKSKUL','SEMESTER','JADWAL_EKSKUL',]

    subadmins = [JurnalEkskulAdmin]

    def aksi(self, obj):
        base_url = reverse('admin:kesiswaan_daftarjurnalekskul_changelist')
        
        return mark_safe(u'<a href="%s%d/jurnalekskul">%s</a>' % (base_url, obj.ID, 'Buka Jurnal'))

admin.site.register(DaftarJurnalEkskul, DaftarJurnalEkskulAdmin)


# class DaftarJurnalEkskulAdmin(admin.ModelAdmin):
#     search_fields = ('',)
#     list_display = ['PELATIH', 'SEMESTER', 'JADWAL_EKSKUL',]
#     list_per_page = 10 
#     # autocomplete_fields = ['',]
#     # list_filter = (DataSiswaFilter,)
    
# admin.site.register(DaftarJurnalEkskul, DaftarJurnalEkskulAdmin)



class PengajuanEkskulAdmin(admin.ModelAdmin):
    search_fields = ('KELAS_SISWA__NIS__NAMA','EKSKUL__NAMA',)
    list_display = ['KELAS_SISWA', 'EKSKUL','TAHUN_AJARAN', 'TANGGAL_PENGAJUAN', 'STATUS_PENGAJUAN',]
    list_per_page = 10 
    list_filter = ('STATUS_PENGAJUAN', )
    actions = ('accept_action', 'decline_action',)
    exclude = ('STATUS_PENGAJUAN', )
    autocomplete_fields = ('KELAS_SISWA', 'EKSKUL','TAHUN_AJARAN',)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanEkskul.objects.get(ID=d['ID'])
            obj.save()
    
    accept_action.short_description = "Setujui pengajuan ekskul"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanEkskul.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan ekskul"
    
admin.site.register(PengajuanEkskul, PengajuanEkskulAdmin)

    
class ProgramKerjaEkskulAdmin(admin.ModelAdmin):
    search_fields = ('PELATIH__NAMA', 'EKSKUL__NAMA', )
    list_display = ('PELATIH', 'EKSKUL', 'TAHUN_AJARAN', 'FILE_PROGRAM_KERJA',)
    list_per_page = 10
    autocomplete_fields = ('PELATIH', 'EKSKUL', 'TAHUN_AJARAN',)

admin.site.register(ProgramKerjaEkskul, ProgramKerjaEkskulAdmin)

class AnggotaEkskulRegisterAdmin(admin.ModelAdmin):
    search_fields = ('KELAS_SISWA__NIS__NAMA',)
    list_display = ('KELAS_SISWA', 'EKSKUL','TAHUN_AJARAN', 'STATUS')
    list_per_page = 10
    list_filter = ('STATUS', TahunAjaranFilter,)
    # readonly_fields = ('NIS', 'JURNAL_EKSKUL')

admin.site.register(AnggotaEkskul, AnggotaEkskulRegisterAdmin)

class NilaiEkskulAdmin(BaseSubAdminExport):
    model = NilaiEkskul
    search_fields = ('DATA_ANGGOTA__KELAS_SISWA__NIS__NAMA', 'DATA_ANGGOTA__EKSKUL__NAMA', )
    list_display = ['DATA_ANGGOTA', 'ekskul', 'PREDIKAT', 'status_predikat', 'SEMESTER', 'DESKRIPSI']
    list_per_page = 10 
    exclude = ['DATA_ANGGOTA', 'RAPORT']
    resource_class = NilaiEkskulResource
    
    def status_predikat(self, obj):
        if obj.PREDIKAT == 'A':
            return 'SANGAT BAIK' 
        elif obj.PREDIKAT == 'B':
            return 'BAIK'
        elif obj.PREDIKAT == 'C':
            return 'CUKUP' 
        elif obj.PREDIKAT == 'D':
            return 'KURANG'
        elif obj.PREDIKAT == 'E':
            return 'SANGAT KURANG'
        
    def ekskul(self, obj):
        return obj.DATA_ANGGOTA.EKSKUL.NAMA
        

class NilaiEkskulPelatihAdmin(admin.ModelAdmin):
    search_fields = ['DATA_ANGGOTA__KELAS_SISWA__NIS__NAMA', 'DATA_ANGGOTA__EKSKUL__NAMA']
    list_display = ['DATA_ANGGOTA', 'ekskul', 'PREDIKAT', 'status_predikat', 'SEMESTER', 'DESKRIPSI']
    list_per_page = 10
    exclude = ['DATA_ANGGOTA', 'RAPORT']
    resource_class = NilaiEkskulResource

    def get_queryset(self, request):
        if is_in_group(request.user, 'Pelatih'):
            pelatih = DataPelatihUser.objects.get(USER=request.user).DATA_PELATIH
            jadwal_ekskul = JadwalEkskul.objects.filter(PELATIH=pelatih)
            tahun_ajaran = jadwal_ekskul.values('TAHUN_AJARAN')
            ekskul = jadwal_ekskul.values('EKSKUL')
            anggota = AnggotaEkskul.objects.filter(TAHUN_AJARAN__ID__in=tahun_ajaran, EKSKUL__ID__in=ekskul).values('ID')
            queryset = NilaiEkskul.objects.filter(DATA_ANGGOTA__ID__in=anggota)

            return queryset
        
        return NilaiEkskul.objects.all()

    def status_predikat(self, obj):
        if obj.PREDIKAT == 'A':
            return 'SANGAT BAIK' 
        elif obj.PREDIKAT == 'B':
            return 'BAIK'
        elif obj.PREDIKAT == 'C':
            return 'CUKUP' 
        elif obj.PREDIKAT == 'D':
            return 'KURANG'
        elif obj.PREDIKAT == 'E':
            return 'SANGAT KURANG'
        
    def ekskul(self, obj):
        return obj.DATA_ANGGOTA.EKSKUL.NAMA

admin.site.register(NilaiEkskulPelatih, NilaiEkskulPelatihAdmin)