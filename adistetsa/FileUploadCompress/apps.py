from django.apps import AppConfig

from . import getter
from . import register_signals
from .list_app import apps_to_compress


class FileuploadcompressConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FileUploadCompress"

    def ready(self):
        getter.start(apps_to_compress)
        register_signals.register()
