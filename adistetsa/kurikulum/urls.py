from django.urls.conf import path

from .views import *
from .filter_views import *
from .import_views import *

urlpatterns = [
    path('kurikulum/kelas', KelasListView.as_view(), name='kelas'),
    path('kurikulum/mata_pelajaran', MataPelajaranListView.as_view(), name='mata_pelajaran'),
    path('kurikulum/semester', SemesterListView.as_view(), name='semester'),
    path('kurikulum/tahun_ajaran', TahunAjaranListView.as_view(), name='tahun_ajaran'),
    path('kurikulum/ktsp', KTSPListView.as_view(), name='ktsp'),
    path('kurikulum/ktsp/<int:pk>', KTSPDetailView.as_view(), name='ktsp'),
    path('kurikulum/silabus_rpb', SilabusRPBListView.as_view(), name='silabus_rpb'),
    path('kurikulum/silabus_rpb/<int:pk>', SilabusRPBDetailView.as_view(), name='silabus_rpb'),
    path('kurikulum/tata_tertib', TataTertibListView.as_view(), name='tata_tertib'),
    path('kurikulum/tata_tertib/<int:pk>', TataTertibDetailView.as_view(), name='tata_tertib'),
    path('kurikulum/poin_pelanggaran', PoinPelanggaranListView.as_view(), name='poin_pelanggaran'),
    path('kurikulum/kategori_tata_tertib', KategoriTataTertibListView.as_view(), name='kategori_tata_tertib'),
    #path('data_tata_tertib', TataTertibListView.as_view(), name='data_tata_tertib'),
    #path('data_tata_tertib/<int:tata_tertib_id>', TataTertibDetailView.as_view(), name='data_tata_tertib'),
    #path('data_mata_pelajaran', MataPelajaranListView.as_view(), name='data_mata_pelajaran'),
    #path('data_mata_pelajaran/<int:mata_pelajaran_id>', MataPelajaranDetailView.as_view(), name='data_mata_pelajaran'),
    #path('data_kelas', KelasListView.as_view(), name='data_kelas'),
    #path('data_kelas/<int:kelas_id>', KelasDetailView.as_view(), name='data_kelas'),
    #path('data_poin_pelanggaran', PoinPelanggaranListView.as_view(), name='data_poin_pelanggaran'),
    #path('data_poin_pelanggaran/<int:kelas_id>', PoinPelanggaranDetailView.as_view(), name='data_poin_pelanggaran'),
]