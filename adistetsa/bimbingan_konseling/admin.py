from django.contrib import admin
from django.utils.html import format_html
from .forms import KatalogKonselorForm
from kustom_autentikasi.models import DataGuruUser

from django.utils.safestring import mark_safe


from bimbingan_konseling.importexportresources import DataAlumniResource, KatalogKonselorResource, PeminatanLintasMinatResource
from .custom_filter import JurusanFilter, TingkatanFilter

from import_export.admin import ImportExportModelAdmin, ExportMixin
from .models import *

# Register your models here.
class DataAlumniAdmin(ImportExportModelAdmin):
    search_fields = ['NAMA_SISWA','NISN','TAHUN_AJARAN','NAMA_PT','PROGRAM_STUDI','MEDIA_SOSIAL','EMAIL','ALAMAT','TEMPAT_BEKERJA']
    list_display = ('NAMA_SISWA','NISN','TAHUN_AJARAN','NAMA_PT','PROGRAM_STUDI','MEDIA_SOSIAL','EMAIL','ALAMAT','TEMPAT_BEKERJA')
    # exclude = ['NAMA']
    resource_class = DataAlumniResource
    
admin.site.register(DataAlumni, DataAlumniAdmin)

class PeminatanLintasMinatAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['KELAS_SISWA__NIS__NAMA', 'KATEGORI']
    list_display = ('KELAS_SISWA', 'KATEGORI','FILE')
    list_filter = (JurusanFilter, TingkatanFilter)
    resource_class = PeminatanLintasMinatResource
    autocomplete_fields = ['KELAS_SISWA']

admin.site.register(PeminatanLintasMinat, PeminatanLintasMinatAdmin)

class KatalogKonselorAdmin(ImportExportModelAdmin):
    search_fields = ['NAMA', 'KOMPETENSI', 'ALUMNUS']
    list_display = ('aksi', 'foto', 'nip','NAMA','KOMPETENSI','ALUMNUS', 'whatsapp', 'conference','FOTO', 'STATUS')
    resource_class = KatalogKonselorResource
    form = KatalogKonselorForm
    autocomplete_fields = ['USER']

    def aksi(self, obj):
        return str('Edit')
    
    def nip(self, obj):
        return str(DataGuruUser.objects.get(USER=obj.USER).DATA_GURU.NIP)
    
    def foto(self, obj):
        if obj.FOTO:
            return mark_safe(u'<img src="%s" width="100" height="100"/>' % (obj.FOTO.url))
        else:
            return ''
    
    def whatsapp(self, obj):
        return format_html('<a href="'+obj.WHATSAPP+'">Buka WA</a>')
    
    def conference(self, obj):
        return format_html('<a href="'+obj.CONFERENCE+'">Buka Conference</a>')
    
    
    # def kompetensi(self, obj):
    #     return obj.DATA_GURU.BIDANG_STUDI
    
    
admin.site.register(KatalogKonselor, KatalogKonselorAdmin)

class KonsultasiAdmin(admin.ModelAdmin):
    search_fields = ['KONSELOR__NAMA', 'JENIS_MASALAH']
    list_display = ('USER','KONSELOR', 'TANGGAL_KONSULTASI','JAM_AWAL','JAM_AKHIR', 'JENIS_MASALAH','RATING', 'STATUS', 'KRITIK_SARAN',)
    list_per_page = 10
    list_filter = ('STATUS',)
    actions = ('accept_action', 'decline_action','konsultasi_action','feedback_action',)
    autocomplete_fields = ['USER', 'KONSELOR']
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS = 'Dijadwalkan')
        for d in queryset.values():
            obj = Konsultasi.objects.get(ID=d['ID'])
            obj.save()
        
    accept_action.short_description = "Setujui pengajuan konsultasi"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS = 'Ditolak')
        for d in queryset.values():
            obj = Konsultasi.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan konsultasi"
    
    def konsultasi_action(self, request, queryset):
        queryset.update(STATUS = 'Selesai')
        for d in queryset.values():
            obj = Konsultasi.objects.get(ID=d['ID'])
            obj.save()
    
    konsultasi_action.short_description = "Selesai konsultasi"
    
    def feedback_action(self, request, queryset):
        queryset.update(STATUS = 'Telah Mengisi Feedback')
        for d in queryset.values():
            obj = Konsultasi.objects.get(ID=d['ID'])
            obj.save()
    
    feedback_action.short_description = "Telah Mengisi Feedback"

admin.site.register(Konsultasi, KonsultasiAdmin)