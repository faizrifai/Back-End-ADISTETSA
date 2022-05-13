from django.apps import apps
from django.core.files.base import ContentFile
from django.forms import ValidationError

import os, io, zipfile

def duplikat_file(obj, file, nama_file):
    file_baru = ContentFile(file)
    split_name = nama_file.split('/')
    ekstensi = split_name[1].split('.')
    file_baru.name = 'riwayat_' + str(obj.ID) + '.' + ekstensi[-1]
    
    return file_baru

def hapus_kunci_kosong(arr):
    for k, v in list(arr.items()):
        if v is None:
            del arr[k]
            
def gabung_dictionary(*parameters):
    temp = None
    
    for dict in parameters:
        if not temp:
            temp = dict
        else:
            temp = temp | dict

    return temp

def validasi_keuangan(value):
    test_value = int(value)
    if test_value < 0 :
        raise ValidationError(str(value) + ' Tidak boleh kurang dari 0')

def validasi_integer(value):
    try:
        tes_int = int(value)
    except:
        raise ValidationError(str(value) + ' bukan angka')
    
def paksa_huruf_besar(value):
    tes_value = str(value)
    
    if any(i.isdigit() for i in tes_value):
        raise ValidationError(str(value) + ' tidak boleh ada angka')
    
    if not tes_value.isupper():
        raise ValidationError(str(value) + ' harus huruf besar ')
    
def cek_huruf_besar_awal_kalimat(value):
    tes_value = str(value)
    
    if any(i.isdigit() for i in tes_value):
        raise ValidationError(str(value) + ' tidak boleh ada angka')
    
    if not tes_value.istitle():
        raise ValidationError(str(value) + ' harus huruf besar setiap awal kata')

def wajib_diisi(value, kondisi, self, fields):
    validator_arr = {}
    
    if value == kondisi:
        for field in fields:
            field_value = getattr(self, field)
            if not field_value:
                # print(field + ' wajib diisi')
                validator_arr[field] = field + ' wajib diisi'
  
    return validator_arr
    
def paksa_huruf_besar_dengan_angka(value):
    tes_value = str(value)
    
    if not tes_value.isupper():
        raise ValidationError(str(value) + ' harus huruf besar ')       
    
def cek_error_import(model_name, row_object, row_name, field_name):
    validator_arr = {}
    
    data = {
        field_name: row_object[row_name]
    }
    
    try:
        tes = model_name.objects.get(**data)
    except model_name.DoesNotExist:
        validator_arr[row_name] = 'Data tidak sesuai atau tidak ada di database'
        
    return validator_arr

def get_project_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(current_dir)

def get_file_to_zip(app_name, queryset):
    file_to_zip = []

    model_name = apps.get_model(app_name, queryset.model.__name__)
    file_fields = [f.name for f in model_name._meta.get_fields() if f.get_internal_type() == 'FileField']

    for data in queryset:
        for field in file_fields:
            field_data = getattr(data, field)
            exists = field_data.storage.exists(field_data.name)
            file_path = field_data.path
            
            if exists:
                file_to_zip.append(file_path)

    return file_to_zip

def zip_file(file_to_zip):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file in file_to_zip:
            splitted = file.split(os.sep)
            file_name = splitted[-2] + '/' + splitted[-1]
            zip_file.write(file, file_name)

    return zip_buffer