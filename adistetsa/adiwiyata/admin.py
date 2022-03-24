from django.contrib import admin

from .forms import ReuseReduceRecycleForm, SanitasiDrainaseForm

from.models import *

# Register your models here.
class SanitasiDraineseAdmin (admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'UNSUR_TERLIBAT', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'UNSUR_TERLIBAT', 'KETERANGAN', 'FILE')
    list_per_page = 10
    form = SanitasiDrainaseForm
    
admin.site.register(SanitasiDrainase, SanitasiDraineseAdmin)

class JaringanKerjaAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10
    
admin.site.register(JaringanKerja, JaringanKerjaAdmin)

class PublikasiAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'JENIS_MEDIA', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'JENIS_MEDIA', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(Publikasi, PublikasiAdmin)

class DaftarKaderAdmin(admin.ModelAdmin):
    # search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'JENIS_KEGIATAN', 'KETERANGAN')
    list_display = ('NIS',)
    # list_per_page = 10

admin.site.register(DaftarKader, DaftarKaderAdmin)

class KegiatanKaderAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(KegiatanKader, KegiatanKaderAdmin)

class KonservasiAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'KATEGORI','NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'KATEGORI','NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(Konservasi, KonservasiAdmin)

class PenanamanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PenanamanPohon, PenanamanPohonAdmin)

class PembibitanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PembibitanPohon, PembibitanPohonAdmin)

class PemeliharaanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PemeliharaanPohon, PemeliharaanPohonAdmin)

class KaryaInovatifAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_INOVATOR', 'NAMA_KARYA_INOVATIF','JENIS', 'FILE')
    list_display = ('TANGGAL', 'NAMA_INOVATOR', 'NAMA_KARYA_INOVATIF','JENIS', 'FILE')
    list_per_page = 10

admin.site.register(KaryaInovatif, KaryaInovatifAdmin) 

class PenerapanPRLHAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'PESERTA','KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'PESERTA','KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PenerapanPRLH, PenerapanPRLHAdmin)

class ReuseReduceRecycleAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN','JENIS_KEGIATAN','PIHAK_TERLIBAT', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN','JENIS_KEGIATAN','PIHAK_TERLIBAT', 'KETERANGAN', 'FILE')
    list_per_page = 10
    form = ReuseReduceRecycleForm

admin.site.register(ReuseReduceRecycle, ReuseReduceRecycleAdmin)

class PemeliharaanSampahAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PemeliharaanSampah, PemeliharaanSampahAdmin)

class TabunganSampahAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'JUMLAH_PERTANGGAL')
    list_display = ('TANGGAL', 'JUMLAH_PERTANGGAL')
    list_per_page = 10

admin.site.register(TabunganSampah, TabunganSampahAdmin)