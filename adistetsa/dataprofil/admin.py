from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

from .models import *

# Register your models here.
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

class DataGuruResource(resources.ModelResource):

    class Meta:
        model = DataGuru
        exclude = ('ID',)
        import_id_fields = ('NIK',)

class DataGuruAdmin(ImportExportModelAdmin):
    list_display = ('NIP', 'NAMA_LENGKAP', 'kompetensi_guru', 'anak_guru', 'beasiswa_guru','buku_guru','diklat_guru','karya_tulis_guru','kesejahteraan_guru','tunjangan_guru','tugas_tambahan_guru','penghargaan_guru','nilai_tes_guru','riwayat_gaji_berkala_guru','riwayat_jabatan_struktural_guru','riwayat_kepangkatan_guru','riwayat_pendidikan_formal_guru','riwayat_sertifikasi_guru','riwayat_jabatan_fungsional_guru','riwayat_karir_guru')
    search_fields = ['NIP', 'NAMA_LENGKAP']
    list_per_page = 10

    resource_class = DataGuruResource

    def kompetensi_guru(self, obj):
        daftar = DataKompetensiGuru.objects.filter(OWNER=obj)
        count = daftar.count()

        base_url = reverse('admin:dataprofil_datakompetensiguru_changelist')

        if (count == 0):
            return mark_safe('0 Kompetensi')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Kompetensi</a>' % (base_url, obj.ID, count))

    def anak_guru(self, obj):
        daftar_anak = DataAnakGuru.objects.filter(OWNER=obj)
        count = daftar_anak.count()

        base_url = reverse('admin:dataprofil_dataanakguru_changelist')

        if (count == 0):
            return mark_safe('0 Anak')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Anak</a>' % (base_url, obj.ID, count))
    
    def beasiswa_guru(self, obj):
        daftar_beasiswa = DataBeasiswaGuru.objects.filter(OWNER=obj)
        count = daftar_beasiswa.count()

        base_url = reverse('admin:dataprofil_databeasiswaguru_changelist')

        if (count == 0):
            return mark_safe('0 Beasiswa')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Beasiswa</a>' % (base_url, obj.ID, count))
    
    def buku_guru(self, obj):
        daftar_buku = DataBukuGuru.objects.filter(OWNER=obj)
        count = daftar_buku.count()

        base_url = reverse('admin:dataprofil_databukuguru_changelist')

        if (count == 0):
            return mark_safe('0 Buku')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Buku</a>' % (base_url, obj.ID, count))
    
    def diklat_guru(self, obj):
        daftar_diklat = DataDiklatGuru.objects.filter(OWNER=obj)
        count = daftar_diklat.count()

        base_url = reverse('admin:dataprofil_datadiklatguru_changelist')

        if (count == 0):
            return mark_safe('0 Diklat')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Diklat</a>' % (base_url, obj.ID, count))
    
    def karya_tulis_guru(self, obj):
        daftar_karya_tulis = DataKaryaTulisGuru.objects.filter(OWNER=obj)
        count = daftar_karya_tulis.count()

        base_url = reverse('admin:dataprofil_datakaryatulisguru_changelist')

        if (count == 0):
            return mark_safe('0 Karya Tulis')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Karya Tulis</a>' % (base_url, obj.ID, count))
    
    def kesejahteraan_guru(self, obj):
        daftar_kesejahteraan = DataKesejahteraanGuru.objects.filter(OWNER=obj)
        count = daftar_kesejahteraan.count()

        base_url = reverse('admin:dataprofil_datakesejahteraanguru_changelist')

        if (count == 0):
            return mark_safe('0 Kesejahteraan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Kesejahteraan</a>' % (base_url, obj.ID, count))
    
    def tunjangan_guru(self, obj):
        daftar_tunjangan = DataTunjanganGuru.objects.filter(OWNER=obj)
        count = daftar_tunjangan.count()

        base_url = reverse('admin:dataprofil_datatunjanganguru_changelist')

        if (count == 0):
            return mark_safe('0 Tunjangan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Tunjangan</a>' % (base_url, obj.ID, count))
    
    def tugas_tambahan_guru(self, obj):
        daftar_tugas_tambahan = DataTugasTambahanGuru.objects.filter(OWNER=obj)
        count = daftar_tugas_tambahan.count()

        base_url = reverse('admin:dataprofil_datatugastambahanguru_changelist')

        if (count == 0):
            return mark_safe('0 Tugas Tambahan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Tugas Tambahan</a>' % (base_url, obj.ID, count))
    
    def penghargaan_guru(self, obj):
        daftar_penghargaan = DataPenghargaanGuru.objects.filter(OWNER=obj)
        count = daftar_penghargaan.count()

        base_url = reverse('admin:dataprofil_datapenghargaanguru_changelist')

        if (count == 0):
            return mark_safe('0 Penghargaan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Penghargaan</a>' % (base_url, obj.ID, count))
    
    def nilai_tes_guru(self, obj):
        daftar_nilai_tes = DataNilaiTesGuru.objects.filter(OWNER=obj)
        count = daftar_nilai_tes.count()

        base_url = reverse('admin:dataprofil_datanilaitesguru_changelist')

        if (count == 0):
            return mark_safe('0 Nilai Tes')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Nilai Tes</a>' % (base_url, obj.ID, count))
    
    def riwayat_gaji_berkala_guru(self, obj):
        daftar_riwayat_gaji_berkala = DataRiwayatGajiBerkalaGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_gaji_berkala.count()

        base_url = reverse('admin:dataprofil_datariwayatgajiberkalaguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Gaji Berkala')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Gaji Berkala</a>' % (base_url, obj.ID, count))
    
    def riwayat_jabatan_struktural_guru(self, obj):
        daftar_riwayat_jabatan_struktural = DataRiwayatJabatanStrukturalGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_jabatan_struktural.count()

        base_url = reverse('admin:dataprofil_datariwayatjabatanstrukturalguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Jabatan Struktural')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Jabatan Struktural</a>' % (base_url, obj.ID, count))
    
    def riwayat_kepangkatan_guru(self, obj):
        daftar_riwayat_kepangkatan = DataRiwayatKepangkatanGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_kepangkatan.count()

        base_url = reverse('admin:dataprofil_datariwayatkepangkatanguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Kepangkatan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Kepangkatan</a>' % (base_url, obj.ID, count))
    
    def riwayat_pendidikan_formal_guru(self, obj):
        daftar_riwayat_pendidikan_formal = DataRiwayatPendidikanFormalGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_pendidikan_formal.count()

        base_url = reverse('admin:dataprofil_datariwayatpendidikanformalguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Pendidikan Formal')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Pendidikan Formal</a>' % (base_url, obj.ID, count))
    
    def riwayat_sertifikasi_guru(self, obj):
        daftar_riwayat_sertifikasi = DataRiwayatSertifikasiGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_sertifikasi.count()

        base_url = reverse('admin:dataprofil_datariwayatsertifikasiguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Sertifikasi Guru')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Sertifikasi</a>' % (base_url, obj.ID, count))
    
    def riwayat_jabatan_fungsional_guru(self, obj):
        daftar_riwayat_jabatan_fungsional = DataRiwayatJabatanFungsionalGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_jabatan_fungsional.count()

        base_url = reverse('admin:dataprofil_datariwayatjabatanfungsionalguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Jabatan Fungsional')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Jabatan Fungsional</a>' % (base_url, obj.ID, count))
    
    def riwayat_karir_guru(self, obj):
        daftar_riwayat_karir_guru = DataRiwayatKarirGuru.objects.filter(OWNER=obj)
        count = daftar_riwayat_karir_guru.count()

        base_url = reverse('admin:dataprofil_datariwayatkarirguru_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Karir Guru')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Karir</a>' % (base_url, obj.ID, count))
    

    kompetensi_guru.short_description = "Daftar Kompetensi"
    anak_guru.short_description = "Daftar Anak"
    beasiswa_guru.short_description = "Daftar Beasiswa"
    buku_guru.short_description = "Daftar Buku"
    diklat_guru.short_description = "Daftar Diklat"
    karya_tulis_guru.short_description = "Daftar Karya Tulis"
    kesejahteraan_guru.short_description = "Daftar Kesejahteraan"
    tunjangan_guru.short_description = "Daftar Tunjangan"
    tugas_tambahan_guru.short_description = "Daftar Tugas Tambahan"
    penghargaan_guru.short_description = "Daftar Penghargaan"
    nilai_tes_guru.short_description = "Daftar Nilai Tes"
    riwayat_gaji_berkala_guru.short_description = "Daftar Riwayat Gaji Berkala"
    riwayat_jabatan_struktural_guru.short_description = "Daftar Riwayat Jabatan Struktural"
    riwayat_kepangkatan_guru.short_description = "Daftar Riwayat Kepangkatan"
    riwayat_pendidikan_formal_guru.short_description = "Daftar Pendidikan Formal"
    riwayat_sertifikasi_guru.short_description = "Daftar Sertifikasi Guru"
    riwayat_jabatan_fungsional_guru.short_description = "Daftar Riwayat Jabatan Fungsional"
    riwayat_karir_guru.short_description = "Daftar Riwayat Karir"

