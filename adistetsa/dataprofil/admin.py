from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DataSiswa)
admin.site.register(DataAnakPegawai)
admin.site.register(DataBeasiswaPegawai)
admin.site.register(DataBukuPegawai)
admin.site.register(DataDiklatPegawai)
admin.site.register(DataKaryaTulisPegawai)
admin.site.register(DataKesejahteraanPegawai)
admin.site.register(DataKompetensiPegawai)
admin.site.register(DataNilaiTesPegawai)
admin.site.register(DataPenghargaanPegawai)
admin.site.register(DataRiwayatGajiBerkalaPegawai)
admin.site.register(DataRiwayatJabatanFungsionalPegawai)
admin.site.register(DataRiwayatJabatanStrukturalPegawai)
admin.site.register(DataRiwayatKarirGuruPegawai)
admin.site.register(DataRiwayatKepangkatanPegawai)
admin.site.register(DataRiwayatPendidikanFormalPegawai)
admin.site.register(DataRiwayatSertifikasiPegawai)
admin.site.register(DataTugasTambahanPegawai)
admin.site.register(DataTunjanganPegawai)

class DataOrangTuaAdmin(admin.ModelAdmin):
    filter_horizontal = ('DATA_ANAK',)

admin.site.register(DataOrangTua, DataOrangTuaAdmin)


class kompetensi_pegawai_inline(admin.TabularInline):
    model = DataPegawai.DATA_KOMPETENSI_PEGAWAI.through
    extra = 1
    verbose_name = 'Kompetensi Pegawai'
    verbose_name_plural = 'Daftar Kompetensi Pegawai'

class anak_pegawai_inline(admin.TabularInline):
    model = DataPegawai.DATA_ANAK_PEGAWAI.through
    extra = 1
    verbose_name = 'Anak Pegawai'
    verbose_name_plural = 'Daftar Anak Pegawai'
    
class beasiswa_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_BEASISWA_PEGAWAI.through
    extra = 1
    verbose_name = 'Beasiswa Pegawai'
    verbose_name_plural = 'Daftar Beasiswa Pegawai'

class buku_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_BUKU_PEGAWAI.through
    extra = 1
    verbose_name = 'Buku Pegawai'
    verbose_name_plural = 'Data Buku Pegawai'

class diklat_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_DIKLAT_PEGAWAI.through
    extra = 1
    verbose_name = 'Diklat Pegawai'
    verbose_name_plural = 'Data Diklat Pegawai'

class karya_tulis_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_KARYA_TULIS_PEGAWAI.through
    extra = 1
    verbose_name = 'Karya Tulis Pegawai'
    verbose_name_plural = 'Data Karya Tulis Pegawai'

class kesejahteraan_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_KESEJAHTERAAN_PEGAWAI.through
    extra = 1
    verbose_name = 'Kesejahteraan Pegawai'
    verbose_name_plural = 'Data Kesejahteraan Pegawai'

class tunjangan_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_TUNJANGAN_PEGAWAI.through
    extra = 1
    verbose_name = 'Tunjangan Pegawai'
    verbose_name_plural = 'Data Tunjangan Pegawai'

class tugas_tambahan_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_TUNJANGAN_PEGAWAI.through
    extra = 1
    verbose_name = 'Tugas Tambahan Pegawai'
    verbose_name_plural = 'Data Tugas Tambahan Pegawai'
    
class penghargaan_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_PENGHARGAAN_PEGAWAI.through
    extra = 1
    verbose_name = 'Penghargaan Pegawai'
    verbose_name_plural = 'Data Penghargaan Pegawai'

class nilai_tes_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_NILAI_TEST_PEGAWAI.through
    extra = 1
    verbose_name = 'Nilai Tes Pegawai'
    verbose_name_plural = 'Data Nilai Tes Pegawai'
    
class riwayat_gaji_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_RIWAYAT_GAJI_PEGAWAI.through
    extra = 1
    verbose_name = 'Riwayat Gaji Pegawai'
    verbose_name_plural = 'Data Riwayat Gaji Pegawai'

class riwayat_jabatan_struktural_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI.through
    extra = 1
    verbose_name = 'Riwayat Jabatan Struktural Pegawai'
    verbose_name_plural = 'Data Riwayat Jabatan Struktural Pegawai'
    
class riwayat_kepangkatan_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_RIWAYAT_KEPANGKATAN_PEGAWAI.through
    extra = 1
    verbose_name = 'Riwayat Kepangkatan Pegawai'
    verbose_name_plural = 'Data Riwayat Kepangkatan Pegawai'

class pendidikan_normal_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_PENDIDIKAN_NORMAL_PEGAWAI.through
    extra = 1
    verbose_name = 'Pendidikan Normal Pegawai'
    verbose_name_plural = 'Data Pendidikan Normal Pegawai'

class sertifikasi_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_SERTIFIKASI_PEGAWAI.through
    extra = 1
    verbose_name = 'Sertifikasi Pegawai'
    verbose_name_plural = 'Data Sertifikasi Pegawai'

class jabatan_fungsional_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI.through
    extra = 1
    verbose_name = 'Jabatan Fungsional Pegawai'
    verbose_name_plural = 'Data Jabatan Fungsional Pegawai'

class riwayat_karir_guru_pegawai(admin.TabularInline):
    model = DataPegawai.DATA_RIWAYAT_KARIR_GURU_PEGAWAI.through
    extra = 1
    verbose_name = 'Riwayat Karir Guru Pegawai'
    verbose_name_plural = 'Data Riwayat Karir Guru Pegawai'
    
class DataPegawaiAdmin(admin.ModelAdmin):
    inlines = [
        kompetensi_pegawai_inline,
        anak_pegawai_inline,
        beasiswa_pegawai,
        buku_pegawai,
        diklat_pegawai,
        karya_tulis_pegawai,
        kesejahteraan_pegawai,
        tunjangan_pegawai,
        tugas_tambahan_pegawai,
        penghargaan_pegawai,
        nilai_tes_pegawai,
        riwayat_gaji_pegawai,
        riwayat_jabatan_struktural_pegawai,
        riwayat_kepangkatan_pegawai,
        pendidikan_normal_pegawai,
        sertifikasi_pegawai,
        jabatan_fungsional_pegawai,
        riwayat_karir_guru_pegawai
    ]
    exclude = ('DATA_KOMPETENSI_PEGAWAI', 'DATA_ANAK_PEGAWAI', 'DATA_BEASISWA_PEGAWAI', 'DATA_BUKU_PEGAWAI', 'DATA_DIKLAT_PEGAWAI','DATA_KARYA_TULIS_PEGAWAI', 'DATA_KESEJAHTERAAN_PEGAWAI', 'DATA_TUNJANGAN_PEGAWAI', 'DATA_TUGAS_TAMBAHAN_PEGAWAI', 'DATA_PENGHARGAAN_PEGAWAI', 'DATA_NILAI_TEST_PEGAWAI', 'DATA_RIWAYAT_GAJI_PEGAWAI', 'DATA_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI', 'DATA_RIWAYAT_KEPANGKATAN_PEGAWAI', 'DATA_PENDIDIKAN_NORMAL_PEGAWAI', 'DATA_SERTIFIKASI_PEGAWAI', 'DATA_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI', 'DATA_RIWAYAT_KARIR_GURU_PEGAWAI',)


admin.site.register(DataPegawai, DataPegawaiAdmin)

