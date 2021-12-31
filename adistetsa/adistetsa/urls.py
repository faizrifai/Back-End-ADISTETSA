from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from dataprofil import views

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.HomeView.as_view()),
    path('api-token-auth', views.ObtainAuthTokenView.as_view()),
    path('data_siswa', views.DataSiswaListView.as_view()),
    path('data_siswa/<int:pk>', views.DataSiswaDetailView.as_view()),
    path('api-token-auth', views.ObtainAuthTokenView.as_view()),
    path('data_orang_tua', views.DataOrangTuaSiswaListView.as_view()),
    path('data_orang_tua/<int:pk>', views.DataOrangTuaDetailView.as_view()),
    path('data_karyawan', views.DataKaryawanListView.as_view()),
    path('data_karyawan/<int:pk>', views.DataKaryawanDetailView.as_view()),
    path('data_guru', views.DataGuruListView.as_view()),
    path('data_guru/<int:pk>', views.DataGuruDetailView.as_view()),
    path('data_kompetensi_guru', views.DataKompetensiGuruListView.as_view()),
    path('data_kompetensi_guru/<int:pk>', views.DataKompetensiGuruDetailView.as_view()),
    path('data_kompetensi_karyawan', views.DataKompetensiKaryawanListView.as_view()),
    path('data_kompetensi_karyawan/<int:pk>', views.DataKompetensiKaryawanDetailView.as_view()),
    path('data_anak_guru', views.DataAnakGuruListView.as_view()),
    path('data_anak_guru/owner/<int:id>', views.DataBeasiswaGuruView.as_view()),
    path('data_anak_guru/<int:pk>', views.DataAnakGuruDetailView.as_view()),
    path('data_anak_karyawan', views.DataAnakKaryawanListView.as_view()),
    path('data_anak_karyawan/<int:pk>', views.DataAnakKaryawanDetailView.as_view()),
    path('data_beasiswa_guru', views.DataBeasiswaGuruListView.as_view()),
    path('data_beasiswa_guru/owner/<int:id>', views.DataBeasiswaGuruView.as_view()),
    path('data_beasiswa_guru/<int:id>/<int:pk>', views.DataBeasiswaGuru2View.as_view()),
    path('data_beasiswa_karyawan', views.DataBeasiswaKaryawanListView.as_view()),
    path('data_beasiswa_karyawan/<int:pk>', views.DataBeasiswaKaryawanDetailView.as_view()),
    path('docs/', include_docs_urls(title='Adi Stetsa API')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
