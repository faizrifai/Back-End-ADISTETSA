from collections import defaultdict

from django.apps import apps
from django.db import models

# storage


def default_set():
    return set()


model_and_fields = defaultdict(default_set)


def get_storage():
    return model_and_fields


# handler


def start(app_list: list):
    if model_and_fields:
        return

    if not app_list:
        return

    for app_label in app_list:
        models = get_all_model_from_app(app_label)

        for model_name in models:
            name = "{}.{}".format(app_label, model_name)
            store_file_field_from_model(name)


# utility function


def get_all_models():
    for model_name in model_and_fields:
        yield apps.get_model(model_name)


def get_all_model_from_app(app_label: str):
    models = apps.all_models[app_label]

    return dict(models).keys()


def get_fields_from_model(model_name: str, exclude=None):
    exist = model_name in model_and_fields

    if exist:
        fields = model_and_fields[model_name]

        if exclude is not None:
            assert isinstance(exclude, set)
            fields = fields.difference(exclude)

        for field_name in fields:
            yield field_name


def fields_for_model_instance(instance, using=None):
    if using is None:
        using = instance

    model_name = get_model_name(instance)
    deferred_fields = instance.get_deferred_fields()

    for field_name in get_fields_from_model(model_name, exclude=deferred_fields):
        fieldfile = getattr(instance, field_name, None)
        yield field_name, fieldfile.__class__(using, fieldfile.field, fieldfile.name)


def get_model_name(instance):
    return "{opt.app_label}.{opt.model_name}".format(opt=instance._meta)


def store_file_field_from_model(model_name: str):
    model = apps.get_model(model_name)
    opts = model._meta

    for field in opts.get_fields():
        if isinstance(field, models.FileField):
            store_model_and_field(model_name, field.name)


def store_model_and_field(model_name: str, field_name: str):
    model_and_fields[model_name].add(field_name)
