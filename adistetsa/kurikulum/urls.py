from django.urls.conf import path

from .views import *
from .filter_views import *
from .import_views import *

urlpatterns = [
    path('kurikulum/mata_pelajaran', MataPelajaranListView.as_view(), name='mata_pelajaran'),
    path('kurikulum/tahun_ajaran', TahunAjaranListView.as_view(), name='tahun_ajaran'),
    path('kurikulum/semester', SemesterListView.as_view(), name='semester'),
    path('kurikulum/kelas', KelasListView.as_view(), name='kelas'),
    path('kurikulum/ktsp', KTSPListView.as_view(), name='ktsp'),
    path('kurikulum/ktsp/<int:pk>', KTSPDetailView.as_view(), name='ktsp'),
    path('kurikulum/silabus_rpb', SilabusRPBListView.as_view(), name='silabus_rpb'),
    path('kurikulum/silabus_rpb/<int:pk>', SilabusRPBDetailView.as_view(), name='silabus_rpb'),
    path('kurikulum/import_tata_tertib', ImportDataTataTertibView.as_view(), name='import_tata_tertib'),
    path('kurikulum/export_tata_tertib', ExportDataTataTertibView.as_view(), name='export_tata_tertib'),
    path('kurikulum/poin_pelanggaran', PoinPelanggaranListView.as_view(), name='poin_pelanggaran'),
    path('kurikulum/kategori_tata_tertib', KategoriTataTertibListView.as_view(), name='kategori_tata_tertib'),
]