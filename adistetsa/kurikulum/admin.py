from admin_auto_filters.filters import AutocompleteFilterFactory
from config_models.admin import ConfigurationModelAdmin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from import_export.admin import ImportExportModelAdmin
from kesiswaan.admin import NilaiEkskulAdmin
from subadmin import RootSubAdmin, SubAdmin
from utility.subadminexport import BaseSubAdminExport, SubAdminExportDataWithFile

from .filter_admin import *
from .forms import *
from .importexportresources import *
from .models import *

# utility function


def deskripsi_materi(obj):
    name = "%s" % obj.DESKRIPSI_MATERI
    return Truncator(name).chars(10)


def deskripsi_tata_tertib(obj):
    name = "%s" % obj.KETERANGAN
    return Truncator(name).chars(50)


class JurusanAdmin(admin.ModelAdmin):
    search_fields = [
        "NAMA",
    ]


admin.site.register(Jurusan, JurusanAdmin)


class TahunAjaranAdmin(admin.ModelAdmin):
    search_fields = ["TAHUN_AJARAN_AWAL", "TAHUN_AJARAN_AKHIR"]

    def get_ordering(self, request):
        return ["TAHUN_AJARAN_AWAL"]


admin.site.register(TahunAjaran, TahunAjaranAdmin)


class KelasAdmin(ImportExportModelAdmin):
    search_fields = [
        "KODE_KELAS",
    ]
    list_per_page = 10
    exclude = ["KODE_KELAS"]
    autocomplete_fields = ["TAHUN_AJARAN", "JURUSAN"]


admin.site.register(Kelas, KelasAdmin)


class DataSemesterAdmin(admin.ModelAdmin):
    search_fields = ["KE", "NAMA"]
    exclude = ["NAMA"]


admin.site.register(DataSemester, DataSemesterAdmin)


class MataPelajaranAdmin(ImportExportModelAdmin):
    search_fields = ["KODE", "NAMA"]

    resource_class = MataPelajaranResource


admin.site.register(MataPelajaran, MataPelajaranAdmin)


class WaktuPelajaranAdmin(ImportExportModelAdmin):
    search_fields = ["WAKTU_MULAI", "WAKTU_BERAKHIR", "JAM_KE"]

    resource_class = WaktuPelajaranResource


admin.site.register(WaktuPelajaran, WaktuPelajaranAdmin)


class NamaOfferingKelasAdmin(admin.ModelAdmin):
    search_fields = ["NAMA"]
    list_per_page = 10


admin.site.register(NamaOfferingKelas, NamaOfferingKelasAdmin)


class OfferingKelasAdmin(admin.ModelAdmin):
    search_fields = ["KELAS__KODE_KELAS"]
    list_per_page = 10
    list_filter = [
        KelasFilter,
        NamaOfferingKelasFilter,
    ]
    list_display = ["KELAS", "OFFERING"]
    ordering = ["KELAS__TINGKATAN", "-KELAS__JURUSAN__NAMA", "OFFERING"]
    autocomplete_fields = ["KELAS", "OFFERING"]


admin.site.register(OfferingKelas, OfferingKelasAdmin)


class AbsensiSiswaAdmin(BaseSubAdminExport):
    model = AbsensiSiswa
    list_display = [
        "NIS",
        "KETERANGAN",
        "FILE_KETERANGAN",
        "mata_pelajaran",
        "kelas",
        "pertemuan",
    ]
    list_per_page = 10
    readonly_fields = ["NIS", "JURNAL_BELAJAR"]
    resource_class = AbsensiSiswaResource
    autocomplete_fields = ["NIS", "JURNAL_BELAJAR"]

    def mata_pelajaran(self, obj):
        return obj.JURNAL_BELAJAR.DAFTAR.MATA_PELAJARAN

    def kelas(self, obj):
        return obj.JURNAL_BELAJAR.DAFTAR.KELAS

    def pertemuan(self, obj):
        return obj.JURNAL_BELAJAR.PERTEMUAN


