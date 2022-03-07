from csv import excel
from pyexpat import model
from wsgiref.validate import validator
from attr import field
from django.contrib.auth.models import User, Group
from django.forms import CharField

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, CharWidget, ManyToManyWidget
from import_export import resources

from adistetsa.custom_function import cek_error_import

from .models import *

class TahunAjaranForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row):
        return self.model.objects.filter(
            first_name__iexact=row["TAHUN_AJARAN_AWAL"],
            last_name__iexact=row["TAHUN_AJARAN_AKHIR"]
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

class KatalogEkskulResource(resources.ModelResource):

    class Meta:
        model = KatalogEkskul
        exclude = ('ID',)
        import_id_fields = ('NAMA',)

class KategoriProgramKebaikanResource(resources.ModelResource):

    class Meta:
        model = KategoriProgramKebaikan
        exclude = ('ID',)
        import_id_fields = ('NAMA',)
        
class NilaiEkskulResource(resources.ModelResource):
    data_anggota = Field(
        column_name='DATA_ANGGOTA',
        attribute='DATA_ANGGOTA',
        widget=ForeignKeyWidget(NilaiEkskul, 'KODE_PENDANAAN')
    )
    
    
    
    class Meta:
        model = NilaiEkskul
        exclude = ('ID',)
        import_id_fields = ('data_anggota',)
        

class AnggotaEkskulResource(resources.ModelResource):
    kelas_siswa = Field(
        column_name= 'KELAS_SISWA',
        attribute= 'KELAS_SISWA',
        widget= CharWidget()
    )
    
    tahun_ajaran = Field(
        column_name='TAHUN_AJARAN',
        attribute='TAHUN_AJARAN',
        widget=CharWidget()
    )
    ekskul = Field(
        column_name='EKSKUL',
        attribute='EKSKUL',
        widget=ForeignKeyWidget(KatalogEkskul, 'NAMA')
    )
    class Meta:
        model = AnggotaEkskul
        fields = ('kelas_siswa', 'tahun_ajaran', 'eksul')
        exclude = ('ID',)

class JurnalEkskulResource(resources.ModelResource):
    
    daftar = Field(
        column_name='DAFTAR',
        attribute='DAFTAR',
        widget=CharWidget()
    )
    
    pelatih = Field(
        column_name='PELATIH',
        attribute='PELATIH',
        widget=ForeignKeyWidget(DataPelatih, 'NAMA')
    )
    
    class Meta:
        model = JurnalEkskul
        fields = ('pelatih', 'PERTEMUAN', 'TANGGAL_MELATIH', 'DESKRIPSI', 'FILE_DOKUMENTASI', 'daftar')
        exclude = ('ID',)
        
class JadwalEkskulResource(resources.ModelResource):
    pelatih = Field(
        column_name='PELATIH',
        attribute='PELATIH',
        widget=ForeignKeyWidget(DataPelatih, 'NAMA')
    )
    
    tahun_ajaran = Field(
        column_name='TAHUN_AJARAN',
        attribute='TAHUN_AJARAN',
        widget=CharWidget()
    )
    
    semester = Field(
        column_name='SEMESTER',
        attribute='SEMESTER',
        widget=ForeignKeyWidget(DataSemester, 'KE')
    )
    
    ekskul = Field(
        column_name='EKSKUL',
        attribute='EKSKUL',
        widget=ForeignKeyWidget(KatalogEkskul, 'NAMA')
    )
    
    def before_import_row(self, row, **kwargs):
        tahun_ajaran = row['TAHUN_AJARAN'].split('/')
        try:
            tahun_ajaran_aktif = TahunAjaran.objects.get(TAHUN_AJARAN_AWAL=tahun_ajaran[0], TAHUN_AJARAN_AKHIR=tahun_ajaran[1])
            row['TAHUN_AJARAN'] = tahun_ajaran_aktif
        except Exception as e:
            raise ValidationError({'TAHUN_AJARAN' : 'Data tahun masih belum ada'})
            # raise ValidationError(str(e))
        
    
    class Meta:
        model = JadwalEkskul
        fields = ('HARI', 'WAKTU_MULAI', 'WAKTU_BERAKHIR')
        exclude = ('ID',)
        import_id_fields = ('pelatih', 'HARI', 'tahun_ajaran', 'WAKTU_MULAI', 'WAKTU_BERAKHIR')

class PelanggaranSiswaResource(resources.ModelResource):
    data_siswa = Field(
        column_name='DATA_SISWA',
        attribute='DATA_SISWA',
        widget=CharWidget()
    )
    
    class Meta:
        model = PelanggaranSiswa 
        fields = ('data_siswa', 'POIN')
        exclude = ('ID', )
        import_id_fields = ('ID',)
        
class PoinProgramKebaikanResource(resources.ModelResource):
    class Meta:
        model = PoinProgramKebaikan
        fields = ('KETERANGAN', 'POIN')
        exclude = ('ID',)
        import_id_fields = ('KETERANGAN',)

class RiwayatLaporanPelanggaranResource(resources.ModelResource):
    data_siswa = Field(
        column_name='DATA_SISWA',
        attribute='DATA_SISWA',
        widget=CharWidget()
    )
    
    jenis_pelanggaran = Field(
        column_name='JENIS_PELANGGARAN',
        attribute='JENIS_PELANGGARAN', 
        widget=ForeignKeyWidget(PoinPelanggaran, 'KETERANGAN')
    )
    
    
    class Meta:
        model = RiwayatLaporanPelanggaran
        fields =  ('data_siswa', 'jenis_pelanggaran', 'TANGGAL_PENGAJUAN', 'BUKTI_PELANGGARAN', 'STATUS_PENGAJUAN')
        exclude = ('ID',)

class RiwayatProgramKebaikanResource(resources.ModelResource):
    data_siswa = Field(
        column_name='DATA_SISWA',
        attribute='DATA_SISWA',
        widget=CharWidget()
    )
    
    jenis_program_kebaikan = Field(
        column_name='JENIS_PROGRAM_KEBAIKAN',
        attribute='JENIS_PROGRAM_KEBAIKAN', 
        widget=ForeignKeyWidget(PoinProgramKebaikan, 'KETERANGAN')
    )
    
    
    class Meta:
        model = RiwayatProgramKebaikan
        fields =  ('data_siswa', 'jenis_program_kebaikan', 'TANGGAL_PENGAJUAN', 'BUKTI_PROGRAM_KEBAIKAN', 'STATUS_PENGAJUAN')
        exclude = ('ID',)

