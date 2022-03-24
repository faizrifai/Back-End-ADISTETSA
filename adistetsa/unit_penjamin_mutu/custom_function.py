from heapq import merge
import pandas as pd
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models import Count
from kurikulum.models import JadwalMengajar, OfferingKelas, KelasSiswa, Kelas
from dataprofil.models import DataRiwayatKepangkatanGuru
from adistetsa.custom_function import gabung_dictionary
import openpyxl

import time

def value_in_list_of_dict(key, value, d):
    for data in d:
        if data[key] == value:
            return True
        
    return False

def multiple_value_exist(v: dict, d: dict):
    keys = v.keys()
    for data in d:
        kebenaran = True
        for key in keys:
            value = v[key]
        
            if data[key] == value:
                kebenaran = kebenaran and True
            else:
                kebenaran = kebenaran and False
                
        if kebenaran:
            return True
            
    return False


def get_column(df, column_name):
    col_no = chr(65 + df.columns.get_loc(column_name))
    col_no = col_no + ':' + col_no
    
    return col_no

def get_columns_from_worksheet(ws):
  return {
      cell.value: {
          'letter': openpyxl.utils.get_column_letter(cell.column),
          'number': cell.column - 1
      } for cell in ws[1] if cell.value
  }

def apply_style_to_cell(worksheet, width, font, border):
    column_letter = tuple(openpyxl.utils.get_column_letter(col_number + 1) for col_number in range(worksheet.max_column))
    for letter in column_letter:
        worksheet.column_dimensions[letter].width = width
        for cell in worksheet[letter + ':' + letter]:
            cell.font = font
            cell.border = border
            
def merge_cell(worksheet, dataframe, col_name, col_merge):
    col = get_columns_from_worksheet(worksheet)
    col_dif = col[col_merge]['number'] + 1
    
    for car in dataframe[col_name].unique():
        # find indices and add one to account for header
        u=dataframe.loc[dataframe[col_name]==car].index.values + 1

        if len(u) < 2:
            pass # do not merge cells if there is only one car name
        else:
            worksheet.merge_cells(start_row=u[0] + 1, start_column=col_dif, end_row=u[-1] + 1, end_column=col_dif)
            
def cari_pangkat(self):
    pangkat = DataRiwayatKepangkatanGuru.objects.all()
    for data in pangkat:
        if self == data.OWNER:
            return str(data.PANGKAT_GOLONGAN)
        
    return '-'

