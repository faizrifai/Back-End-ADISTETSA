from cgi import test
import string
from django.core.files.base import ContentFile
from django.forms import ValidationError

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
    except Exception as e:
        validator_arr[row_name] = 'Data tidak sesuai atau tidak ada di database'
        
    return validator_arr