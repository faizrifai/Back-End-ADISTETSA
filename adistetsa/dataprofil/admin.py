from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
admin.site.register(DataKaryawan)
admin.site.register(DataAnakGuru)
admin.site.register(DataBeasiswaGuru)
admin.site.register(DataBukuGuru)
admin.site.register(DataDiklatGuru)
admin.site.register(DataKaryaTulisGuru)
admin.site.register(DataKesejahteraanGuru)
admin.site.register(DataNilaiTesGuru)
admin.site.register(DataPenghargaanGuru)
admin.site.register(DataRiwayatGajiBerkalaGuru)
admin.site.register(DataRiwayatJabatanFungsionalGuru)
admin.site.register(DataRiwayatJabatanStrukturalGuru)
admin.site.register(DataRiwayatKarirGuru)
admin.site.register(DataRiwayatKepangkatanGuru)
admin.site.register(DataRiwayatPendidikanFormalGuru)
admin.site.register(DataRiwayatSertifikasiGuru)
admin.site.register(DataTugasTambahanGuru)
admin.site.register(DataTunjanganGuru)
admin.site.register(DataAnakKaryawan)
admin.site.register(DataBeasiswaKaryawan)
admin.site.register(DataBukuKaryawan)
admin.site.register(DataDiklatKaryawan)
admin.site.register(DataKaryaTulisKaryawan)
admin.site.register(DataKesejahteraanKaryawan)
admin.site.register(DataKompetensiKaryawan)
admin.site.register(DataNilaiTesKaryawan)
admin.site.register(DataPenghargaanKaryawan)
admin.site.register(DataRiwayatGajiBerkalaKaryawan)
admin.site.register(DataRiwayatJabatanFungsionalKaryawan)
admin.site.register(DataRiwayatJabatanStrukturalKaryawan)
admin.site.register(DataRiwayatKarirKaryawan)
admin.site.register(DataRiwayatKepangkatanKaryawan)
admin.site.register(DataRiwayatPendidikanFormalKaryawan)
admin.site.register(DataRiwayatSertifikasiKaryawan)
admin.site.register(DataTugasTambahanKaryawan)
admin.site.register(DataTunjanganKaryawan)

class DataSiswaAdmin(admin.ModelAdmin):
    search_fields = ['NISN', 'NAMA']

admin.site.register(DataSiswa, DataSiswaAdmin)

class DataOrangTuaAdmin(admin.ModelAdmin):
    filter_horizontal = ('DATA_ANAK',)

admin.site.register(DataOrangTua, DataOrangTuaAdmin)

class DataGuruAdmin(admin.ModelAdmin):
    list_display = ('NIP', 'NAMA_LENGKAP', 'kompetensi_guru',)
    search_fields = ['NIP', 'NAMA_LENGKAP']

    def kompetensi_guru(self, obj):
        daftar = DataKompetensiGuru.objects.filter(OWNER=obj)
        count = daftar.count()

        base_url = reverse('admin:dataprofil_datakompetensiguru_changelist')

        if (count == 0):
            return mark_safe('0 Kompetensi')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Kompetensi</a>' % (base_url, obj.ID, count))

    kompetensi_guru.short_description = "Daftar Kompetensi"

admin.site.register(DataGuru, DataGuruAdmin)

class DataKompetensiGuruAdmin(admin.ModelAdmin):
    list_display = ('BIDANG_STUDI', 'URUTAN', 'OWNER')

admin.site.register(DataKompetensiGuru, DataKompetensiGuruAdmin)

# class DataGuruAdmin(admin.ModelAdmin):
#     filter_horizontal = ('DATA_KOMPETENSI_GURU', 'DATA_ANAK_GURU', 'DATA_BEASISWA_GURU', 'DATA_BUKU_GURU', 'DATA_DIKLAT_GURU', 'DATA_KARYA_TULIS_GURU', 'DATA_KESEJAHTERAAN_GURU', 'DATA_TUNJANGAN_GURU', 'DATA_TUGAS_TAMBAHAN_GURU', 'DATA_PENGHARGAAN_GURU', 'DATA_NILAI_TEST_GURU', 'DATA_RIWAYAT_GAJI_GURU', 'DATA_RIWAYAT_JABATAN_STRUKTURAL_GURU', 'DATA_RIWAYAT_KEPANGKATAN_GURU', 'DATA_PENDIDIKAN_NORMAL_GURU', 'DATA_SERTIFIKASI_GURU', 'DATA_RIWAYAT_JABATAN_FUNGSIONAL_GURU', 'DATA_RIWAYAT_KARIR_GURU',)

# admin.site.register(DataGuru, DataGuruAdmin)

# class DataKaryawanAdmin(admin.ModelAdmin):
#     filter_horizontal = ('DATA_KOMPETENSI_KARYAWAN', 'DATA_ANAK_KARYAWAN', 'DATA_BEASISWA_KARYAWAN', 'DATA_BUKU_KARYAWAN', 'DATA_DIKLAT_KARYAWAN', 'DATA_KARYA_TULIS_KARYAWAN', 'DATA_KESEJAHTERAAN_KARYAWAN', 'DATA_TUNJANGAN_KARYAWAN', 'DATA_TUGAS_TAMBAHAN_KARYAWAN', 'DATA_PENGHARGAAN_KARYAWAN', 'DATA_NILAI_TEST_KARYAWAN', 'DATA_RIWAYAT_GAJI_KARYAWAN', 'DATA_RIWAYAT_JABATAN_STRUKTURAL_KARYAWAN', 'DATA_RIWAYAT_KEPANGKATAN_KARYAWAN', 'DATA_PENDIDIKAN_NORMAL_KARYAWAN', 'DATA_SERTIFIKASI_KARYAWAN', 'DATA_RIWAYAT_JABATAN_FUNGSIONAL_KARYAWAN', 'DATA_RIWAYAT_KARIR_KARYAWAN',)

