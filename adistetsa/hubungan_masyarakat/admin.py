from django.contrib import admin
from .forms import *
from import_export.admin import ExportMixin
from .models import *
from .importexportresources import*
import datetime


# Register your models here.
class LogUKSSiswaAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['NAMA__NIS__NAMA', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN']
    list_display = ('NAMA','kelas', 'nisn', 'TANGGAL','JENIS_PEMERIKSAAN','OBAT_DIBERIKAN','TINDAK_LANJUT')
    list_filter = ('TANGGAL','JENIS_PTK')
    readonly_fields = ('JENIS_PTK',)
    autocomplete_fields = ('NAMA',)
    # form = LogUKSSiswaForm
    resource_class = LogUKSSiswaResource
    
    def kelas (self, obj):
        return obj.NAMA.KELAS
    
    def nisn (self, obj):
        return obj.NAMA.NIS.NISN 
    
admin.site.register(LogUKSSiswa, LogUKSSiswaAdmin)

class LogUKSTendikAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['NAMA__NAMA_LENGKAP', 'JENIS_PTK', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN']
    list_display = ('NAMA','JENIS_PTK','TANGGAL','JENIS_PEMERIKSAAN','OBAT_DIBERIKAN','TINDAK_LANJUT')
    list_filter = ('TANGGAL','JENIS_PTK')
    autocomplete_fields = ('NAMA', )
    resource_class = LogUKSTendikResource
    
admin.site.register(LogUKSTendik, LogUKSTendikAdmin)

class LogUKSKaryawanAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['NAMA__NAMA_LENGKAP', 'JENIS_PTK', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN']
    list_display = ('NAMA','JENIS_PTK','TANGGAL','JENIS_PEMERIKSAAN','OBAT_DIBERIKAN','TINDAK_LANJUT')
    list_filter = ('TANGGAL','JENIS_PTK')
    autocomplete_fields = ('NAMA',)
    resource_class = LogUKSKaryawanResource
    
admin.site.register(LogUKSKaryawan, LogUKSKaryawanAdmin)

class BukuTamuAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['NAMA', 'INSTANSI_ASAL','KEPERLUAN']
    list_display = ('NAMA','INSTANSI_ASAL','ALAMAT','NO_HP','HARI','TANGGAL','KEPERLUAN')
    resource_class = BukuTamuResource
    exclude = ('HARI',)

    
admin.site.register(BukuTamu, BukuTamuAdmin)