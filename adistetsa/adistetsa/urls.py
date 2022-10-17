from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from filebrowser.sites import site

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Adi Stetsa API",
        default_version="v1",
        description="Website ini adalah dokumentasi API, sebagai referensi untuk integrasi dengan Front End",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="adistetsa@gmail.com"),
        license=openapi.License(name="None"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin_urls = [
    path("admin/filebrowser/", site.urls),
    path("admin/", admin.site.urls, name="admin"),
]

app_urls = [
    path("", include("adiwiyata.urls")),
    path("", include("bimbingan_konseling.urls")),
    path("", include("dataprofil.urls")),
    path("", include("hubungan_masyarakat.urls")),
    path("", include("kesiswaan.urls")),
    path("", include("kurikulum.urls")),
    path("", include("kustom_autentikasi.urls")),
    path("", include("perpustakaan.urls")),
    path("", include("sarana_prasarana.urls")),
]

swagger_urls = [
    re_path(r"^$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns = (
    [
        # path('__debug__/', include('debug_toolbar.urls')),
        path("login/", TokenObtainPairView.as_view(), name="login"),
        path("login/refresh", TokenRefreshView.as_view(), name="refresh_token"),
        path(
            "devices",
            FCMDeviceAuthorizedViewSet.as_view({"post": "create"}),
            name="create_fcm_device",
        ),
    ]
    + admin_urls
    + app_urls
    + swagger_urls
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
