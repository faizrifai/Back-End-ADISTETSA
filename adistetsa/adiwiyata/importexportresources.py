from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import DataSiswa, DaftarKader


class DaftarKaderResource(resources.ModelResource):

    nis = Field(
        column_name="NIS", attribute="NIS", widget=ForeignKeyWidget(DataSiswa, "NIS")
    )

    class Meta:
        model = DaftarKader
        fields = "nis"
        import_id_fields = ("nis",)
        exclude = "ID"
