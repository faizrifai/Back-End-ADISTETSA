from django.contrib import admin
from django.utils.html import format_html
from .forms import KatalogKonselorForm
from kustom_autentikasi.models import DataGuruUser


from bimbingan_konseling.importexportresources import DataAlumniResource, KatalogKonselorResource, PeminatanLintasMinatResource
from .custom_filter import JurusanFilter, TingkatanFilter

from import_export.admin import ImportExportModelAdmin, ExportMixin
from .models import *

# Register your models here.
class DataAlumniAdmin(ImportExportModelAdmin):
    search_fields = []
    list_display = ('NAMA_SISWA','NISN','TAHUN_AJARAN','NAMA_PT','PROGRAM_STUDI','MEDIA_SOSIAL','EMAIL','ALAMAT','TEMPAT_BEKERJA')
    # exclude = ['NAMA']
    resource_class = DataAlumniResource
    
admin.site.register(DataAlumni, DataAlumniAdmin)

class PeminatanLintasMinatAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = []
    list_display = ('KELAS_SISWA', 'KATEGORI','FILE')
    list_filter = (JurusanFilter, TingkatanFilter)
    resource_class = PeminatanLintasMinatResource

admin.site.register(PeminatanLintasMinat, PeminatanLintasMinatAdmin)

class KatalogKonselorAdmin(ImportExportModelAdmin):
    search_fields = []
    list_display = ('aksi', 'nip','nama','KOMPETENSI','ALUMNUS', 'whatsapp', 'conference', 'STATUS')
    # exclude = ('WHATSAPP')
    resource_class = KatalogKonselorResource
    form = KatalogKonselorForm

    def aksi(self, obj):
        return str('Edit')
    
    def nip(self, obj):
        return str(DataGuruUser.objects.get(USER=obj.USER).DATA_GURU.NIP)
    
    def nama(self, obj):
        return str(DataGuruUser.objects.get(USER=obj.USER).DATA_GURU.NAMA_LENGKAP)
    
    def whatsapp(self, obj):
        return format_html('<a href="'+obj.WHATSAPP+'">Buka WA</a>')
    
    def conference(self, obj):
        return format_html('<a href="'+obj.CONFERENCE+'">Buka Conference</a>')
    
    
    # def kompetensi(self, obj):
    #     return obj.DATA_GURU.BIDANG_STUDI
    
    
admin.site.register(KatalogKonselor, KatalogKonselorAdmin)

class KonsultasiAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ('USER','KONSELOR', 'TANGGAL', 'JENIS_MASALAH')
    exclude = ('TANGGAL',)

admin.site.register(Konsultasi, KonsultasiAdmin)
