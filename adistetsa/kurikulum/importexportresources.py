from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources

from .models import *

# Register your import_export resource model here
class TataTertibResource(resources.ModelResource):

    class Meta:
        model = TataTertib
        fields = ('KETERANGAN')
        exclude = ('ID')
        import_id_fields = ('KETERANGAN')

class PoinPelanggaranResource(resources.ModelResource):

    class Meta:
        model = PoinPelanggaran
        fields = ('KETERANGAN', 'POIN')
        exclude = ('ID')
        import_id_fields = ('KETERANGAN')

class JadwalMengajarResource(resources.ModelResource):
    guru = Field(
        column_name='GURU',
        attribute='GURU',
        widget=ForeignKeyWidget(DataGuru, 'NAMA_LENGKAP')
    )

    class Meta:
        model = JadwalMengajar
        fields = ('guru')
        import_id_fields = ('ID',)
