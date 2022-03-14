from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from .models import *
from .forms import *
from .importexportresources import *

# Register your models here.
class MutasiMasukAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('NAMA_SISWA','ASAL_SEKOLAH','NO_INDUK_ASAL','ALAMAT','KELAS','NO_INDUK_BARU','TANGGAL_SURAT','NO_SURAT','BULAN','TAHUN')
    list_filter = ('BULAN','TAHUN')
    form = MutasiMasukForm
    resource_class = MutasiMasukResource
    
admin.site.register(MutasiMasuk, MutasiMasukAdmin)

class MutasiKeluarAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('NAMA_SISWA','KELAS','NO_INDUK','PINDAH_KE','TANGGAL_SURAT','NO_SURAT','BULAN','TAHUN')
    list_filter = ('BULAN','TAHUN')
    form = MutasiKeluarForm
    resource_class = MutasiKeluarResource
    
admin.site.register(MutasiKeluar, MutasiKeluarAdmin)