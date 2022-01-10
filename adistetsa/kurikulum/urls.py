from django.urls.conf import path

from .views import *

urlpatterns = [
    path('kurikulum/ktsp', DataKTSPListView.as_view(), name='ktsp'),
    path('kurikulum/ktsp/<int:pk>', DataKTSPDetailView.as_view(), name='ktsp'),
]