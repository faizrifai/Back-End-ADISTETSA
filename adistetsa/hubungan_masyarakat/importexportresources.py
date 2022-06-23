from django.apps import apps
from import_export import resources
from import_export.fields import Field
from import_export.widgets import (CharWidget, ForeignKeyWidget,
                                   ManyToManyWidget)

from .models import *

class LogUKSTendikResource(resources.ModelResource):
    
    nama = Field(
        column_name='NAMA',
        attribute='NAMA',
        widget=ForeignKeyWidget(DataGuru, 'NAMA_LENGKAP')
    )
    
    class Meta:
        model = LogUKSTendik
        fields = ('nama','JENIS_PTK', 'TANGGAL', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN', 'TINDAK_LANJUT')
        exclude = ('ID',)
        

class LogUKSKaryawanResource(resources.ModelResource):
    
    nama = Field(
        column_name='NAMA',
        attribute='NAMA',
        widget=ForeignKeyWidget(DataKaryawan, 'NAMA_LENGKAP')
    )
    
    class Meta:
        model = LogUKSKaryawan
        fields = ('nama','JENIS_PTK', 'TANGGAL', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN', 'TINDAK_LANJUT')
        exclude = ('ID',)
           
class LogUKSSiswaResource(resources.ModelResource):
    
    nama = Field(
        column_name='NAMA',
        attribute='NAMA',
        widget=CharWidget()
    )
    
    # guru = Field(
    #     column_name='NAMA',
    #     attribute='NAMA',
    #     widget=ForeignKeyWidget(KelasSiswa, 'NAMA__NIS__NAMA_LENGKAP')
    # )
    
    class Meta:
        fields = ('nama', 'kelas','nisn', 'TANGGAL', 'JENIS_PEMERIKSAAN', 'OBAT_DIBERIKAN', 'TINDAK_LANJUT')
        model = LogUKSSiswa
        exclude = ('ID',)
        
class BukuTamuResource(resources.ModelResource):
    class Meta:
        model = BukuTamu
        exclude = ('ID',)