from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Adi Stetsa API",
        default_version='v1',
        description="Website ini adalah dokumentasi API, sebagai referensi untuk integrasi dengan Front End",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="adistetsa@gmail.com"),
        license=openapi.License(name="None"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include_docs_urls(title='Adi Stetsa API')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh', TokenObtainPairView.as_view(), name='refresh_token'),
    path('', include('kustom_autentikasi.urls')),
    path('', include('dataprofil.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
