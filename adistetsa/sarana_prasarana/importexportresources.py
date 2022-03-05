from attr import field
from django.contrib.auth.models import User, Group

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import resources

from .models import *

# class TahunAjaranForeignKeyWidget(ForeignKeyWidget):
#     def get_queryset(self, value, row):
#         return self.model.objects.filter(
#             first_name__iexact=row["TAHUN_AJARAN_AWAL"],
#             last_name__iexact=row["TAHUN_AJARAN_AKHIR"]
#         )
        
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

class SaranaResource(resources.ModelResource):
    jenis_sarana = Field(
        column_name='JENIS',
        attribute='JENIS',
        widget=ForeignKeyWidget(JenisSarana, 'KATEGORI')
    )
    class Meta:
        model = Sarana
        exclude = ('ID', 'JENIS')
        export_order=['NAMA','jenis_sarana','STATUS']

class RuanganResource(resources.ModelResource):
    jenis_ruangan = Field(
        column_name='JENIS',
        attribute='JENIS',
        widget=ForeignKeyWidget(JenisRuangan, 'KATEGORI')
    )
    
    class Meta:
        model = Ruangan
        exclude = ('ID', 'JENIS')
        export_order=['NAMA','jenis_ruangan','STATUS']
        
class RiwayatPeminjamanBarangResource(resources.ModelResource):
    alat = Field(
        column_name='ALAT',
        attribute='ALAT',
        widget=ManyToManyWidget(Sarana, field='NAMA')
    )
    
    class Meta:
        model = RiwayatPeminjamanBarang
        exclude = ('ID','USER','ALAT')
        export_order=['NAMA_PEMINJAM','NO_TELEPON','alat','KEGIATAN', 'TANGGAL_PENGGUNAAN', 'TANGGAL_PENGEMBALIAN','KETERANGAN', 'STATUS_PEMINJAMAN','TANDA_TANGAN']
        
class RiwayatPeminjamanRuanganResource(resources.ModelResource):
    ruangan = Field(
        column_name='RUANGAN',
        attribute='RUANGAN',
        widget=ForeignKeyWidget(Ruangan, 'NAMA')
    )
    
    class Meta:
        model = RiwayatPeminjamanRuangan
        exclude = ('ID','USER','RUANGAN')
        export_order=['PENGGUNA', 'NO_HP', 'KEGIATAN', 'ruangan' ,'TANGGAL_PENGAJUAN', 'TANGGAL_PEMAKAIAN','TANGGAL_BERAKHIR','JAM_PENGGUNAAN','JAM_BERAKHIR', 'JENIS_PEMINJAMAN', 'KETERANGAN','TANDA_TANGAN', 'STATUS_PEMINJAMAN',]

