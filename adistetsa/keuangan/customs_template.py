from io import  BytesIO
from django.core.files.base import ContentFile
import openpyxl

def buat_kuitansi(self): 
    
   pembayaran = {}
   pembayaran['NAMA_SISWA'] = self.DATA_SISWA.NAMA_LENGKAP
   pembayaran['KELAS']  