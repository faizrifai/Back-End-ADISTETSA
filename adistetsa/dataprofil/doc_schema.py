from typing_extensions import Required
from drf_yasg import openapi

schema_datakompetensiguru = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'BIDANG_STUDI': openapi.Schema(type=openapi.TYPE_STRING),
        'URUTAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)