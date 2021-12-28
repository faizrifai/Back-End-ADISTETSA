from django.contrib import admin

from .models import *

# Register your models here.
class DataSiswaUserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['NISN', ]

admin.site.register(DataSiswaUser, DataSiswaUserAdmin)