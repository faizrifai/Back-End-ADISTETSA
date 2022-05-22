from import_export import resources
from import_export.fields import Field
from import_export.widgets import (CharWidget, ForeignKeyWidget,
                                   ManyToManyWidget)

from .models import *

# Register your import_export resource model here


class TataTertibResource(resources.ModelResource):
    kategori = Field(
        column_name='KATEGORI',
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
        widget=ForeignKeyWidget(apps.get_model(
            'dataprofil', 'DataGuru'), 'NAMA_LENGKAP')
    )

    class Meta:
        model = JurnalBelajar
        fields = ('PERTEMUAN', 'PERTEMUAN', 'TANGGAL_MENGAJAR',
                  'DESKRIPSI_MATERI', 'FILE_DOKUMENTASI')
        exclude = ('ID',)
        import_id_fields = ('PERTEMUAN',)


class AbsensiSiswaResource(resources.ModelResource):
    nama = Field(
        column_name='NIS',
        attribute='NIS',
        widget=ForeignKeyWidget(apps.get_model(
            'dataprofil', 'DataSiswa'), 'NAMA')
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
        widget=ForeignKeyWidget(apps.get_model(
            'dataprofil', 'DataGuru'), 'NAMA_LENGKAP')
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
        waktu_pelajaran = row['WAKTU_PELAJARAN'].split(',')

        v_kelas = self.kelas_valid(row, kelas)
        v_guru = cek_error_import(apps.get_model(
            'kurikulum', 'DataGuru'), row, 'GURU', 'NAMA_LENGKAP')
        v_mapel = cek_error_import(
            MataPelajaran, row, 'MATA_PELAJARAN', 'NAMA')
        v_semester = cek_error_import(DataSemester, row, 'SEMESTER', 'KE')
        v_waktu_pelajaran = self.jadwal_valid(waktu_pelajaran, row)

        validator = gabung_dictionary(
            v_guru, v_mapel, v_semester, v_kelas, v_waktu_pelajaran)

        if validator:
            raise ValidationError(validator)

    def jadwal_valid(self, waktu_pelajaran, row):
        jadwal = JadwalMengajar.objects.filter(
            GURU__NAMA_LENGKAP=row['GURU'], HARI=row['HARI'])

        for waktu in waktu_pelajaran:
            for data in jadwal:
                for waktu_lama in data.WAKTU_PELAJARAN.all():
                    if int(waktu) == waktu_lama.JAM_KE:
                        v_waktu_pelajaran = {
                            'WAKTU_PELAJARAN': 'Jadwal mengajar bentrok'}
                        break

        return v_waktu_pelajaran

    def kelas_valid(self, row, kelas):
        try:
            offering_kelas = OfferingKelas.objects.get(
                KELAS__KODE_KELAS=kelas[0] + ' ' + kelas[1], OFFERING__NAMA=kelas[2])
            row['KELAS'] = offering_kelas
        except OfferingKelas.DoesNotExist:
            v_kelas = {'KELAS': 'Data kelas masih belum ada'}
            
        return v_kelas

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
