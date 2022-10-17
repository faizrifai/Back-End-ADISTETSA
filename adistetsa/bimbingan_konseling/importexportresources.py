from django.contrib.auth.models import User

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources


from .models import *


class TahunAjaranForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row):
        return self.model.objects.filter(
            first_name__iexact=row["TAHUN_AJARAN_AWAL"],
            last_name__iexact=row["TAHUN_AJARAN_AKHIR"],
        )


# # class AnggotaEkskulResource(resources.ModelResource):


# #     tahun_ajaran = Field(
# #         column_name='TAHUN_AJARAN',
# #         attribute='TAHUN_AJARAN',
# #         widget=ForeignKeyWidget(TipeMedia, 'KODE_MEDIA')
# #     )

# #     kode_tipe = Field(
# #         column_name='KODE_TIPE',
# #         attribute='KODE_TIPE',
# #         widget=ForeignKeyWidget(TipeBuku, 'KODE_TIPE')
# #     )

# #     kode_lokasi = Field(
# #         column_name='KODE_LOKASI',
# #         attribute='KODE_LOKASI',
# #         widget=ForeignKeyWidget(Lokasi, 'KODE_LOKASI')
# #     )

# #     lokasi_spesifik = Field(
# #         column_name='LOKASI_SPESIFIK',
# #         attribute='LOKASI_SPESIFIK',
# #         widget=ForeignKeyWidget(LokasiSpesifik, 'LOKASI_SPESIFIK')
# #     )

# #     class Meta:
# #         model = KatalogBuku
# #         fields = ('REGISTER','ISBN','JUDUL','VOLUME','EDISI','BAHASA','kode_media','kode_tipe','NOMER_DEWEY','KODE_AUTHOR','KODE_JUDUL','TAHUN_TERBIT','KOTA_PENERBIT','PENERBIT','DESKRIPSI_FISIK','INDEX','BIBLIOGRAPHY','kode_lokasi','lokasi_spesifik','HARGA','DATA_ENTRY','OPERATOR_CODE')
# #         import_id_fields = ('REGISTER',)
# #         export_order = ['REGISTER','ISBN','JUDUL','VOLUME','EDISI','BAHASA','kode_media','kode_tipe','NOMER_DEWEY','KODE_AUTHOR','KODE_JUDUL','TAHUN_TERBIT','KOTA_PENERBIT','PENERBIT','DESKRIPSI_FISIK','INDEX','BIBLIOGRAPHY','kode_lokasi','lokasi_spesifik','HARGA','DATA_ENTRY','OPERATOR_CODE']

# class DonasiBukuResource(resources.ModelResource):

#     kode_donasi = Field(
#         column_name='KODE_DONASI',
#         attribute='KODE_DONASI',
#         widget=ForeignKeyWidget(Pendanaan, 'KODE_PENDANAAN')
#     )

#     def before_import_row(self, row, **kwargs):
#         tanggal_penerimaan = datetime.datetime.fromisoformat(row['TANGGAL_PENERIMAAN']).astimezone(datetime.timezone.utc)
#         data_entry = datetime.datetime.fromisoformat(row['DATA_ENTRY']).astimezone(datetime.timezone.utc)

#         row['TANGGAL_PENERIMAAN'] = tanggal_penerimaan
#         row['DATA_ENTRY'] = data_entry

#     class Meta:
#         model = DonasiBuku
#         fields = ('REGISTER_DONASI', 'DUPLIKAT', 'KODE_DONASI','TANGGAL_PENERIMAAN','CATATAN_DONASI')
#         import_id_fields = ('id',)
#         export_order = ['REGISTER_DONASI', 'DUPLIKAT', 'KODE_DONASI','TANGGAL_PENERIMAAN','CATATAN_DONASI']


class DataAlumniResource(resources.ModelResource):
    class Meta:
        model = DataAlumni
        exclude = "ID"
        import_id_fields = ("NAMA_SISWA",)


class PeminatanLintasMinatResource(resources.ModelResource):
    # kelas_siswa = Field(
    #     column_name='KELAS_SISWA',
    #     attribute='KELAS_SISWA',
    #     widget=ForeignKeyWidget(KelasSiswa,)
    # )

    class Meta:
        model = PeminatanLintasMinat
        exclude = "ID"
        import_id_fields = ("KELAS_SISWA",)


class KatalogKonselorResource(resources.ModelResource):
    user = Field(
        column_name="USER", attribute="USER", widget=ForeignKeyWidget(User, "username")
    )

    class Meta:
        model = KatalogKonselor
        fields = ("KOMPETENSI", "ALUMNUS", "CONFERENCE", "WHATSAPP")
        exclude = ("ID", "STATUS")
        import_id_fields = ("KOMPETENSI",)


class KonsultasiResource(resources.ModelResource):
    user = Field(
        column_name="USER", attribute="USER", widget=ForeignKeyWidget(User, "username")
    )

    konselor = Field(
        column_name="KONSELOR",
        attribute="KONSELOR",
        widget=ForeignKeyWidget(KatalogKonselor, "NAMA"),
    )

    class Meta:
        model = Konsultasi
        fields = (
            "TANGGAL_KONSULTASI",
            "JAM_AWAL",
            "JAM_AKHIR",
            "JENIS_MASALAH",
            "RATING",
            "STATUS",
            "KRITIK_SARAN",
        )
        exclude = ("ID",)
