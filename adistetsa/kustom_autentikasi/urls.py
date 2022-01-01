from django.urls.conf import path

from .views import *

urlpatterns = [
    path('profile', ProfilDetailView.as_view(), name='profile'),
    path('daftar_role', RoleUserView.as_view(), name='daftar_role'),
    path('import_data_siswa', ImportDataSiswaView.as_view(), name='import_data_siswa'),
    path('export_data_siswa', ExportDataSiswaView.as_view(), name='export_data_siswa'),
    path('import_data_guru', ImportDataGuruView.as_view(), name='import_data_guru'),
    path('export_data_guru', ExportDataGuruView.as_view(), name='export_data_guru'),
    path('import_data_karyawan', ImportDataKaryawanView.as_view(), name='import_data_karyawan'),
    path('export_data_karyawan', ExportDataKaryawanView.as_view(), name='export_data_karyawan'),
    path('import_data_orang_tua', ImportDataOrangTuaView.as_view(), name='import_data_orang_tua'),
    path('export_data_orang_tua', ExportDataOrangTuaView.as_view(), name='export_data_orang_tua'),
    path('import_data_siswa_user', ImportDataSiswaUserView.as_view(), name='import_data_siswa_user'),
    path('export_data_siswa_user', ExportDataSiswaUserView.as_view(), name='export_data_siswa_user'),
    # path('import_data_guru_user', ImportDataGuruUserView.as_view(), name='import_data_guru_user'),
    # path('export_data_guru_user', ExportDataGuruUserView.as_view(), name='export_data_guru_user'),
    # path('import_data_karyawan_user', ImportDataKaryawanUserView.as_view(), name='import_data_karyawan_user'),
    # path('export_data_karyawan_user', ExportDataKaryawanUserView.as_view(), name='export_data_karyawan_user'),
]