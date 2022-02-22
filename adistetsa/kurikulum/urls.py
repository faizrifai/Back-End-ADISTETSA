from django.urls.conf import path

from .views import *
from .filter_views import *
from .import_views import *

urlpatterns = [
    path('kurikulum/kelas', KelasListView.as_view(), name='kelas'),
    path('kurikulum/mata_pelajaran', MataPelajaranListView.as_view(), name='mata_pelajaran'),
    path('kurikulum/semester', SemesterListView.as_view(), name='semester'),
    path('kurikulum/tahun_ajaran', TahunAjaranListView.as_view(), name='tahun_ajaran'),
    # path('kurikulum/ktsp', KTSPListView.as_view(), name='ktsp'),
    # path('kurikulum/ktsp/<int:pk>', KTSPDetailView.as_view(), name='ktsp'),
    # path('kurikulum/silabus_rpb', SilabusRPBListView.as_view(), name='silabus_rpb'),
    # path('kurikulum/silabus_rpb/<int:pk>', SilabusRPBDetailView.as_view(), name='silabus_rpb'),
    # path('kurikulum/tata_tertib', TataTertibListView.as_view(), name='tata_tertib'),
    # path('kurikulum/tata_tertib/<int:pk>', TataTertibDetailView.as_view(), name='tata_tertib'),
    # path('kurikulum/poin_pelanggaran', PoinPelanggaranListView.as_view(), name='poin_pelanggaran'),
    # path('kurikulum/poin_pelanggaran/<int:pk>', PoinPelanggaranDetailView.as_view(), name='poin_pelanggaran'),
    # path('kurikulum/kategori_tata_tertib', KategoriTataTertibListView.as_view(), name='kategori_tata_tertib'),
    # path('kurikulum/jadwal_pekan_aktif', JadwalPekanAktifListView.as_view(), name='jadwal_pekan_aktif'),
    # path('kurikulum/jadwal_pekan_aktif/<int:pk>', JadwalPekanAktifDetailView.as_view(), name='jadwal_pekan_aktif'),
    # path('kurikulum/jadwal_pekan_efektif_semester', JadwalPekanEfektifSemesterListView.as_view(), name='jadwal_pekan_efektif_semester'),
    # path('kurikulum/jadwal_pekan_efektif_semester/<int:pk>', JadwalPekanEfektifSemesterDetailView.as_view(), name='jadwal_pekan_tidak_efektif_semester'),
    # path('kurikulum/jadwal_pekan_tidak_efektif', JadwalPekanTidakEfektifListView.as_view(), name='jadwal_pekan_tidak_efektif'),
    # path('kurikulum/jadwal_pekan_tidak_efektif/<int:pk>', JadwalPekanTidakEfektifDetailView.as_view(), name='jadwal_pekan_tidak_efektif'),
    # path('kurikulum/jadwal_mengajar_guru', JadwalMengajarGuruListView.as_view(), name='jadwal_mengajar_guru'),
    # path('kurikulum/kelas_siswa', KelasSiswaListView.as_view(), name='kelas_siswa'),
    # path('kurikulum/tambah_kelas_siswa', TambahKelasSiswaView.as_view(), name='tambah_kelas_siswa'),
    path('kurikulum/jurnal_belajar_mengajar', DaftarJurnalBelajarGuruListView.as_view(), name='jurnal_belajar_mengajar_guru'),
    path('kurikulum/jurnal_belajar_pertemuan/<int:id_jurnal_belajar_mengajar>', JurnalBelajarGuruListView.as_view(), name='jurnal_belajar_pertemuan_guru'),
    path('kurikulum/presensi_siswa/<int:id_jurnal_belajar_pertemuan>', AbsensiSiswaListView.as_view(), name='presensi_siswa'),
    path('kurikulum/detail_presensi_siswa/<int:pk>', AbsensiSiswaDetailView.as_view(), name='detail_presensi_siswa'),
    #path('data_tata_tertib', TataTertibListView.as_view(), name='data_tata_tertib'),
    #path('data_tata_tertib/<int:tata_tertib_id>', TataTertibDetailView.as_view(), name='data_tata_tertib'),
    #path('data_mata_pelajaran', MataPelajaranListView.as_view(), name='data_mata_pelajaran'),
    #path('data_mata_pelajaran/<int:mata_pelajaran_id>', MataPelajaranDetailView.as_view(), name='data_mata_pelajaran'),
    #path('data_kelas', KelasListView.as_view(), name='data_kelas'),
    #path('data_kelas/<int:kelas_id>', KelasDetailView.as_view(), name='data_kelas'),
    #path('data_poin_pelanggaran', PoinPelanggaranListView.as_view(), name='data_poin_pelanggaran'),
    #path('data_poin_pelanggaran/<int:kelas_id>', PoinPelanggaranDetailView.as_view(), name='data_poin_pelanggaran'),
]