import datetime

import tablib
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from utility.permissions import HasGroupPermissionAny, IsSuperAdmin

from .doc_schema import *
from .importexportresources import *
from .models import *


class ImportDataTataTertibView(APIView):
    """
    post: Melakukan import data tata tertib (Super Admin/ Staf Kurikulum).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "POST": ["Staf Kurikulum"],
    }
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        manual_parameters=[
            param_importexportfile,
        ],
        responses={
            "200": "Berhasil mengupdate data tata tertib",
            "400": "Gagal mengupdate data, ada kesalahan",
        },
    )
    def post(self, request, format=None):
        file = request.FILES["file"]

        str_text = ""
        for line in file:
            str_text = str_text + line.decode()

        data_tata_tertib_resource = TataTertibResource()
        csv_data = tablib.import_set(str_text, format="csv")
        print(csv_data)

        try:
            result = data_tata_tertib_resource.import_data(
                csv_data, dry_run=True, raise_errors=True
            )

            if not result.has_errors():
                data_tata_tertib_resource.import_data(csv_data, dry_run=False)

                return Response(
                    {"Result": "Berhasil mengupdate data tata tertib"}, status=200
                )
        except Exception as e:
            return Response({"Result": str(e)}, status=400)

        return Response(
            {"Result": "Gagal mengupdate data tata tertib, ada kesalahan"}, status=400
        )


class ExportDataTataTertibView(APIView):
    """
    get: Melakukan export data tata tertib (Super Admin/ Staf PPDB).
    """

    permission_classes = [IsSuperAdmin | HasGroupPermissionAny]
    required_groups = {
        "GET": ["Staf Kurikulum"],
    }

    def get(self, request, format=None):
        data_tata_tertib_resource = TataTertibResource()
        try:
            dataset = data_tata_tertib_resource.export()
            today = datetime.date.today()
            filename = "data_tata_tertib-" + str(today) + ".csv"
            response = HttpResponse(dataset.csv, content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="%s"' % (filename)

            return response
        except Exception as e:
            return Response({"Result": str(e)}, status=400)
