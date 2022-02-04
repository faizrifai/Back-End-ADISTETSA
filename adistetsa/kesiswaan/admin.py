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
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanLaporanPelanggaran.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan peminjaman"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanLaporanPelanggaran.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan peminjaman"
    
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