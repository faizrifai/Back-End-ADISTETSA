from django.contrib import admin
from .forms import *
from import_export.admin import ExportMixin
from .models import *
from .importexportresources import*
import datetime

# Register your models here.
class LogUKSSiswaAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('NAMA','KELAS','NISN','TANGGAL','JENIS_PEMERIKSAAN','OBAT_DIBERIKAN','TINDAK_LANJUT')
    list_filter = ('TANGGAL','JENIS_PTK')
    readonly_fields = ('JENIS_PTK',)
    form = LogUKSSiswaForm
    resource_class = LogUKSSiswaResource
    
admin.site.register(LogUKSSiswa, LogUKSSiswaAdmin)

class LogUKSTendikAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('NAMA','JENIS_PTK','TANGGAL','JENIS_PEMERIKSAAN','OBAT_DIBERIKAN','TINDAK_LANJUT')
    list_filter = ('TANGGAL','JENIS_PTK')
    resource_class = LogUKSTendikResource
    
admin.site.register(LogUKSTendik, LogUKSTendikAdmin)

class BukuTamuAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('NAMA','INSTANSI_ASAL','ALAMAT','NO_HP','HARI','TANGGAL','KEPERLUAN')
    resource_class = BukuTamuResource
    exclude = ('HARI',)

    
admin.site.register(BukuTamu, BukuTamuAdmin)