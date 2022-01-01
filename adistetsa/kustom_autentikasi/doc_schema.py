from typing_extensions import Required
from drf_yasg import openapi

param_importexportfile = openapi.Parameter(
    name="file",
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    required=True,
    description="Document"
)