# admin.site.register(DataKaryawan, DataKaryawanAdmin)


# class kompetensi_pegawai_inline(admin.TabularInline):
#     model = DataPegawai.DATA_KOMPETENSI_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Kompetensi Pegawai'
#     verbose_name_plural = 'Daftar Kompetensi Pegawai'

# class anak_pegawai_inline(admin.TabularInline):
#     model = DataPegawai.DATA_ANAK_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Anak Pegawai'
#     verbose_name_plural = 'Daftar Anak Pegawai'
    
# class beasiswa_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_BEASISWA_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Beasiswa Pegawai'
#     verbose_name_plural = 'Daftar Beasiswa Pegawai'

# class buku_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_BUKU_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Buku Pegawai'
#     verbose_name_plural = 'Data Buku Pegawai'

# class diklat_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_DIKLAT_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Diklat Pegawai'
#     verbose_name_plural = 'Data Diklat Pegawai'

# class karya_tulis_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_KARYA_TULIS_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Karya Tulis Pegawai'
#     verbose_name_plural = 'Data Karya Tulis Pegawai'

# class kesejahteraan_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_KESEJAHTERAAN_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Kesejahteraan Pegawai'
#     verbose_name_plural = 'Data Kesejahteraan Pegawai'

# class tunjangan_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_TUNJANGAN_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Tunjangan Pegawai'
#     verbose_name_plural = 'Data Tunjangan Pegawai'

# class tugas_tambahan_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_TUNJANGAN_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Tugas Tambahan Pegawai'
#     verbose_name_plural = 'Data Tugas Tambahan Pegawai'
    
# class penghargaan_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_PENGHARGAAN_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Penghargaan Pegawai'
#     verbose_name_plural = 'Data Penghargaan Pegawai'

# class nilai_tes_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_NILAI_TEST_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Nilai Tes Pegawai'
#     verbose_name_plural = 'Data Nilai Tes Pegawai'
    
# class riwayat_gaji_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_RIWAYAT_GAJI_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Riwayat Gaji Pegawai'
#     verbose_name_plural = 'Data Riwayat Gaji Pegawai'

# class riwayat_jabatan_struktural_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Riwayat Jabatan Struktural Pegawai'
#     verbose_name_plural = 'Data Riwayat Jabatan Struktural Pegawai'
    
# class riwayat_kepangkatan_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_RIWAYAT_KEPANGKATAN_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Riwayat Kepangkatan Pegawai'
#     verbose_name_plural = 'Data Riwayat Kepangkatan Pegawai'

# class pendidikan_normal_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_PENDIDIKAN_NORMAL_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Pendidikan Normal Pegawai'
#     verbose_name_plural = 'Data Pendidikan Normal Pegawai'

# class sertifikasi_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_SERTIFIKASI_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Sertifikasi Pegawai'
#     verbose_name_plural = 'Data Sertifikasi Pegawai'

# class jabatan_fungsional_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Jabatan Fungsional Pegawai'
#     verbose_name_plural = 'Data Jabatan Fungsional Pegawai'

# class riwayat_karir_guru_pegawai(admin.TabularInline):
#     model = DataPegawai.DATA_RIWAYAT_KARIR_GURU_PEGAWAI.through
#     extra = 1
#     verbose_name = 'Riwayat Karir Guru Pegawai'
#     verbose_name_plural = 'Data Riwayat Karir Guru Pegawai'
    
# class DataPegawaiAdmin(admin.ModelAdmin):
#     inlines = [
#         kompetensi_pegawai_inline,
#         anak_pegawai_inline,
#         beasiswa_pegawai,
#         buku_pegawai,
#         diklat_pegawai,
#         karya_tulis_pegawai,
#         kesejahteraan_pegawai,
#         tunjangan_pegawai,
#         tugas_tambahan_pegawai,
#         penghargaan_pegawai,
#         nilai_tes_pegawai,
#         riwayat_gaji_pegawai,
#         riwayat_jabatan_struktural_pegawai,
#         riwayat_kepangkatan_pegawai,
#         pendidikan_normal_pegawai,
#         sertifikasi_pegawai,
#         jabatan_fungsional_pegawai,
#         riwayat_karir_guru_pegawai
#     ]
#     exclude = ('DATA_KOMPETENSI_PEGAWAI', 'DATA_ANAK_PEGAWAI', 'DATA_BEASISWA_PEGAWAI', 'DATA_BUKU_PEGAWAI', 'DATA_DIKLAT_PEGAWAI','DATA_KARYA_TULIS_PEGAWAI', 'DATA_KESEJAHTERAAN_PEGAWAI', 'DATA_TUNJANGAN_PEGAWAI', 'DATA_TUGAS_TAMBAHAN_PEGAWAI', 'DATA_PENGHARGAAN_PEGAWAI', 'DATA_NILAI_TEST_PEGAWAI', 'DATA_RIWAYAT_GAJI_PEGAWAI', 'DATA_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI', 'DATA_RIWAYAT_KEPANGKATAN_PEGAWAI', 'DATA_PENDIDIKAN_NORMAL_PEGAWAI', 'DATA_SERTIFIKASI_PEGAWAI', 'DATA_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI', 'DATA_RIWAYAT_KARIR_GURU_PEGAWAI',)


# admin.site.register(DataPegawai, DataPegawaiAdmin)