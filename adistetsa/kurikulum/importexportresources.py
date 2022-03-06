from ast import mod
from pyexpat import model
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, CharWidget, ManyToManyWidget
from import_export import resources
from import_export.results import NON_FIELD_ERRORS

from .models import *

# Register your import_export resource model here
class TataTertibResource(resources.ModelResource):
    kategori = Field(
        column_name= 'KATEGORI',
        attribute='KATEGORI',
        widget=ForeignKeyWidget(KategoriTataTertib, 'NAMA')
    )
    
    class Meta:
        model = TataTertib
        fields = ('KETERANGAN', 'kategori')
        exclude = ('ID',)
        import_id_fields = ('KETERANGAN',)

class PoinPelanggaranResource(resources.ModelResource):

    class Meta:
        model = PoinPelanggaran
        fields = ('KETERANGAN', 'POIN')
        exclude = ('ID',)
        import_id_fields = ('KETERANGAN',)

class MataPelajaranResource(resources.ModelResource):
    
    class Meta:
        model = MataPelajaran
        fields = ('KODE', 'NAMA')
        exclude = ('ID',)
        import_id_fields = ('KODE',)
        
class KategoriTataTertibResource(resources.ModelResource):
    
    class Meta:
        model = KategoriTataTertib
        fields = ('NAMA',)
        exclude = ('ID',)
        import_id_fields = ('NAMA',)

class JurnalBelajarResource(resources.ModelResource):
    guru = Field(
        column_name='GURU',
        attribute='GURU',
        widget=ForeignKeyWidget(DataGuru, 'NAMA_LENGKAP')
    )
    
    class Meta:
        model = JurnalBelajar
        fields = ('PERTEMUAN', 'PERTEMUAN', 'TANGGAL_MENGAJAR', 'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI')
        exclude = ('ID',)
        import_id_fields = ('PERTEMUAN',)

class AbsensiSiswaResource(resources.ModelResource):
    nama = Field(
        column_name='NIS',
        attribute='NIS',
        widget=ForeignKeyWidget(DataSiswa, 'NAMA')
    )
    
    class Meta:
        model = AbsensiSiswa
        exclude = ('ID',)
        
class TahunAjaranForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row):
        tahun_ajaran = row["TAHUN_AJARAN"].split('/')
        return TahunAjaran.objects.filter(
            TAHUN_AJARAN__TAHUN_AJARAN_AWAL__iexact=int(tahun_ajaran[0]),
            TAHUN_AJARAN__TAHUN_AJARAN_AKHIR__iexact=int(tahun_ajaran[1])
        )

class JadwalMengajarResource(resources.ModelResource):
    guru = Field(
        column_name='GURU',
        attribute='GURU',
        widget=ForeignKeyWidget(DataGuru, 'NAMA_LENGKAP')
    )
    
    kelas = Field(
        column_name='KELAS',
        attribute='KELAS',
        widget=CharWidget()
    )
    
    mata_pelajaran = Field(
        column_name='MATA_PELAJARAN',
        attribute='MATA_PELAJARAN',
        widget=ForeignKeyWidget(MataPelajaran, 'NAMA')
    )
    
    
    def before_import_row(self, row, **kwargs):
        kelas = row['KELAS'].split(' ')
        try:
            offering_kelas = OfferingKelas.objects.get(KELAS__KODE_KELAS=kelas[0] + ' ' + kelas[1], OFFERING__NAMA=kelas[2])
            row['KELAS'] = offering_kelas
        except Exception as e:
            raise ValidationError({'KELAS' : 'Data kelas masih belum ada'})
        
        # try:
        #     tes = MataPelajaran.objects.get(NAMA=row['MATA_PELAJARAN'])
        # except Exception as e:
        #     raise ValidationError('Tes')
        
        v_mapel = cek_error_import(MataPelajaran, row, 'MATA_PELAJARAN', 'NAMA')
        v_semester = cek_error_import(DataSemester, row, 'SEMESTER', 'KE')
        validator = gabung_dictionary(v_mapel, v_semester)
        
        if validator:
            raise ValidationError(validator)
    
    semester = Field(
        column_name='SEMESTER',
        attribute='SEMESTER',
        widget=ForeignKeyWidget(DataSemester, 'KE')
    )
    
    waktu_pelajaran = Field(
        column_name='WAKTU_PELAJARAN',
        attribute='WAKTU_PELAJARAN',
        widget=ManyToManyWidget(WaktuPelajaran, field='JAM_KE')
    )
    
    
    class Meta:
        model = JadwalMengajar
        fields = ('HARI',)
        exclude = ('ID',)
        import_id_fields = ('kelas', 'mata_pelajaran', 'HARI')