class JurnalBelajarAdmin(SubAdminExportDataWithFile):
    model = JurnalBelajar
    list_display = [
        "aksi",
        "GURU",
        "PERTEMUAN",
        "TANGGAL_MENGAJAR",
        deskripsi_materi,
        "FILE_DOKUMENTASI",
        "absensi",
    ]
    list_per_page = 10
    search_fields = ["TANGGAL_MENGAJAR", "DESKRIPSI_MATERI", "FILE_DOKUMENTASI"]
    autocomplete_fields = ["GURU", "DAFTAR"]
    exclude = ["GURU"]

    resource_class = JurnalBelajarResource
    post_export_redirect_url = "admin:kurikulum_rekapjurnalbelajar_changelist"

    subadmins = [AbsensiSiswaAdmin]

    def pre_export(self, request, file_format):
        self.generate_zip(request, file_format)

    def generate_zip(self, request, file_format):
        exported_file, queryset = super().pre_export(request, file_format)

        file_to_zip = get_file_to_zip("kurikulum", queryset)
        zip_buffer = zip_file(file_to_zip)

        obj = RekapJurnalBelajar.load()
        obj.FILE_REKAP = exported_file
        obj.FILE_ZIP = ContentFile(zip_buffer.getvalue(), name="Rekap.zip")
        obj.save()

    def aksi(self, obj):
        return "Edit"

    def absensi(self, obj):
        base_url = reverse("admin:kurikulum_daftarjurnalbelajar_changelist")

        return mark_safe(
            '<a href="%s%d/jurnalbelajar/%d/absensisiswa">%s</a>'
            % (base_url, obj.DAFTAR.ID, obj.ID, "Buka Absensi")
        )


class KelasSiswaAdmin(admin.ModelAdmin):
    search_fields = ["NIS__NIS", "NIS__NAMA"]
    list_display = ["get_nis", "get_nama", "KELAS"]
    list_per_page = 10
    list_filter = [
        KelasFilter,
    ]
    autocomplete_fields = ["NIS", "KELAS"]

    def get_nis(self, obj):
        return obj.NIS.NIS

    def get_nama(self, obj):
        return obj.NIS.NAMA

    get_nis.short_description = "NIS"
    get_nama.short_description = "NAMA"


admin.site.register(KelasSiswa, KelasSiswaAdmin)


class PoinPelanggaranAdmin(ImportExportModelAdmin):
    search_fields = [
        "KETERANGAN",
        "POIN",
    ]
    list_display = [
        deskripsi_tata_tertib,
        "POIN",
    ]
    list_per_page = 10

    resource_class = PoinPelanggaranResource


admin.site.register(PoinPelanggaran, PoinPelanggaranAdmin)


class JadwalMengajarAdmin(ImportExportModelAdmin):
    search_fields = [
        "GURU__NAMA_LENGKAP",
        "TAHUN_AJARAN__TAHUN_AJARAN_AWAL",
        "TAHUN_AJARAN__TAHUN_AJARAN_AKHIR",
        "SEMESTER__KE",
        "KELAS__OFFERING__NAMA",
        "MATA_PELAJARAN__NAMA",
    ]
    list_per_page = 10
    filter_horizontal = ["WAKTU_PELAJARAN"]
    exclude = ["JUMLAH_WAKTU"]
    list_display = [
        "GURU",
        "TAHUN_AJARAN",
        "SEMESTER",
        "KELAS",
        "MATA_PELAJARAN",
        "HARI",
        "jam_pelajaran",
        "jumlah_waktu",
    ]
    list_filter = [
        TahunFilter,
        SemesterFilter,
        "HARI",
        KelasFilter,
        MataPelajaranFilter,
        WaktuPelajaranFilter,
        GuruFilter,
    ]
    form = JadwalMengajarForm
    autocomplete_fields = [
        "GURU",
        "TAHUN_AJARAN",
        "SEMESTER",
        "KELAS",
        "MATA_PELAJARAN",
    ]

    resource_class = JadwalMengajarResource

    def jumlah_waktu(self, obj):
        jumlah_waktu = obj.WAKTU_PELAJARAN.all().count()

        return str(jumlah_waktu)

    def jam_pelajaran(self, obj):
        daftar = ""
        for data in obj.WAKTU_PELAJARAN.all():
            daftar += str(data) + "<br>"

        return format_html(daftar)


admin.site.register(JadwalMengajar, JadwalMengajarAdmin)