admin.site.register(DataGuru, DataGuruAdmin)

class DataKaryawanAdmin(admin.ModelAdmin):
    list_display = ('NIP', 'NAMA_LENGKAP', 'kompetensi_karyawan', 'anak_karyawan', 'beasiswa_karyawan','buku_karyawan','diklat_karyawan','karya_tulis_karyawan','kesejahteraan_karyawan','tunjangan_karyawan','tugas_tambahan_karyawan','penghargaan_karyawan','nilai_tes_karyawan','riwayat_gaji_berkala_karyawan','riwayat_jabatan_struktural_karyawan','riwayat_kepangkatan_karyawan','riwayat_pendidikan_formal_karyawan','riwayat_sertifikasi_karyawan','riwayat_jabatan_fungsional_karyawan','riwayat_karir_karyawan')
    search_fields = ['NIP', 'NAMA_LENGKAP']
    list_per_page = 10

    def kompetensi_karyawan(self, obj):
        daftar = DataKompetensiKaryawan.objects.filter(OWNER=obj)
        count = daftar.count()

        base_url = reverse('admin:dataprofil_datakompetensikaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Kompetensi')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Kompetensi</a>' % (base_url, obj.ID, count))

    def anak_karyawan(self, obj):
        daftar_anak = DataAnakKaryawan.objects.filter(OWNER=obj)
        count = daftar_anak.count()

        base_url = reverse('admin:dataprofil_dataanakkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Anak')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Anak</a>' % (base_url, obj.ID, count))
    
    def beasiswa_karyawan(self, obj):
        daftar_beasiswa = DataBeasiswaKaryawan.objects.filter(OWNER=obj)
        count = daftar_beasiswa.count()

        base_url = reverse('admin:dataprofil_databeasiswakaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Beasiswa')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Beasiswa</a>' % (base_url, obj.ID, count))
    
    def buku_karyawan(self, obj):
        daftar_buku = DataBukuKaryawan.objects.filter(OWNER=obj)
        count = daftar_buku.count()

        base_url = reverse('admin:dataprofil_databukukaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Buku')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Buku</a>' % (base_url, obj.ID, count))
    
    def diklat_karyawan(self, obj):
        daftar_diklat = DataDiklatKaryawan.objects.filter(OWNER=obj)
        count = daftar_diklat.count()

        base_url = reverse('admin:dataprofil_datadiklatkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Diklat')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Diklat</a>' % (base_url, obj.ID, count))
    
    def karya_tulis_karyawan(self, obj):
        daftar_karya_tulis = DataKaryaTulisKaryawan.objects.filter(OWNER=obj)
        count = daftar_karya_tulis.count()

        base_url = reverse('admin:dataprofil_datakaryatuliskaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Karya Tulis')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Karya Tulis</a>' % (base_url, obj.ID, count))
    
    def kesejahteraan_karyawan(self, obj):
        daftar_kesejahteraan = DataKesejahteraanKaryawan.objects.filter(OWNER=obj)
        count = daftar_kesejahteraan.count()

        base_url = reverse('admin:dataprofil_datakesejahteraankaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Kesejahteraan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Kesejahteraan</a>' % (base_url, obj.ID, count))
    
    def tunjangan_karyawan(self, obj):
        daftar_tunjangan = DataTunjanganKaryawan.objects.filter(OWNER=obj)
        count = daftar_tunjangan.count()

        base_url = reverse('admin:dataprofil_datatunjangankaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Tunjangan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Tunjangan</a>' % (base_url, obj.ID, count))
    
    def tugas_tambahan_karyawan(self, obj):
        daftar_tugas_tambahan = DataTugasTambahanKaryawan.objects.filter(OWNER=obj)
        count = daftar_tugas_tambahan.count()

        base_url = reverse('admin:dataprofil_datatugastambahankaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Tugas Tambahan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Tugas Tambahan</a>' % (base_url, obj.ID, count))
    
    def penghargaan_karyawan(self, obj):
        daftar_penghargaan = DataPenghargaanKaryawan.objects.filter(OWNER=obj)
        count = daftar_penghargaan.count()

        base_url = reverse('admin:dataprofil_datapenghargaankaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Penghargaan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Penghargaan</a>' % (base_url, obj.ID, count))
    
    def nilai_tes_karyawan(self, obj):
        daftar_nilai_tes = DataNilaiTesKaryawan.objects.filter(OWNER=obj)
        count = daftar_nilai_tes.count()

        base_url = reverse('admin:dataprofil_datanilaiteskaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Nilai Tes')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Nilai Tes</a>' % (base_url, obj.ID, count))
    
    def riwayat_gaji_berkala_karyawan(self, obj):
        daftar_riwayat_gaji_berkala = DataRiwayatGajiBerkalaKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_gaji_berkala.count()

        base_url = reverse('admin:dataprofil_datariwayatgajiberkalakaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Gaji Berkala')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Gaji Berkala</a>' % (base_url, obj.ID, count))
    
    def riwayat_jabatan_struktural_karyawan(self, obj):
        daftar_riwayat_jabatan_struktural = DataRiwayatJabatanStrukturalKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_jabatan_struktural.count()

        base_url = reverse('admin:dataprofil_datariwayatjabatanstrukturalkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Jabatan Struktural')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Jabatan Struktural</a>' % (base_url, obj.ID, count))
    
    def riwayat_kepangkatan_karyawan(self, obj):
        daftar_riwayat_kepangkatan = DataRiwayatKepangkatanKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_kepangkatan.count()

        base_url = reverse('admin:dataprofil_datariwayatkepangkatankaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Kepangkatan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Kepangkatan</a>' % (base_url, obj.ID, count))
    
    def riwayat_pendidikan_formal_karyawan(self, obj):
        daftar_riwayat_pendidikan_formal = DataRiwayatPendidikanFormalKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_pendidikan_formal.count()

        base_url = reverse('admin:dataprofil_datariwayatpendidikanformalkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Pendidikan Karyawan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Pendidikan Formal</a>' % (base_url, obj.ID, count))
    
    def riwayat_sertifikasi_karyawan(self, obj):
        daftar_riwayat_sertifikasi = DataRiwayatSertifikasiKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_sertifikasi.count()

        base_url = reverse('admin:dataprofil_datariwayatsertifikasikaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Sertifikasi')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Sertifikasi</a>' % (base_url, obj.ID, count))
    
    def riwayat_jabatan_fungsional_karyawan(self, obj):
        daftar_riwayat_jabatan_fungsional = DataRiwayatJabatanFungsionalKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_jabatan_fungsional.count()

        base_url = reverse('admin:dataprofil_datariwayatjabatanfungsionalkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Jabatan Fungsional')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Jabatan Fungsional</a>' % (base_url, obj.ID, count))
    
    def riwayat_karir_karyawan(self, obj):
        daftar_riwayat_karir_karyawan = DataRiwayatKarirKaryawan.objects.filter(OWNER=obj)
        count = daftar_riwayat_karir_karyawan.count()

        base_url = reverse('admin:dataprofil_datariwayatkarirkaryawan_changelist')

        if (count == 0):
            return mark_safe('0 Riwayat Karir Karyawan')
        
        return mark_safe(u'<a href="%s?OWNER__exact=%d">%d Riwayat Karir</a>' % (base_url, obj.ID, count))
    

    kompetensi_karyawan.short_description = "Daftar Kompetensi"
    anak_karyawan.short_description = "Daftar Anak"
    beasiswa_karyawan.short_description = "Daftar Beasiswa"
    buku_karyawan.short_description = "Daftar Buku"
    diklat_karyawan.short_description = "Daftar Diklat"
    karya_tulis_karyawan.short_description = "Daftar Karya Tulis"
    kesejahteraan_karyawan.short_description = "Daftar Kesejahteraan"
    tunjangan_karyawan.short_description = "Daftar Tunjangan"
    tugas_tambahan_karyawan.short_description = "Daftar Tugas Tambahan"
    penghargaan_karyawan.short_description = "Daftar Penghargaan"
    nilai_tes_karyawan.short_description = "Daftar Nilai Tes"
    riwayat_gaji_berkala_karyawan.short_description = "Daftar Riwayat Gaji Berkala"
    riwayat_jabatan_struktural_karyawan.short_description = "Daftar Riwayat Jabatan Struktural"
    riwayat_kepangkatan_karyawan.short_description = "Daftar Riwayat Kepangkatan"
    riwayat_pendidikan_formal_karyawan.short_description = "Daftar Pendidikan Formal"
    riwayat_sertifikasi_karyawan.short_description = "Daftar Sertifikasi Guru"
    riwayat_jabatan_fungsional_karyawan.short_description = "Daftar Riwayat Jabatan Fungsional"
    riwayat_karir_karyawan.short_description = "Daftar Riwayat Karir"

admin.site.register(DataKaryawan, DataKaryawanAdmin)

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