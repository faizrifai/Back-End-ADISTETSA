import random

from django.db import transaction
from django.core.management.base import BaseCommand

from dataprofil.models import *
from dataprofil.factories import (
    DataSiswaFactory,
    DataOrangTuaFactory,
    DataKompetensiPegawaiFactory,
    DataAnakPegawaiFactory,
    DataBeasiswaPegawaiFactory,
    DataBukuPegawaiFactory,
    DataDiklatPegawaiFactory,
    DataKaryaTulisPegawaiFactory,
    DataKesejahteraanPegawaiFactory,
    DataTunjanganPegawaiFactory,
    DataTugasTambahanPegawaiFactory,
    DataPenghargaanPegawaiFactory,
    DataNilaiTesPegawaiFactory,
    DataRiwayatGajiBerkalaPegawaiFactory,
    DataRiwayatJabatanStrukturalPegawaiFactory,
    DataRiwayatKepangkatanPegawaiFactory,
    DataRiwayatPendidikanFormalPegawaiFactory,
    DataRiwayatSertifikasiPegawaiFactory,
    DataRiwayatJabatanFungsionalPegawaiFactory,
    DataRiwayatKarirGuruPegawaiFactory,
    DataGuruFactory,
    DataKaryawanFactory,
)

NUM_SISWA = 50
NUM_ORANG_TUA = 50
NUM_KOMPETENSI_PEGAWAI = 50
NUM_ANAK_PEGAWAI = 50
NUM_BEASISWA_PEGAWAI = 50
NUM_BUKU_PEGAWAI = 50
NUM_DIKLAT_PEGAWAI = 50
NUM_KARYA_TULIS_PEGAWAI = 50
NUM_KESEJAHTERAAN_PEGAWAI = 50
NUM_TUNJANGAN_PEGAWAI = 50
NUM_TUGAS_TAMBAHAN_PEGAWAI = 50
NUM_PENGHARGAAN_PEGAWAI = 50
NUM_NILAI_TES_PEGAWAI = 50
NUM_RIWAYAT_GAJI_BERKALA_PEGAWAI = 50
NUM_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI = 50
NUM_RIWAYAT_KEPANGKATAN_PEGAWAI = 50
NUM_RIWAYAT_PENDIDIKAN_FORMAL_PEGAWAI = 50
NUM_RIWAYAT_SERTIFIKASI_PEGAWAI = 50
NUM_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI = 50
NUM_RIWAYAT_KARIR_GURU_PEGAWAI = 50
NUM_PEGAWAI = 50

class Command(BaseCommand):
    help = "Melakukan generate data dummy"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Menghapus data lama...")
        models = [DataSiswa, DataOrangTua, DataKompetensiPegawai]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Membuat data baru...")

        # Membuat data siswa
        for _ in range(NUM_SISWA):
            data_siswa = DataSiswaFactory()
            
        # Membuat data orang tua
        for _ in range(NUM_ORANG_TUA):
            data_orang_tua = DataOrangTuaFactory()
        
        
        for _ in range(NUM_KOMPETENSI_PEGAWAI):
            data_kompetensi_pegawai = DataKompetensiPegawaiFactory()
        
        for _ in range(NUM_ANAK_PEGAWAI):
            data_anak_pegawai = DataAnakPegawaiFactory()
        
        for _ in range(NUM_BEASISWA_PEGAWAI):
            data_beasiswa_pegawai = DataBeasiswaPegawaiFactory()
        
        for _ in range(NUM_BUKU_PEGAWAI):
            data_buku_pegawai = DataBukuPegawaiFactory()
        
        for _ in range(NUM_DIKLAT_PEGAWAI):
            data_diklat_pegawai = DataDiklatPegawaiFactory()
        
        for _ in range(NUM_KARYA_TULIS_PEGAWAI):
            data_karya_tulis_pegawai = DataKaryaTulisPegawaiFactory()
        
        for _ in range(NUM_KESEJAHTERAAN_PEGAWAI):
            data_kesejahteraan_pegawai = DataKesejahteraanPegawaiFactory()
            
        for _ in range(NUM_TUNJANGAN_PEGAWAI):
            data_tunjangan_pegawai = DataTunjanganPegawaiFactory()
            
        for _ in range(NUM_TUGAS_TAMBAHAN_PEGAWAI):
            data_tugas_tambahan_pegawai = DataTugasTambahanPegawaiFactory()
        
        for _ in range(NUM_PENGHARGAAN_PEGAWAI):
            data_penghargaan_pegawai = DataPenghargaanPegawaiFactory()
            
        for _ in range(NUM_NILAI_TES_PEGAWAI):
            data_nilai_tes_pegawai = DataNilaiTesPegawaiFactory()
            
        for _ in range(NUM_RIWAYAT_GAJI_BERKALA_PEGAWAI):
            data_riwayat_gaji_berkala_pegawai = DataRiwayatGajiBerkalaPegawaiFactory()
            
        for _ in range(NUM_RIWAYAT_JABATAN_STRUKTURAL_PEGAWAI):
            data_riwayat_jabatan_struktural_pegawai = DataRiwayatJabatanStrukturalPegawaiFactory()
            
        for _ in range(NUM_RIWAYAT_KEPANGKATAN_PEGAWAI):
            data_riwayat_kepangkatan_pegawai = DataRiwayatKepangkatanPegawaiFactory()
            
        for _ in range(NUM_RIWAYAT_PENDIDIKAN_FORMAL_PEGAWAI):
            data_riwayat_pendidikan_formal_pegawai = DataRiwayatPendidikanFormalPegawaiFactory()    
            
        for _ in range(NUM_RIWAYAT_SERTIFIKASI_PEGAWAI):
            data_riwayat_sertifikasi_pegawai = DataRiwayatSertifikasiPegawaiFactory()
        
        for _ in range(NUM_RIWAYAT_JABATAN_FUNGSIONAL_PEGAWAI):
            data_riwayat_jabatan_fungsional_pegawai = DataRiwayatJabatanFungsionalPegawaiFactory()
    
        for _ in range(NUM_RIWAYAT_KARIR_GURU_PEGAWAI):
            data_riwayat_karir_guru_pegawai = DataRiwayatKarirGuruPegawaiFactory()
            
        for _ in range(NUM_PEGAWAI):
            data_guru = DataGuruFactory()
            
        for _ in range(NUM_PEGAWAI):
            data_karyawan = DataKaryawanFactory()