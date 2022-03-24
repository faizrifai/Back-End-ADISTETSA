from csv import excel
from re import search
from django.contrib import admin
import pandas
from .models import BahanBukuUPM, PembagianTugasGuruBK, TugasPokokTendik, PembagianTugasPokokTambahanTendik

# Register your models here.
class BahanBukuUPMadmin(admin.ModelAdmin):
    list_display = ('KATEGORI', 'TAHUN_AJARAN', 'FILE', 'FILE_HASIL')
    list_per_page = 10 
    
admin.site.register(BahanBukuUPM, BahanBukuUPMadmin)

class PembagianTugasGuruBKAdmin(admin.ModelAdmin):
    search_fields = ('DATA_GURU__NAMA_LENGKAP', )
    list_display = ('DATA_GURU', 'KETERANGAN_TUGAS')
    list_per_page = 10
    filter_horizontal = ['DATA_KELAS',]
    
admin.site.register(PembagianTugasGuruBK, PembagianTugasGuruBKAdmin)

class TugasPokokTendikAdmin(admin.ModelAdmin):
    search_fields = ('JENIS_TUGAS',)
    list_display = ('JENIS_TUGAS',)
    list_per_page = 10 

admin.site.register(TugasPokokTendik, TugasPokokTendikAdmin)

class PembagianTugasPokokTambahanTendikAdmin(admin.ModelAdmin):
    search_fields = ('DATA_GURU__NAMA_LENGKAP', 'TUGAS_POKOK__JENIS_TUGAS', 'TUGAS_TAMBAHAN')
    list_display = ('DATA_GURU', 'TUGAS_POKOK','TUGAS_TAMBAHAN')
    list_per_page = 10 

admin.site.register(PembagianTugasPokokTambahanTendik, PembagianTugasPokokTambahanTendikAdmin)