class DaftarJurnalBelajarAdmin(RootSubAdmin):
    search_fields = [
        "MATA_PELAJARAN__NAMA",
        "GURU__NAMA_LENGKAP",
        "KELAS__KELAS__KODE_KELAS",
        "KELAS__OFFERING__NAMA",
    ]
    list_per_page = 10
    list_display = [
        "aksi",
        "GURU",
        "SEMESTER",
        "hari",
        "KELAS",
        "MATA_PELAJARAN",
        "jurnal_belajar",
    ]
    list_filter = [SemesterFilter, KelasFilter, MataPelajaranFilter, GuruFilter]
    autocomplete_fields = ["GURU", "MATA_PELAJARAN", "KELAS", "SEMESTER"]

    subadmins = [JurnalBelajarAdmin]

    def aksi(self, obj):
        return "Edit"

    def jurnal_belajar(self, obj):
        base_url = reverse("admin:kurikulum_daftarjurnalbelajar_changelist")

        return mark_safe(
            '<a href="%s%d/jurnalbelajar">%s</a>' % (base_url, obj.ID, "Buka Jurnal")
        )

    def hari(self, obj):
        data = JadwalMengajar.objects.filter(
            GURU=obj.GURU,
            MATA_PELAJARAN=obj.MATA_PELAJARAN,
            KELAS=obj.KELAS,
            SEMESTER=obj.SEMESTER,
        ).order_by("-HARI")

        hari = []
        for d in data:
            temp = []
            output_waktu = "Jam ke-"
            for waktu in d.WAKTU_PELAJARAN.all():
                temp.append(str(waktu.JAM_KE))
            waktu = ", ".join(temp)
            hari.append(d.HARI + " " + f"({output_waktu}{waktu})")

        output_hari = "<br>".join(hari)

        return format_html(output_hari)


admin.site.register(DaftarJurnalBelajar, DaftarJurnalBelajarAdmin)


class NilaiRaportAdmin(SubAdmin):
    model = NilaiRaport
    search_fields = [
        "MATA_PELAJARAN",
        "BEBAN",
        "NILAI_PENGETAHUAN",
        "NILAI_KETERAMPILAN",
        "DESKRIPSI_PENGETAHUAN",
        "DESKRIPSI_KETERAMPILAN",
    ]
    list_display = [
        "RAPORT",
        "MATA_PELAJARAN",
        "BEBAN",
        "NILAI_PENGETAHUAN",
        "NILAI_KETERAMPILAN",
        "DESKRIPSI_PENGETAHUAN",
        "DESKRIPSI_KETERAMPILAN",
    ]
    list_per_page = 10
    exclude = ["RAPORT"]
    ordering = [
        "-RAPORT",
    ]
    autocomplete_fields = ["RAPORT", "MATA_PELAJARAN"]


class RaportAdmin(SubAdmin):
    model = Raport
    search_fields = ["KELAS_SISWA"]
    list_display = ["KELAS_SISWA", "SEMESTER", "aksi_nilai_raport", "aksi_nilai_ekskul"]
    list_per_page = 10
    subadmins = [NilaiRaportAdmin, NilaiEkskulAdmin]
    exclude = ["KELAS_SISWA"]
    ordering = ["KELAS_SISWA", "SEMESTER"]
    autocomplete_fields = ["KELAS_SISWA", "SEMESTER", "BUKU_INDUK"]

    def aksi_nilai_raport(self, obj):
        base_url = reverse("admin:tata_usaha_bukuinduk_changelist")

        return mark_safe(
            '<a href="%s%d/raport/%d/nilairaport">%s</a>'
            % (base_url, obj.BUKU_INDUK.ID, obj.ID, "Buka Raport")
        )

    def aksi_nilai_ekskul(self, obj):
        base_url = reverse("admin:tata_usaha_bukuinduk_changelist")

        return mark_safe(
            '<a href="%s%d/raport/%d/nilaiekskul">%s</a>'
            % (base_url, obj.BUKU_INDUK.ID, obj.ID, "Buka Nilai Ekskul")
        )


class RaportKurikulumAdmin(RootSubAdmin):
    search_fields = ["KELAS_SISWA"]
    list_display = ["KELAS_SISWA", "SEMESTER", "tahun_ajaran", "aksi_nilai_raport"]
    list_filter = [
        SemesterFilter,
        AutocompleteFilterFactory(
            "TAHUN AJARAN", "KELAS_SISWA__KELAS__KELAS__TAHUN_AJARAN"
        ),
        AutocompleteFilterFactory("KELAS", "KELAS_SISWA__KELAS"),
        AutocompleteFilterFactory("SISWA", "KELAS_SISWA__NIS"),
    ]
    list_per_page = 10
    subadmins = [NilaiRaportAdmin]
    exclude = ["KELAS_SISWA"]
    ordering = ["KELAS_SISWA", "SEMESTER"]
    autocomplete_fields = ["KELAS_SISWA", "SEMESTER"]

    def tahun_ajaran(self, obj):
        return str(obj.KELAS_SISWA.KELAS.KELAS.TAHUN_AJARAN)

    def aksi_nilai_raport(self, obj):
        base_url = reverse("admin:kurikulum_raport_changelist")

        return mark_safe(
            '<a href="%s%d/nilairaport">%s</a>' % (base_url, obj.ID, "Buka Raport")
        )


