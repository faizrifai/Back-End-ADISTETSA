from attr import fields
from import_export import resources
from import_export.fields import Field
from import_export.widgets import (CharWidget, ForeignKeyWidget,
                                   ManyToManyWidget)

from .models import *

class DaftarKaderResource (resources.ModelResource):
    
    nis = Field(
        column_name= 'NIS', 
        attribute= 'NIS', 
        widget= ForeignKeyWidget(DataSiswa, 'NIS')
    )
    
    class Meta:
        model = DaftarKader
        fields = ('nis')
        import_id_fields = ('nis',)
        exclude = ('ID')