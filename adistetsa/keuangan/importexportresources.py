from ast import mod
from pyexpat import model
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, CharWidget, ManyToManyWidget
from import_export import resources
from import_export.results import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError

from .models import *



class PembayaranResource(resources.ModelResource):
    nama_siswa = Field(
        column_name='NAMA_SISWA',
        attribute='NAMA_SISWA',
        widget = CharWidget()
    )
    
    class Meta: 
        model = Pembayaran
        fields = ('JENIS_PEMBAYARAN','TANGGAL_PEMBAYARAN', 'PEMBAYARAN_DPSM_RUTIN','PEMBAYARAN_DPSM_INSINDENTAL', 'BIMBEL', 'NOMINAL_SPP', 'PEMBAYARAN_SPP')
        exclude = ('ID',)
        import_id_fields = ('nama_siswa',)
        