admin.site.register(Raport, RaportKurikulumAdmin)

admin.site.register(Configuration, ConfigurationModelAdmin)


class RekapJurnalBelajarAdmin(admin.ModelAdmin):
    list_display = ["FILE_REKAP", "FILE_ZIP"]


admin.site.register(RekapJurnalBelajar, RekapJurnalBelajarAdmin)


# DRAFT

# class KTSPAdmin(admin.ModelAdmin):
#     list_display = ['TAHUN_AJARAN', 'NAMA_FILE']
#     list_per_page = 10
#     search_fields = ['TAHUN_AJARAN__TAHUN_AJARAN_AWAL',
#                      'TAHUN_AJARAN__TAHUN_AJARAN_AKHIR']
#     list_filter = [TahunFilter,]
#     autocomplete_fields = ['TAHUN_AJARAN']


# admin.site.register(KTSP, KTSPAdmin)


# class JadwalPekanAktifAdmin(admin.ModelAdmin):
#     filter_horizontal = ['MINGGU_TIDAK_EFEKTIF', 'MINGGU_EFEKTIF', ]
#     list_display = ['aksi', 'bulan_efektif', 'jumlah_minggu', 'jumlah_minggu_efektif',
#                     'jumlah_minggu_tidak_efektif', 'uraian_kegiatan',  'MATA_PELAJARAN', 'KELAS', 'SEMESTER']
#     list_filter = [SemesterFilter, KelasFilter, MataPelajaranFilter]
#     autocomplete_fields = ['MATA_PELAJARAN', 'KELAS', 'SEMESTER']

#     def uraian_kegiatan(self, obj):
#         daftar = ""
#         for data in obj.MINGGU_TIDAK_EFEKTIF.all():
#             kegiatan = str(data.URAIAN_KEGIATAN)
#             daftar += Truncator(kegiatan).chars(10) + "<br>"

#         return format_html(daftar)

#     def bulan_efektif(self, obj):
#         daftar = ""
#         for data in obj.MINGGU_EFEKTIF.all():
#             daftar += str(data.BULAN) + "<br>"
#         return format_html(daftar)

#     def jumlah_minggu(self, obj):
#         daftar = ""
#         for data in obj.MINGGU_EFEKTIF.all():
#             daftar += str(data.JUMLAH_MINGGU) + "<br>"
#         return format_html(daftar)

#     def jumlah_minggu_efektif(self, obj):
#         daftar = ""
#         for data in obj.MINGGU_EFEKTIF.all():
#             daftar += str(data.JUMLAH_MINGGU_EFEKTIF) + "<br>"
#         return format_html(daftar)

#     def jumlah_minggu_tidak_efektif(self, obj):
#         daftar = ""
#         for data in obj.MINGGU_EFEKTIF.all():
#             daftar += str(data.JUMLAH_MINGGU_TIDAK_EFEKTIF) + "<br>"
#         return format_html(daftar)

#     def aksi(self, obj):
#         return "Detail"


# admin.site.register(JadwalPekanAktif, JadwalPekanAktifAdmin)


# class JadwalPekanEfektifSemesterAdmin(admin.ModelAdmin):
#     list_display = ['BULAN', 'JUMLAH_MINGGU', 'JUMLAH_MINGGU_EFEKTIF',
#                     'JUMLAH_MINGGU_TIDAK_EFEKTIF', 'KETERANGAN']


# admin.site.register(JadwalPekanEfektifSemester,
#                     JadwalPekanEfektifSemesterAdmin)


# class JadwalPekanTidakEfektifAdmin(admin.ModelAdmin):
#     list_display = ['URAIAN_KEGIATAN', 'JUMLAH_MINGGU', 'KETERANGAN']


# admin.site.register(JadwalPekanTidakEfektif, JadwalPekanTidakEfektifAdmin)


# class SilabusRPBAdmin(admin.ModelAdmin):
#     list_display = ['MATA_PELAJARAN', 'TAHUN_AJARAN', 'NAMA_FILE', 'KELAS']
#     list_per_page = 10
#     search_fields = ['MATA_PELAJARAN__NAMA',
#                      'KELAS__KODE_KELAS', 'SEMESTER__NAMA']
#     list_filter = [TahunFilter, MataPelajaranFilter,
#                    KelasFilter, SemesterFilter]
#     autocomplete_fields = ['MATA_PELAJARAN',
#                            'TAHUN_AJARAN', 'KELAS', 'SEMESTER']


# admin.site.register(SilabusRPB, SilabusRPBAdmin)
