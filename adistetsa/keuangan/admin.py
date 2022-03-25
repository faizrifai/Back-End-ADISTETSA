from re import search
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin, ExportMixin
from keuangan.filter_admin import JenisPembayaranFilter
from kurikulum.filter_admin import KelasFilter
from .forms import PembayaranForm

from kesiswaan.filter_admin import DataSiswaFilter
# from .filter_admin import *
from .models import *

class PembayaranAdmin(admin.ModelAdmin):
    search_fields = ('NAMA_SISWA__NIS__NAMA', 'NAMA_SISWA__NIS__NIS', 'NAMA_SISWA__KELAS__KELAS__KODE_KELAS','NAMA_SISWA__KELAS__OFFERING__NAMA', 'JENIS_PEMBAYARAN__JENIS_PEMBAYARAN',)
    list_display = ('NAMA_SISWA','nis', 'JENIS_PEMBAYARAN','PEMBAYARAN_BULAN', 'KUITANSI')
    list_per_page = 10
    # autocomplete_fields = ('NAMA_SISWA', 'JENIS_PEMBAYARAN',)
    # list_filter = (JenisPembayaranFilter,)
    form = PembayaranForm

    def nis(self, obj):
        return obj.NAMA_SISWA.NIS.NIS
    

admin.site.register(Pembayaran, PembayaranAdmin)
    
    