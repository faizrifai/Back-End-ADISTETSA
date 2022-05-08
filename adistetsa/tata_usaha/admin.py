from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin

from kurikulum.admin import RaportAdmin
from .models import *
from .forms import *
from .importexportresources import *
from subadmin import SubAdmin, RootSubAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse



# Register your models here.
class DataBeasiswaSiswaAdmin(SubAdmin):
    model = DataBeasiswaSiswa
    # model = MutasiKeluar
    list_display = ('aksi', 'TAHUN', 'KELAS', 'DARI')
    list_per_page = 10
    search_fields = ['TAHUN', 'KELAS', 'DARI']
    autocomplete_fields = ['BUKU_INDUK']
    exclude = ('ID',)
    autocomplete_fields = ['BUKU_INDUK']

    def aksi(self, obj):
        return "Edit"


class BukuIndukAdmin(RootSubAdmin):
    search_fields = []
    list_display = ('nama','nis','aksi_beasiswa','aksi_raport', 'HASIL_EXPORT')
    readonly_fields = ('DITERIMA_DI_KELAS','KELOMPOK','ORANG_TUA',)
    autocomplete_fields = ['NIS']
    autocomplete_fields = ['NIS']
    # inlines = [DataSiswaTabular,]

    subadmins = [DataBeasiswaSiswaAdmin, RaportAdmin]
    def nis(self, obj):
        return DataSiswa.objects.get(NIS=obj.NIS.NIS).NIS
    
    def nama(self, obj):
        return DataSiswa.objects.get(NIS=obj.NIS.NIS).NAMA
    
    def aksi_beasiswa(self, obj):
        base_url = reverse('admin:tata_usaha_bukuinduk_changelist')
        
        return mark_safe(u'<a href="%s%d/databeasiswasiswa">%s</a>' % (base_url, obj.ID, 'Buka Beasiswa'))
    
    def aksi_raport(self, obj):
        base_url = reverse('admin:tata_usaha_bukuinduk_changelist')
        
        return mark_safe(u'<a href="%s%d/raport">%s</a>' % (base_url, obj.ID, 'Buka Raport'))
    
    
    # <button style="background-color: #04AA6D; border:0px; border-radius:2px; color:white; padding: 5px; font-size: 12px;" >
    

admin.site.register(BukuInduk, BukuIndukAdmin)

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