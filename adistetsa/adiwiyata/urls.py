from django.urls.conf import path

from .views import *

urlpatterns = [
    path('adiwiyata/sanitasi_drainase', SanitasiDrainaseListView.as_view(), name='sanitasi_drainase'),
    path('adiwiyata/jaringan_kerja', JaringanKerjaListView.as_view(), name='jaringan_kerja'),
    path('adiwiyata/publikasi', PublikasiListView.as_view(), name='publikasi'),
    path('adiwiyata/daftar_kader', DaftarKaderListView.as_view(), name='daftar_kader'),
    path('adiwiyata/kegiatan_kader', KegiatanKaderListView.as_view(), name='kegiatan_kader'),

    path('adiwiyata/konservasi_energi', KonservasiEnergiListView.as_view(), name='konservasi_energi'),
    path('adiwiyata/konservasi_air', KonservasiAirListView.as_view(), name='konservasi_air'),

    path('adiwiyata/pembibitan_pohon', PembibitanPohonListView.as_view(), name='pembibitan_pohon'),
    path('adiwiyata/pemeliharaan_pohon', PemeliharaanPohonListView.as_view(), name='pemeliharaan_pohon'),

    path('adiwiyata/inovatif', KaryaInovatifListView.as_view(), name='inovatif'),
    path('adiwiyata/prlh', PenerapanPRLHListView.as_view(), name='prlh'),
    path('adiwiyata/reuse_reduce_recycle', ReuseReduceRecycleListView.as_view(), name='reuse_reduce_recycle'),
    path('adiwiyata/pemeliharaan_sampah', PemeliharaanSampahListView.as_view(), name='pemeliharaan_sampah'),
    path('adiwiyata/penanaman_pohon', PenanamanPohonListView.as_view(), name='penanaman_pohon'),
    path('adiwiyata/tabungan_sampah_tahun', FilterTahunListView.as_view(), name='tabungan_sampah_tahun'),
    path('adiwiyata/tabungan_sampah', TabunganSampahListView.as_view(), name='tabungan_sampah'),
]