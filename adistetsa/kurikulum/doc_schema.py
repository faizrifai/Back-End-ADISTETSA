from typing_extensions import Required
from drf_yasg import openapi

schema_ktsp = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'TAHUN_AJARAN': openapi.Schema(type=openapi.TYPE_INTEGER),
        'NAMA_FILE': openapi.Schema(type=openapi.TYPE_FILE),
    }
)

param_importexportfile = openapi.Parameter(
    name="NAMA_FILE",
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    required=True,
    description="Document"
)
param_tahunajaran = openapi.Parameter(
    name="TAHUN_AJARAN",
    in_=openapi.IN_FORM,
    type=openapi.TYPE_INTEGER,
    required=True,
    description="Document"
)