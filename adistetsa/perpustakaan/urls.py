from django.urls.conf import path

from .views import *
#from .filter_views import *
#from .import_views import *

urlpatterns = [
    path('perpustakaan/katalog_buku', KatalogBukuListView.as_view(), name='katalog_buku'),
]