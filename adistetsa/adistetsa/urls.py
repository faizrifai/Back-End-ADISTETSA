from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from dataprofil import views

router = routers.DefaultRouter()
router.register(r'data_siswa', views.DataSiswaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
