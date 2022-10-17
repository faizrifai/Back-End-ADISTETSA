from csv import excel
from re import search
from django.contrib import admin
import pandas
from .models import (
    BahanBukuUPM,
    JenisBidang,
    PembagianTugasGuruBK,
    TugasPokokTendik,
    PembagianTugasPokokTambahanTendik,
    PembagianTugasGuruTIK,
    RincianTugasPokokTambahanTendik,
    TugasTambahanKepanitiaanTendik,
)


# Register your models here.
class BahanBukuUPMadmin(admin.ModelAdmin):
    list_display = (
        "KATEGORI",
        "TAHUN_AJARAN",
        "FILE",
    )
    list_per_page = 10
    list_filter = ("TAHUN_AJARAN", "SEMESTER", "KATEGORI")


admin.site.register(BahanBukuUPM, BahanBukuUPMadmin)


class PembagianTugasGuruBKAdmin(admin.ModelAdmin):
    search_fields = ("DATA_GURU__NAMA_LENGKAP",)
    list_display = ("DATA_GURU", "KETERANGAN_TUGAS")
    list_per_page = 10
    filter_horizontal = [
        "DATA_KELAS",
    ]
    autocomplete_fields = ["DATA_GURU", "TAHUN_AJARAN"]
    list_filter = ("TAHUN_AJARAN", "SEMESTER")


admin.site.register(PembagianTugasGuruBK, PembagianTugasGuruBKAdmin)


class PembagianTugasGuruTIKAdmin(admin.ModelAdmin):
    search_fields = ("DATA_GURU__NAMA_LENGKAP",)
    list_display = ("DATA_GURU", "KETERANGAN_TUGAS")
    list_per_page = 10
    filter_horizontal = [
        "DATA_KELAS",
    ]
    autocomplete_fields = ["DATA_GURU", "TAHUN_AJARAN"]
    list_filter = ["TAHUN_AJARAN", "SEMESTER"]


admin.site.register(PembagianTugasGuruTIK, PembagianTugasGuruTIKAdmin)


class TugasPokokTendikAdmin(admin.ModelAdmin):
    search_fields = ("JENIS_TUGAS",)
    list_display = ("JENIS_TUGAS",)
    list_per_page = 10


admin.site.register(TugasPokokTendik, TugasPokokTendikAdmin)


class PembagianTugasPokokTambahanTendikAdmin(admin.ModelAdmin):
    search_fields = (
        "DATA_GURU__NAMA_LENGKAP",
        "TUGAS_POKOK__JENIS_TUGAS",
        "TUGAS_TAMBAHAN",
    )
    list_display = ("DATA_GURU", "TUGAS_POKOK", "TUGAS_TAMBAHAN")
    list_per_page = 10
    autocomplete_fields = ["DATA_GURU", "TUGAS_POKOK", "TAHUN_AJARAN"]
    list_filter = [
        "TAHUN_AJARAN",
    ]


admin.site.register(
    PembagianTugasPokokTambahanTendik, PembagianTugasPokokTambahanTendikAdmin
)


class RincianTugasPokokTambahanTendikAdmin(admin.ModelAdmin):
    search_fields = ("DATA_GURU__NAMA_LENGKAP", "TUGAS_POKOK", "TUGAS_TAMBAHAN")
    list_display = ("DATA_GURU", "TUGAS_POKOK", "TUGAS_TAMBAHAN")
    list_per_page = 10
    autocomplete_fields = ["DATA_GURU", "TAHUN_AJARAN"]
    list_filter = [
        "TAHUN_AJARAN",
    ]


admin.site.register(
    RincianTugasPokokTambahanTendik, RincianTugasPokokTambahanTendikAdmin
)


class JenisBidangAdmin(admin.ModelAdmin):
    search_fields = ("KODE_BIDANG", "NAMA_BIDANG")
    list_display = ("KODE_BIDANG", "NAMA_BIDANG")
    list_per_page = 10


admin.site.register(JenisBidang, JenisBidangAdmin)


class TugasTambahanKepanitiaanTendikAdmin(admin.ModelAdmin):
    search_fields = ("DATA_GURU__NAMA_LENGKAP", "BIDANG__NAMA_BIDANG", "TUGAS")
    list_display = ("DATA_GURU", "kode_bidang", "BIDANG", "TUGAS")
    list_per_page = 10
    ordering = ("BIDANG__KODE_BIDANG",)
    autocomplete_fields = ["DATA_GURU", "BIDANG", "TAHUN_AJARAN"]
    list_filter = [
        "TAHUN_AJARAN",
    ]

    def kode_bidang(self, obj):
        kode = obj.BIDANG.KODE_BIDANG
        return kode


admin.site.register(TugasTambahanKepanitiaanTendik, TugasTambahanKepanitiaanTendikAdmin)
