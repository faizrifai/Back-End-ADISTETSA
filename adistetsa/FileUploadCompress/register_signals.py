import filetype
import logging

from PIL import Image, UnidentifiedImageError
from django.db.models.signals import post_save

from . import getter

logger = logging.getLogger(__name__)


def compress_post_save(sender, instance, raw, **kwargs):
    if raw:
        return

    for field_name, new_file in getter.fields_for_model_instance(instance):
        if new_file:
            extension = get_image_file_extension(new_file.path)

            if extension:
                compress_image(new_file.path)


def compress_image(filename: str):
    print("compressing image...")
    try:
        img = Image.open(filename)
    except UnidentifiedImageError:
        return

    img = img.convert("RGB")
    img.save(filename, "JPEG", optimize=True, quality=30)


def get_image_file_extension(filename: str):
    kind = filetype.guess(filename)

    if kind is None:
        return None

    if not filetype.is_image(filename):
        return None

    return kind.extension


def register():
    for model in getter.get_all_models():
        key = "{{}}_compress_signal_{}".format(getter.get_model_name(model))
        post_save.connect(
            compress_post_save, sender=model, dispatch_uid=key.format("post_save")
        )
