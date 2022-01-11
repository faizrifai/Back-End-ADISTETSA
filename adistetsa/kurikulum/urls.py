from django.urls.conf import path

from .views import *

urlpatterns = [
    #path('data_tata_tertib', TataTertibListView.as_view(), name='data_tata_tertib'),
    #path('data_tata_tertib/<int:tata_tertib_id>', TataTertibDetailView.as_view(), name='data_tata_tertib'),
    #path('data_mata_pelajaran', MataPelajaranListView.as_view(), name='data_mata_pelajaran'),
    #path('data_mata_pelajaran/<int:mata_pelajaran_id>', MataPelajaranDetailView.as_view(), name='data_mata_pelajaran'),
    #path('data_kelas', KelasListView.as_view(), name='data_kelas'),
    #path('data_kelas/<int:kelas_id>', KelasDetailView.as_view(), name='data_kelas'),
    #path('data_poin_pelanggaran', PoinPelanggaranListView.as_view(), name='data_poin_pelanggaran'),
    #path('data_poin_pelanggaran/<int:kelas_id>', PoinPelanggaranDetailView.as_view(), name='data_poin_pelanggaran'),
    path('kurikulum/data_silabus_rpb_list', DataSilabusRPBListView.as_view(), name='silabus_rpb'),
    path('kurikulum/data_silabus_rpb_create', DataSilabusRPBCreateView.as_view(), name='silabus_rpb'),
    path('kurikulum/data_silabus_rpb/<int:pk>', DataSilabusRPBDetailView.as_view(), name='silabus_rpb'),
    
]