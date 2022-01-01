from django.urls.conf import path

from .views import *

urlpatterns = [
    path('profile', ProfilDetailView.as_view(), name='profile'),
    path('daftar_role', RoleUserView.as_view(), name='daftar_role'),
]