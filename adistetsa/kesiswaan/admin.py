from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin, ExportMixin

from kesiswaan.filter_admin import DataSiswaFilter
# from .filter_admin import *
from .models import *
# from .importexportresources import *

class PengajuanLaporanPelanggaranAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA_LENGKAP',)
    list_display = ('DATA_SISWA', 'BUKTI_PELANGGARAN', 'JENIS_PELANGGARAN', 'status_pengajuan')
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


class PelanggaranSiswaAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA_LENGKAP',)
    list_display = ('DATA_SISWA', 'POIN',)
    list_per_page =  10 
    list_filter = (DataSiswaFilter,)

admin.site.register(PelanggaranSiswa, PelanggaranSiswaAdmin)

class RiwayatLaporanPelanggaranAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA_LENGKAP',)
    list_display = ('DATA_SISWA', 'BUKTI_PELANGGARAN', 'JENIS_PELANGGARAN', 'STATUS_PENGAJUAN')
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PELANGGARAN',]
    list_filter = (DataSiswaFilter,)
    
admin.site.register(RiwayatLaporanPelanggaran, RiwayatLaporanPelanggaranAdmin)

class KategoriProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('NAMA',)
    list_display = ('NAMA',)
    list_per_page = 10 
    
admin.site.register(KategoriProgramKebaikan, KategoriProgramKebaikanAdmin)

class ProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('KETERANGAN', 'KATEGORI__NAMA',)
    list_display = ('KETERANGAN', 'KATEGORI',)
    list_per_page = 10 
    autocomplete_fields = ('KATEGORI',)

admin.site.register(ProgramKebaikan, ProgramKebaikanAdmin)

class PoinProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('KETERANGAN', 'POIN',)
    list_display = ('KETERANGAN', 'POIN',)
    list_per_page = 10 

admin.site.register(PoinProgramKebaikan, PoinProgramKebaikanAdmin)

class PengajuanProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA_LENGKAP',)
    list_display = ['DATA_SISWA', 'BUKTI_PROGRAM_KEBAIKAN', 'JENIS_PROGRAM_KEBAIKAN', 'status_pengajuan',]
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

class RiwayatProgramKebaikanAdmin(admin.ModelAdmin):
    search_fields = ('DATA_SISWA__NAMA_LENGKAP',)
    list_display = ['DATA_SISWA', 'BUKTI_PROGRAM_KEBAIKAN', 'JENIS_PROGRAM_KEBAIKAN', 'STATUS_PENGAJUAN',]
    list_per_page = 10 
    autocomplete_fields = ['DATA_SISWA', 'JENIS_PROGRAM_KEBAIKAN',]
    list_filter = (DataSiswaFilter,)
    
admin.site.register(RiwayatProgramKebaikan, RiwayatProgramKebaikanAdmin)


    
