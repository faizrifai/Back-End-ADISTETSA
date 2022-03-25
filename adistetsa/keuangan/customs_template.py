from io import  BytesIO
from django.core.files.base import ContentFile
import openpyxl

def buat_kuitansi(self): 
   wb_obj = openpyxl.load_workbook(self.TEMPLATE.path)
   sheet_obj = wb_obj.active
   nama_cell =  sheet_obj.cell(row = 8, column= 4)
   nama_cell.value = self.NAMA_SISWA.NIS.NAMA
   kelas_cell =  sheet_obj.cell(row = 9, column= 4)
   kelas_cell.value = str(self.NAMA_SISWA.KELAS)
   nama_cell =  sheet_obj.cell(row = 10, column= 4)
   nama_cell.value = self.NAMA_SISWA.NIS.NIS
   if self.JENIS_PEMBAYARAN == 'SPP' :
      jenis_pembayaran_cell =  sheet_obj.cell(row = 11, column= 3)
      jenis_pembayaran_cell.value = 'X'  
   elif self.JENIS_PEMBAYARAN == 'Dana Peran Serta Masyarakat Rutin' :
      jenis_pembayaran_cell =  sheet_obj.cell(row = 12, column= 3)
      jenis_pembayaran_cell.value = 'X'
   elif self.JENIS_PEMBAYARAN == 'Dana Peran Serta Masyarakat Insindental' :
      jenis_pembayaran_cell =  sheet_obj.cell(row = 13, column= 3)
      jenis_pembayaran_cell.value = 'X'
   elif self.JENIS_PEMBAYARAN == 'Bimbel' :
      jenis_pembayaran_cell =  sheet_obj.cell(row = 14, column= 3)
      jenis_pembayaran_cell.value = 'X'
   bulan = self.PEMBAYARAN_BULAN.split(',')
   print (len(bulan))
   for i in range(len(bulan)):
      cur = bulan[i-1].strip()
      print(cur)
      if cur in 'Januari':
         bulan_cell =  sheet_obj.cell(row = 6, column= 8)
         bulan_cell.value = 'X'
      elif cur in 'Februari' :
         bulan_cell =  sheet_obj.cell(row = 7, column= 8)
         bulan_cell.value = 'X'
      elif cur in 'Maret':
         bulan_cell =  sheet_obj.cell(row = 8, column= 8)
         bulan_cell.value = 'X'
      elif cur in 'April':
         bulan_cell =  sheet_obj.cell(row = 9, column= 8)
         bulan_cell.value = 'X'
      elif cur in 'Mei':
         bulan_cell =  sheet_obj.cell(row = 10, column= 8)
         bulan_cell.value = 'X'   
      elif cur in 'Juni':
         bulan_cell =  sheet_obj.cell(row = 10, column= 8)
         bulan_cell.value = 'X'   
      elif cur in 'Juli':
         bulan_cell =  sheet_obj.cell(row = 6, column= 6)
         bulan_cell.value = 'X'
      elif cur in 'Agustus':
         bulan_cell =  sheet_obj.cell(row = 7, column= 6)
         bulan_cell.value = 'X'
      elif cur in 'September':
         bulan_cell =  sheet_obj.cell(row = 8, column= 6)
         bulan_cell.value = 'X'
      elif cur in 'Oktober':
         bulan_cell =  sheet_obj.cell(row = 9, column= 6)
         bulan_cell.value = 'X'
      elif cur in 'November':
         bulan_cell =  sheet_obj.cell(row = 10, column= 6)
         bulan_cell.value = 'X'   
      elif cur in 'Desember':
         bulan_cell =  sheet_obj.cell(row = 11, column= 6)
         bulan_cell.value = 'X'
   nominal_cell =  sheet_obj.cell(row = 15, column= 4)
   nominal_cell.value = 'Rp. ' + str(self.NOMINAL_PEMBAYARAN) 
   virtual_workbook = BytesIO()
   wb_obj.save(virtual_workbook)
   
   return ContentFile(virtual_workbook.getvalue(), 'kuitansi' + '.xlsx')
        
   