def buat_file_prototype(self, count):
    if self.KATEGORI == 'Pembagian Jadwal Mengajar':
        # check execution time -- start
        start = time.time()

        kelas = OfferingKelas.objects.all().order_by('KELAS__TINGKATAN', '-KELAS__JURUSAN__NAMA', 'OFFERING')
        jadwal = JadwalMengajar.objects.all().filter(TAHUN_AJARAN=self.TAHUN_AJARAN, SEMESTER = self.SEMESTER).order_by('GURU').annotate(JUMLAH=Count('WAKTU_PELAJARAN'))
        kelas_siswa = KelasSiswa.objects.all().filter(KELAS__KELAS__TAHUN_AJARAN = self.TAHUN_AJARAN)
        
        guru = []
        for data in jadwal:
            exist = multiple_value_exist({
                'GURU': data.GURU.NAMA_LENGKAP,
                'MATA_PELAJARAN': str(data.MATA_PELAJARAN)
            }, guru)

            if not (exist):
                guru.append({
                    'GURU': data.GURU.NAMA_LENGKAP,
                    'MATA_PELAJARAN': str(data.MATA_PELAJARAN)
                })

        jumlah = {}

        for data in kelas:
            jumlah[str(data)] = ''
        
        jumlah['JUMLAH_JAM_ATAU_RASIO'] = 0
        jumlah['JAM_TAMBAHAN'] = ''
        jumlah['TOTAL_JAM'] = 0
        jumlah['TUGAS_TAMBAHAN'] = ''
        
        # pembagian jadwal mengajar
        jumlah_keseluruhan = []
        for g in guru:
            if not any(d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'] for d in jumlah_keseluruhan):
                data_baru = g
                data_baru = gabung_dictionary(data_baru, jumlah)
            else:
                data_baru = next(d for d in jumlah_keseluruhan if d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'])

            for data in jadwal:
                if data.GURU.NAMA_LENGKAP == g['GURU'] and str(data.MATA_PELAJARAN) == g['MATA_PELAJARAN']:
                    data_baru['JUMLAH_JAM_ATAU_RASIO'] += data.JUMLAH
    
                    if data_baru[str(data.KELAS)] == '':
                        data_baru[str(data.KELAS)] = data.JUMLAH
                    else:
                        data_baru[str(data.KELAS)] += data.JUMLAH
                        
                if data.GURU.NAMA_LENGKAP == g['GURU']:
                    data_baru['TOTAL_JAM'] += data.JUMLAH

            if not any(d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'] for d in jumlah_keseluruhan):
                jumlah_keseluruhan.append(data_baru)
    
    
        # total kelas
        jumlah_siswa = {}
        for data in kelas:
            jumlah = kelas_siswa.filter(KELAS = data).count()    
            jumlah_siswa[str(data)] = jumlah
            
        
        # for data in kelas:
        #     jumlah_siswa[str(data.KELAS.TINGKATAN)] = kelas_siswa.filter(KELAS__KELAS__TINGKATAN = data.KELAS.TINGKATAN).count()
        
        jumlah_total = []
        jumlah_total.append(jumlah_siswa)
        
        
        df_ = pd.DataFrame(jumlah_keseluruhan)
        df = pd.DataFrame(jumlah_keseluruhan).set_index(['GURU', 'MATA_PELAJARAN'])
        dt = pd.DataFrame(jumlah_total)
        
        b = BytesIO()
        writer = pd.ExcelWriter(b, engine='openpyxl')
        
        df.to_excel(writer, sheet_name=self.KATEGORI, index=True, )
        dt.to_excel(writer, sheet_name='TOTAL_JUMLAH', index=False,)
        
        worksheet = writer.sheets[self.KATEGORI]
        worksheet2 = writer.sheets['TOTAL_JUMLAH']
        
        # col = get_columns_from_worksheet(worksheet)
        # total_jam = col['TOTAL_JAM']['number'] + 1
        
        # for car in df_['GURU'].unique():
        #     # find indices and add one to account for header
        #     u=df_.loc[df_['GURU']==car].index.values + 1

        #     if len(u) < 2:
        #         pass # do not merge cells if there is only one car name
        #     else:
        #         worksheet.merge_cells(start_row=u[0] + 1, start_column=total_jam, end_row=u[-1] + 1, end_column=total_jam)
        
        merge_cell(worksheet, df_, 'GURU', 'TOTAL_JAM')
                
        wb_obj = openpyxl.load_workbook(self.TEMPLATE.path)
        sheet_obj = wb_obj.active
        
        start_row = self.START_ROW - 2
        start_col = self.START_COL - 1
        
        kelas_row = start_row - 2
        kelas_col = start_col + 2
        
        mr = worksheet.max_row + 1
        mc = worksheet.max_column + 1
        
        mr2 = worksheet2.max_row + 1
        mc2 = worksheet2.max_column + 1
        
        no = 1
        
        for i in range (2, mr ):
            for j in range (1, mc ):
                # reading cell value from source excel file
                c = worksheet.cell(row = i, column = j)

                # writing the read value to destination excel file
                cell = sheet_obj.cell(row = i + start_row, column = start_col + j)
                cell.value = c.value
                
                if c.value != None and j == 1:
                    cell = sheet_obj.cell(row = i + kelas_row + 2, column = 1)
                    cell.value = no
                    no += 1
                
        for i in range (2, mr2 ):
            for j in range (1, mc2 ):
                # reading cell value from source excel file
                c = worksheet2.cell(row = i, column = j)

                # writing the read value to destination excel file
                cell = sheet_obj.cell(row = i + kelas_row, column = kelas_col + j)
                cell.value = c.value
                    
        virtual_workbook = BytesIO()
        wb_obj.save(virtual_workbook)
        self.FILE_HASIL = ContentFile(virtual_workbook.getvalue(), self.KATEGORI + '.xlsx')
        
        writer.save()
    
    elif self.KATEGORI == 'Rekapitulasi Jumlah Jam Mengajar':
        kelas_tingkatan = Kelas.objects.all().order_by('TINGKATAN',)
        jadwal = JadwalMengajar.objects.all().filter(TAHUN_AJARAN=self.TAHUN_AJARAN, SEMESTER = self.SEMESTER).order_by('GURU').annotate(JUMLAH=Count('WAKTU_PELAJARAN'))
        kelas_siswa = KelasSiswa.objects.all().filter(KELAS__KELAS__TAHUN_AJARAN = self.TAHUN_AJARAN)
        
        guru = []
        for data in jadwal:
            exist = multiple_value_exist({
                'GURU': data.GURU.NAMA_LENGKAP,
                'MATA_PELAJARAN': str(data.MATA_PELAJARAN)
            }, guru)
            
            if not (exist):
                guru.append({
                    'GURU': data.GURU.NAMA_LENGKAP,
                    'NIP': data.GURU.NIP,
                    'PANGKAT': data.GURU.PANGKAT,
                    'GOL': cari_pangkat(data.GURU),
                    'MATA_PELAJARAN': str(data.MATA_PELAJARAN)
                })
                
        jumlah = {}
        
        for data in kelas_tingkatan:
            jumlah[str(data.TINGKATAN)] = 0

        jumlah_keseluruhan = []
        for g in guru:
            if not any(d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'] for d in jumlah_keseluruhan):
                data_baru = g
                data_baru = gabung_dictionary(data_baru, jumlah)
            else:
                data_baru = next(d for d in jumlah_keseluruhan if d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'])

            for data in jadwal:
                if data.GURU.NAMA_LENGKAP == g['GURU'] and str(data.MATA_PELAJARAN) == g['MATA_PELAJARAN']:
                    tingkatan = data.KELAS.KELAS.TINGKATAN
                    data_baru[tingkatan] += data.JUMLAH

            if not any(d['GURU'] == g['GURU'] and d['MATA_PELAJARAN'] == g['MATA_PELAJARAN'] for d in jumlah_keseluruhan):
                jumlah_keseluruhan.append(data_baru)
    
        df = pd.DataFrame(jumlah_keseluruhan)
        df_ = pd.DataFrame(jumlah_keseluruhan).set_index(['GURU', 'NIP',])
        b = BytesIO()
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df_.to_excel(writer, sheet_name=self.KATEGORI, index=True, )
        print(df_)
        
        worksheet = writer.sheets[self.KATEGORI]
        merge_cell(worksheet, df, 'GURU', 'NIP')
        merge_cell(worksheet, df, 'GURU', 'PANGKAT')
        merge_cell(worksheet, df, 'GURU', 'GOL')
        
        wb_obj = openpyxl.load_workbook(self.TEMPLATE.path)
        sheet_obj = wb_obj.active
        
        start_row = self.START_ROW - 2
        start_col = self.START_COL - 1
        
        no_row = start_row - 2
        no_col = start_col + 2
        
        mr = worksheet.max_row + 1
        mc = worksheet.max_column + 1
        
        no = 1
        
        for i in range (2, mr ):
            for j in range (1, mc ):
                # reading cell value from source excel file
                c = worksheet.cell(row = i, column = j)

                # writing the read value to destination excel file
                cell = sheet_obj.cell(row = i + start_row, column = start_col + j)
                cell.value = c.value
                
                if c.value != None and j == 1:
                    cell = sheet_obj.cell(row = i + no_row + 2, column = 1)
                    cell.value = no
                    no += 1
        
        virtual_workbook = BytesIO()
        wb_obj.save(virtual_workbook)
        self.FILE_HASIL = ContentFile(virtual_workbook.getvalue(), self.KATEGORI + '.xlsx')
        
        
        writer.save()
    
    elif self.KATEGORI == 'Pembagian Tugas BK Semester':
        pembagian_tugas = count
        kelas_tingkatan = OfferingKelas.objects.all().order_by('KELAS__TINGKATAN',)
        kelas_siswa = KelasSiswa.objects.all().filter(KELAS__KELAS__TAHUN_AJARAN = self.TAHUN_AJARAN)
        
        
        guru = []
        for data in pembagian_tugas:
            exist = multiple_value_exist({
                'NAMA/NIP/JABATAN': data.DATA_GURU.NAMA_LENGKAP + ',' + data.DATA_GURU.NIP
            }, guru)
            
            if not (exist):
                guru.append({
                    'NAMA/NIP/JABATAN': data.DATA_GURU.NAMA_LENGKAP + ',' + data.DATA_GURU.NIP,
                    'PANGKAT_GOLONGAN': data.DATA_GURU.PANGKAT + ',' + str(cari_pangkat(data.DATA_GURU)),
                })
        
                
        jumlah = {}
        
        
        jumlah_keseluruhan = []
        for g in guru:
            if not any(d['NAMA/NIP/JABATAN'] == g['NAMA/NIP/JABATAN'] for d in jumlah_keseluruhan):
                data_baru = g
                data_baru = gabung_dictionary(data_baru, jumlah)
            else:
                data_baru = next(d for d in jumlah_keseluruhan if d['NAMA/NIP/JABATAN'] == g['NAMA/NIP/JABATAN'])

            list_kelas_x =  []
            list_kelas_xi =  []
            list_kelas_xii =  []
            
            jumlah_kelas_x = []
            jumlah_kelas_xi = []
            jumlah_kelas_xii = []
            for data in pembagian_tugas:
                for data_kelas in data.DATA_KELAS.all():
                    if data_kelas.KELAS.TINGKATAN == 'X' :
                        list_kelas_x.append(data_kelas)
                        jumlah_kelas_x.append(kelas_siswa.filter(KELAS = data_kelas).count())   
                    elif data_kelas.KELAS.TINGKATAN == 'XI' :
                        list_kelas_xi.append(data_kelas)               
                        jumlah_kelas_xi.append(kelas_siswa.filter(KELAS = data_kelas).count())
                    elif data_kelas.KELAS.TINGKATAN == 'XII' :
                        list_kelas_xii.append(data_kelas)               
                        jumlah_kelas_xii.append(kelas_siswa.filter(KELAS = data_kelas).count())
                    # jumlah[str(data)]  = kelas_siswa.filter(KELAS = data_kelas,).count()

            data_baru['KELAS_X'] = str(list_kelas_x) 
            data_baru['JUMLAH_KELAS_X'] = str(jumlah_kelas_x)
            data_baru['KELAS_XI'] = str(list_kelas_xi)
            data_baru['JUMLAH_KELAS_XI'] = str(jumlah_kelas_xi)
            data_baru['KELAS_XII'] = str(list_kelas_xii)
            data_baru['JUMLAH_KELAS_XII'] = (jumlah_kelas_xii)
            
            data_baru['KETERANGAN'] = data.KETERANGAN_TUGAS
            if not any(d['NAMA/NIP/JABATAN'] == g['NAMA/NIP/JABATAN'] for d in jumlah_keseluruhan):
                jumlah_keseluruhan.append(data_baru)
                print('merdeka')
        
        
        df = pd.DataFrame(jumlah_keseluruhan)
        df_ = pd.DataFrame(jumlah_keseluruhan)
        b = BytesIO()
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df_.to_excel(writer, sheet_name=self.KATEGORI, index=True, )
        worksheet = writer.sheets[self.KATEGORI]
        print('worksheet')
        print(df_)
        writer.save()

    elif self.KATEGORI == 'Pembagian Tugas Pokok dan Tambahan Tenaga Kependidikan':
        pembagian_tugas_tendik = count
        
        print ('Wew')
        guru = []
        
        for data in pembagian_tugas_tendik:
            exist = multiple_value_exist({
                'NAMA': data.DATA_GURU.NAMA_LENGKAP,
            }, guru)
            print ('guru ; ' + str(data.DATA_GURU.NAMA_LENGKAP))
            
        
            if not (exist):
                guru.append({
                    'NAMA': data.DATA_GURU.NAMA_LENGKAP,
                    'NIP': data.DATA_GURU.NIP,
                    'GOL' : cari_pangkat(data),
                    'PANGKAT' : data.DATA_GURU.PANGKAT,
                    'TUGAS_POKOK' : data.TUGAS_POKOK.JENIS_TUGAS,
                    'TUGAS_TAMBAHAN' : data.TUGAS_TAMBAHAN,
                })
        
        jumlah = {}
        jumlah_keseluruhan = []
        
        for g in guru:
            if not any(d['NAMA'] == g['NAMA'] for d in jumlah_keseluruhan):
                data_baru = g
                data_baru = gabung_dictionary(data_baru)
            else:
                data_baru = next(d for d in jumlah_keseluruhan if d['NAMA'] == g['NAMA'])
                    
            if not any(d['NAMA'] == g['NAMA']  for d in jumlah_keseluruhan):
                jumlah_keseluruhan.append(data_baru)
                
        
                
        df = pd.DataFrame(guru)
        b = BytesIO()
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, sheet_name='TUGAS_TAMBAHAN', index=False, )
        print('df :' + str(df))
        print ('Tes Darah')
        writer.save()
        print ('Tes Merdeka')
        self.FILE_HASIL = ContentFile(b.getvalue(), 'TEST' + '.xlsx')
                        
        
    # # check execution time -- finish
    # print('Waktu Eksekusi: ' + str(time.time() - start))
    
    return ContentFile(b.getvalue(), self.KATEGORI + '.xlsx')


