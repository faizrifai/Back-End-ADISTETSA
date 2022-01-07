from django.contrib.auth.models import User, Group

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources

from .models import *

# Register your import_export resource model here
class JadwalPelajaranResource(resources.ModelResource):

    class Meta:
        model = JadwalPelajaran
        exclude = ('ID',)
        import_id_fields = ('PELAJARAN',)
