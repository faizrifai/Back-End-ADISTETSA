from io import BytesIO
from django.core.files.base import ContentFile
from fpdf import FPDF

import os

current_folder = os.path.dirname(os.path.abspath(__file__))


def buat_kuitansi(self):
    # wb_obj = openpyxl.load_workbook(self.TEMPLATE.path)
    # sheet_obj = wb_obj.active
    # nama_cell =  sheet_obj.cell(row = 8, column= 4)
    # nama_cell.value = self.NAMA_SISWA.NIS.NAMA
    # kelas_cell =  sheet_obj.cell(row = 9, column= 4)
    # kelas_cell.value = str(self.NAMA_SISWA.KELAS)
    # nama_cell =  sheet_obj.cell(row = 10, column= 4)
    # nama_cell.value = self.NAMA_SISWA.NIS.NIS
    # total_pembayaran = 0

    # print ('test' + self.PEMBAYARAN_DPSM_INSINDENTAL)

    # if self.NOMINAL_SPP != '' :
    #    bulan = self.PEMBAYARAN_SPP.split(',')
    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 11, column= 3)
    #    jenis_pembayaran_cell.value = 'X'
    #    total_pembayaran += (len(bulan)*int(self.NOMINAL_SPP))
    #    print (len(bulan))
    #    for i in range(len(bulan)):
    #       cur = bulan[i-1].strip()
    #       print(cur)
    #       if cur in 'Januari':
    #          bulan_cell =  sheet_obj.cell(row = 6, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Februari' :
    #          bulan_cell =  sheet_obj.cell(row = 7, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Maret':
    #          bulan_cell =  sheet_obj.cell(row = 8, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'April':
    #          bulan_cell =  sheet_obj.cell(row = 9, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Mei':
    #          bulan_cell =  sheet_obj.cell(row = 10, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Juni':
    #          bulan_cell =  sheet_obj.cell(row = 10, column= 8)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Juli':
    #          bulan_cell =  sheet_obj.cell(row = 6, column= 6)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Agustus':
    #          bulan_cell =  sheet_obj.cell(row = 7, column= 6)
    #          bulan_cell.value = 'X'
    #       elif cur in 'September':
    #          bulan_cell =  sheet_obj.cell(row = 8, column= 6)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Oktober':
    #          bulan_cell =  sheet_obj.cell(row = 9, column= 6)
    #          bulan_cell.value = 'X'
    #       elif cur in 'November':
    #          bulan_cell =  sheet_obj.cell(row = 10, column= 6)
    #          bulan_cell.value = 'X'
    #       elif cur in 'Desember':
    #          bulan_cell =  sheet_obj.cell(row = 11, column= 6)
    #          bulan_cell.value = 'X'

    # if self.PEMBAYARAN_DPSM_RUTIN != '' :
    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 12, column= 3)
    #    jenis_pembayaran_cell.value = 'X'
    #    total_pembayaran += int(float(self.PEMBAYARAN_DPSM_RUTIN))

    # if self.PEMBAYARAN_DPSM_INSINDENTAL != 0 :
    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 13, column= 3)
    #    jenis_pembayaran_cell.value = 'X'
    #    value = self.PEMBAYARAN_DPSM_INSINDENTAL
    #    print (value)
    #    total_pembayaran += int(value)

    # elif self.BIMBEL != 0 :
    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 14, column= 3)
    #    jenis_pembayaran_cell.value = 'X'
    #    total_pembayaran += int(self.BIMBEL)

    # nominal_cell =  sheet_obj.cell(row = 15, column= 4)
    # nominal_cell.value = 'Rp. ' + str(total_pembayaran)
    # virtual_workbook = BytesIO()
    # wb_obj.save(virtual_workbook)

    # Awal Program
    DPSMR = ""
    DPSMI = ""
    BIMBEL = ""

    NILAI_SPP = ""

    JANUARI = ""
    FEBRUARI = ""
    MARET = ""
    APRIL = ""
    MEI = ""
    JUNI = ""
    JULI = ""
    AGUSTUS = ""
    SEPTEMBER = ""
    OKTOBER = ""
    NOVEMBER = ""
    DESEMBER = ""

    JANUARI1 = ""
    FEBRUARI1 = ""
    MARET1 = ""
    APRIL1 = ""
    MEI1 = ""
    JUNI1 = ""
    JULI1 = ""
    AGUSTUS1 = ""
    SEPTEMBER1 = ""
    OKTOBER1 = ""
    NOVEMBER1 = ""
    DESEMBER1 = ""
    NOMINAL_DPSMI = ""
    NOMINAL_DPSMR = ""
    NOMINAL_BIMBEL = ""
    total_pembayaran = 0

    if int(self.PEMBAYARAN_DPSM_RUTIN) > 0:
        bulan = self.BULAN_PEMBAYARAN_DPSM_RUTIN.split(",")
        DPSMR = "X"
        total_pembayaran += len(bulan) * int(self.PEMBAYARAN_DPSM_RUTIN)
        NOMINAL_DPSMR = "Rp. " + str((len(bulan) * int(self.PEMBAYARAN_DPSM_RUTIN)))
        for i in range(len(bulan)):
            cur = bulan[i - 1].strip()

            if cur in "Januari":
                JANUARI = "X"
            elif cur in "Februari":
                FEBRUARI = "X"
            elif cur in "Maret":
                MARET = "X"
            elif cur in "April":
                APRIL = "X"
            elif cur in "Mei":
                MEI = ""
            elif cur in "Juni":
                JUNI = "X"
            elif cur in "Juli":
                JULI = "X"
            elif cur in "Agustus":
                AGUSTUS = "X"
            elif cur in "September":
                SEPTEMBER = "X"
            elif cur in "Oktober":
                OKTOBER = "X"
            elif cur in "November":
                NOVEMBER = "X"
            elif cur in "Desember":
                DESEMBER = "X"

    if int(self.PEMBAYARAN_DPSM_INSINDENTAL) > 0:
        DPSMI = "X"
        value = self.PEMBAYARAN_DPSM_INSINDENTAL
        NOMINAL_DPSMI = "Rp. " + str(value)
        total_pembayaran += int(value)

    if int(self.BIMBEL) > 0:
        bulan1 = self.BULAN_PEMBAYARAN_BIMBEL.split(",")
        BIMBEL = "X"
        total_pembayaran += len(bulan1) * int(self.BIMBEL)
        NOMINAL_BIMBEL = len(bulan1) * int(self.BIMBEL)
        for i in range(len(bulan1)):
            cur = bulan1[i - 1].strip()
            print(cur)
            if cur in "Januari":
                JANUARI1 = "X"
            elif cur in "Februari":
                FEBRUARI1 = "X"
            elif cur in "Maret":
                MARET1 = "X"
            elif cur in "April":
                APRIL1 = "X"
            elif cur in "Mei":
                MEI1 = ""
            elif cur in "Juni":
                JUNI1 = "X"
            elif cur in "Juli":
                JULI1 = "X"
            elif cur in "Agustus":
                AGUSTUS1 = "X"
            elif cur in "September":
                SEPTEMBER1 = "X"
            elif cur in "Oktober":
                OKTOBER1 = "X"
            elif cur in "November":
                NOVEMBER1 = "X"
            elif cur in "Desember":
                DESEMBER1 = "X"

    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf

    pdf.set_font("Times", size=15)
    # create a cell
    # pdf.cell(200, 10, )
    pdf.image(
        os.path.join(current_folder, "bahan_kuitansi/Logo.png"),
        x=None,
        y=None,
        w=190,
        h=35,
        type="",
        link="",
    )
    pdf.cell(200, 12, txt="KUITANSI PEMBAYARAN", ln=1, align="C")
    pdf.line(10, 55, 200, 55)
    pdf.line(10, 56, 200, 56)
    pdf.set_font("Times", size=12)
    # add another cell
    pdf.cell(
        200, 7, txt=str("NAMA SISWA    : " + self.NAMA_SISWA.NIS.NAMA), ln=2, align="L"
    )
    pdf.cell(
        200,
        7,
        txt=str("KELAS                 : " + str(self.NAMA_SISWA.KELAS)),
        ln=2,
        align="L",
    )
    pdf.cell(
        200,
        7,
        txt=str("NOMOR INDUK : " + str(self.NAMA_SISWA.NIS.NIS)),
        ln=2,
        align="L",
    )
    pdf.cell(200, 7, txt="JENIS PEMBAYARAN :", ln=2, align="L")
    pdf.set_font("Times", size=12)
    pdf.set_xy(10, 0)
    # pdf.ln(1)
    pdf.set_xy(10, 85)
    pdf.multi_cell(20, 10, txt=DPSMI, border=1, align="C", fill=bool)
    pdf.set_xy(30, 85)
    # pdf.ln(1)
    pdf.multi_cell(
        170,
        10,
        txt="Dana Peran Serta Masyarakat Insindental",
        border=1,
        align="L",
        fill=bool,
    )
    # pdf.set_xy(10, 95)
    # pdf.multi_cell(20, 10, txt= 'Nominal', border = 1,
    #              align= 'C', fill=bool)
    pdf.set_xy(30, 95)
    # pdf.ln(1)
    pdf.multi_cell(170, 10, txt=NOMINAL_DPSMI, border=1, align="L", fill=bool)

    pdf.set_xy(10, 107)
    pdf.multi_cell(20, 10, txt=DPSMR, border=1, align="C", fill=bool)
    pdf.set_xy(30, 107)
    # pdf.ln(1)
    pdf.multi_cell(
        170, 10, txt="Dana Peran Serta Masyarakat Rutin", border=1, align="L", fill=bool
    )

    # pdf.set_xy(10, 115)
    # pdf.multi_cell(20, 10, txt= 'Nominal', border = 1,
    #              align= 'C', fill=bool)

    pdf.set_xy(30, 117)
    pdf.multi_cell(10, 10, txt=JANUARI, border=1, align="C", fill=bool)
    pdf.set_xy(40, 117)
    pdf.multi_cell(30, 10, txt="JANUARI", border=1, align="L", fill=bool)
    pdf.set_xy(70, 117)
    pdf.multi_cell(10, 10, txt=FEBRUARI, border=1, align="C", fill=bool)
    pdf.set_xy(80, 117)
    pdf.multi_cell(30, 10, txt="FEBRUARI", border=1, align="L", fill=bool)
    pdf.set_xy(110, 117)
    pdf.multi_cell(10, 10, txt=MARET, border=1, align="C", fill=bool)
    pdf.set_xy(120, 117)
    pdf.multi_cell(30, 10, txt="MARET", border=1, align="L", fill=bool)
    pdf.set_xy(150, 117)
    pdf.multi_cell(10, 10, txt=APRIL, border=1, align="C", fill=bool)
    pdf.set_xy(160, 117)
    pdf.multi_cell(40, 10, txt="APRIL", border=1, align="L", fill=bool)

    pdf.set_xy(30, 127)
    pdf.multi_cell(10, 10, txt=MEI, border=1, align="C", fill=bool)
    pdf.set_xy(40, 127)
    pdf.multi_cell(30, 10, txt="MEI", border=1, align="L", fill=bool)
    pdf.set_xy(70, 127)
    pdf.multi_cell(10, 10, txt=JUNI, border=1, align="C", fill=bool)
    pdf.set_xy(80, 127)
    pdf.multi_cell(30, 10, txt="JUNI", border=1, align="L", fill=bool)
    pdf.set_xy(110, 127)
    pdf.multi_cell(10, 10, txt=JULI, border=1, align="C", fill=bool)
    pdf.set_xy(120, 127)
    pdf.multi_cell(30, 10, txt="JULI", border=1, align="L", fill=bool)
    pdf.set_xy(150, 127)
    pdf.multi_cell(10, 10, txt=AGUSTUS, border=1, align="C", fill=bool)
    pdf.set_xy(160, 127)
    pdf.multi_cell(40, 10, txt="AGUSTUS", border=1, align="L", fill=bool)

    pdf.set_xy(30, 137)
    pdf.multi_cell(10, 10, txt=SEPTEMBER, border=1, align="C", fill=bool)
    pdf.set_xy(40, 137)
    pdf.multi_cell(30, 10, txt="SEPTEMBER", border=1, align="L", fill=bool)
    pdf.set_xy(70, 137)
    pdf.multi_cell(10, 10, txt=OKTOBER, border=1, align="C", fill=bool)
    pdf.set_xy(80, 137)
    pdf.multi_cell(30, 10, txt="OKTOBER", border=1, align="L", fill=bool)
    pdf.set_xy(110, 137)
    pdf.multi_cell(10, 10, txt=NOVEMBER, border=1, align="C", fill=bool)
    pdf.set_xy(120, 137)
    pdf.multi_cell(30, 10, txt="NOVEMBER", border=1, align="L", fill=bool)
    pdf.set_xy(150, 137)
    pdf.multi_cell(10, 10, txt=DESEMBER, border=1, align="C", fill=bool)
    pdf.set_xy(160, 137)
    pdf.multi_cell(40, 10, txt="DESEMBER", border=1, align="L", fill=bool)

    pdf.set_xy(30, 147)
    # pdf.ln(1)
    pdf.multi_cell(170, 10, txt=NOMINAL_DPSMR, border=1, align="L", fill=bool)

    pdf.set_xy(10, 159)
    pdf.multi_cell(20, 10, txt=BIMBEL, border=1, align="C", fill=bool)
    pdf.set_xy(30, 159)
    # pdf.ln(1)
    pdf.multi_cell(170, 10, txt="BIMBEL", border=1, align="L", fill=bool)

    pdf.set_xy(30, 169)
    pdf.multi_cell(10, 10, txt=JANUARI1, border=1, align="C", fill=bool)
    pdf.set_xy(40, 169)
    pdf.multi_cell(30, 10, txt="JANUARI", border=1, align="L", fill=bool)
    pdf.set_xy(70, 169)
    pdf.multi_cell(10, 10, txt=FEBRUARI1, border=1, align="C", fill=bool)
    pdf.set_xy(80, 169)
    pdf.multi_cell(30, 10, txt="FEBRUARI", border=1, align="L", fill=bool)
    pdf.set_xy(110, 169)
    pdf.multi_cell(10, 10, txt=MARET1, border=1, align="C", fill=bool)
    pdf.set_xy(120, 169)
    pdf.multi_cell(30, 10, txt="MARET", border=1, align="L", fill=bool)
    pdf.set_xy(150, 169)
    pdf.multi_cell(10, 10, txt=APRIL1, border=1, align="C", fill=bool)
    pdf.set_xy(160, 169)
    pdf.multi_cell(40, 10, txt="APRIL", border=1, align="L", fill=bool)

    pdf.set_xy(30, 179)
    pdf.multi_cell(10, 10, txt=MEI1, border=1, align="C", fill=bool)
    pdf.set_xy(40, 179)
    pdf.multi_cell(30, 10, txt="MEI", border=1, align="L", fill=bool)
    pdf.set_xy(70, 179)
    pdf.multi_cell(10, 10, txt=JUNI1, border=1, align="C", fill=bool)
    pdf.set_xy(80, 179)
    pdf.multi_cell(30, 10, txt="JUNI", border=1, align="L", fill=bool)
    pdf.set_xy(110, 179)
    pdf.multi_cell(10, 10, txt=JULI1, border=1, align="C", fill=bool)
    pdf.set_xy(120, 179)
    pdf.multi_cell(30, 10, txt="JULI", border=1, align="L", fill=bool)
    pdf.set_xy(150, 179)
    pdf.multi_cell(10, 10, txt=AGUSTUS1, border=1, align="C", fill=bool)
    pdf.set_xy(160, 179)
    pdf.multi_cell(40, 10, txt="AGUSTUS", border=1, align="L", fill=bool)

    pdf.set_xy(30, 189)
    pdf.multi_cell(10, 10, txt=SEPTEMBER1, border=1, align="C", fill=bool)
    pdf.set_xy(40, 189)
    pdf.multi_cell(30, 10, txt="SEPTEMBER", border=1, align="L", fill=bool)
    pdf.set_xy(70, 189)
    pdf.multi_cell(10, 10, txt=OKTOBER1, border=1, align="C", fill=bool)
    pdf.set_xy(80, 189)
    pdf.multi_cell(30, 10, txt="OKTOBER", border=1, align="L", fill=bool)
    pdf.set_xy(110, 189)
    pdf.multi_cell(10, 10, txt=NOVEMBER1, border=1, align="C", fill=bool)
    pdf.set_xy(120, 189)
    pdf.multi_cell(30, 10, txt="NOVEMBER", border=1, align="L", fill=bool)
    pdf.set_xy(150, 189)
    pdf.multi_cell(10, 10, txt=DESEMBER1, border=1, align="C", fill=bool)
    pdf.set_xy(160, 189)
    pdf.multi_cell(40, 10, txt="DESEMBER", border=1, align="L", fill=bool)

    pdf.set_xy(30, 199)
    # pdf.ln(1)
    pdf.multi_cell(170, 10, txt=NOMINAL_BIMBEL, border=1, align="L", fill=bool)

    pdf.line(10, 210, 200, 210)
    pdf.line(10, 211, 200, 211)
    pdf.set_font("Times", size=15)
    pdf.set_xy(10, 212)
    pdf.multi_cell(
        170,
        5,
        txt=str("TOTAL PEMBAYARAN =  Rp." + str(total_pembayaran)),
        border=0,
        align="L",
        fill=bool,
    )
    pdf.set_xy(100, 215)
    pdf.multi_cell(
        90,
        10,
        txt=str("Malang, " + str(self.TANGGAL_PEMBAYARAN)),
        border=0,
        align="R",
        fill=bool,
    )
    pdf.set_xy(10, 225)
    pdf.multi_cell(90, 5, txt="Petugas / Penerima", border=0, align="C", fill=bool)
    pdf.set_xy(110, 225)
    pdf.multi_cell(90, 5, txt="Penyetor", border=0, align="C", fill=bool)
    pdf.set_xy(10, 267)
    pdf.multi_cell(90, 5, txt=".................", border=0, align="C", fill=bool)
    pdf.set_xy(110, 267)
    pdf.multi_cell(90, 5, txt=".................", border=0, align="C", fill=bool)
    pdf.set_font("Times", size=8)
    pdf.set_xy(10, 275)
    pdf.multi_cell(
        90,
        1,
        txt="*Mohon slip bukti disimpan dengan baik",
        border=0,
        align="L",
        fill=bool,
    )

    byte_string = pdf.output(dest="S").encode("latin-1")  # Probably what you want
    stream = BytesIO(byte_string)
    return ContentFile(
        stream.getvalue(),
        "kuitansi_"
        + str(self.NAMA_SISWA.NIS.NAMA)
        + "_"
        + str(self.TANGGAL_PEMBAYARAN)
        + "_"
        + str(self.ID)
        + ".pdf",
    )


# def buat_kuitansi(self):
#    # wb_obj = openpyxl.load_workbook(self.TEMPLATE.path)
#    # sheet_obj = wb_obj.active
#    # nama_cell =  sheet_obj.cell(row = 8, column= 4)
#    # nama_cell.value = self.NAMA_SISWA.NIS.NAMA
#    # kelas_cell =  sheet_obj.cell(row = 9, column= 4)
#    # kelas_cell.value = str(self.NAMA_SISWA.KELAS)
#    # nama_cell =  sheet_obj.cell(row = 10, column= 4)
#    # nama_cell.value = self.NAMA_SISWA.NIS.NIS
#    # total_pembayaran = 0

#    # print ('test' + self.PEMBAYARAN_DPSM_INSINDENTAL)

#    # if self.NOMINAL_SPP != '' :
#    #    bulan = self.PEMBAYARAN_SPP.split(',')
#    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 11, column= 3)
#    #    jenis_pembayaran_cell.value = 'X'
#    #    total_pembayaran += (len(bulan)*int(self.NOMINAL_SPP))
#    #    print (len(bulan))
#    #    for i in range(len(bulan)):
#    #       cur = bulan[i-1].strip()
#    #       print(cur)
#    #       if cur in 'Januari':
#    #          bulan_cell =  sheet_obj.cell(row = 6, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Februari' :
#    #          bulan_cell =  sheet_obj.cell(row = 7, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Maret':
#    #          bulan_cell =  sheet_obj.cell(row = 8, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'April':
#    #          bulan_cell =  sheet_obj.cell(row = 9, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Mei':
#    #          bulan_cell =  sheet_obj.cell(row = 10, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Juni':
#    #          bulan_cell =  sheet_obj.cell(row = 10, column= 8)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Juli':
#    #          bulan_cell =  sheet_obj.cell(row = 6, column= 6)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Agustus':
#    #          bulan_cell =  sheet_obj.cell(row = 7, column= 6)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'September':
#    #          bulan_cell =  sheet_obj.cell(row = 8, column= 6)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Oktober':
#    #          bulan_cell =  sheet_obj.cell(row = 9, column= 6)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'November':
#    #          bulan_cell =  sheet_obj.cell(row = 10, column= 6)
#    #          bulan_cell.value = 'X'
#    #       elif cur in 'Desember':
#    #          bulan_cell =  sheet_obj.cell(row = 11, column= 6)
#    #          bulan_cell.value = 'X'

#    # if self.PEMBAYARAN_DPSM_RUTIN != '' :
#    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 12, column= 3)
#    #    jenis_pembayaran_cell.value = 'X'
#    #    total_pembayaran += int(float(self.PEMBAYARAN_DPSM_RUTIN))

#    # if self.PEMBAYARAN_DPSM_INSINDENTAL != 0 :
#    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 13, column= 3)
#    #    jenis_pembayaran_cell.value = 'X'
#    #    value = self.PEMBAYARAN_DPSM_INSINDENTAL
#    #    print (value)
#    #    total_pembayaran += int(value)

#    # elif self.BIMBEL != 0 :
#    #    jenis_pembayaran_cell =  sheet_obj.cell(row = 14, column= 3)
#    #    jenis_pembayaran_cell.value = 'X'
#    #    total_pembayaran += int(self.BIMBEL)

#    # nominal_cell =  sheet_obj.cell(row = 15, column= 4)
#    # nominal_cell.value = 'Rp. ' + str(total_pembayaran)
#    # virtual_workbook = BytesIO()
#    # wb_obj.save(virtual_workbook)

#    DPSMR = ''
#    DPSMI = ''
#    BIMBEL = ''
#    SPP = ''

#    NILAI_SPP = ''

#    JANUARI = ''
#    FEBRUARI = ''
#    MARET = ''
#    APRIL = ''
#    MEI = ''
#    JUNI = ''
#    JULI = ''
#    AGUSTUS = ''
#    SEPTEMBER = ''
#    OKTOBER = ''
#    NOVEMBER = ''
#    DESEMBER = ''
#    total_pembayaran = 0

#    if self.NOMINAL_SPP != '0'or  self.NOMINAL_SPP :
#       bulan = self.PEMBAYARAN_SPP.split(',')
#       SPP = 'X'
#       total_pembayaran += (len(bulan)*int(self.NOMINAL_SPP))
#       print (len(bulan))
#       for i in range(len(bulan)):
#          cur = bulan[i-1].strip()
#          print(cur)
#          if cur in 'Januari':
#             JANUARI = 'X'
#          elif cur in 'Februari' :
#             FEBRUARI = 'X'
#          elif cur in 'Maret':
#             MARET = 'X'
#          elif cur in 'April':
#             APRIL = 'X'
#          elif cur in 'Mei':
#             MEI = ''
#          elif cur in 'Juni':
#             JUNI = 'X'
#          elif cur in 'Juli':
#             JULI = 'X'
#          elif cur in 'Agustus':
#             AGUSTUS = 'X'
#          elif cur in 'September':
#             SEPTEMBER = 'X'
#          elif cur in 'Oktober':
#             OKTOBER = 'X'
#          elif cur in 'November':
#             NOVEMBER = 'X'
#          elif cur in 'Desember':
#             DESEMBER = 'X'

#    if self.PEMBAYARAN_DPSM_RUTIN != '0' or self.PEMBAYARAN_DPSM_RUTIN != '':
#       DPSMR = 'X'
#       total_pembayaran += int(float(self.PEMBAYARAN_DPSM_RUTIN))

#    if self.PEMBAYARAN_DPSM_INSINDENTAL != '0' or self.PEMBAYARAN_DPSM_INSINDENTAL != '' :
#       DPSMI = 'X'
#       value = self.PEMBAYARAN_DPSM_INSINDENTAL
#       print (value)
#       total_pembayaran += int(value)

#    if self.BIMBEL != '0' or self.self.BIMBEL != '':
#       BIMBEL = 'X'
#       total_pembayaran += int(self.BIMBEL)

#    pdf = FPDF()

#    # Add a page
#    pdf.add_page()

#    # set style and size of font
#    # that you want in the pdf

#    pdf.set_font("Times", size = 15)
#    # create a cell
#    # pdf.cell(200, 10, )
#    pdf.image(os.path.join(current_folder, 'bahan_kuitansi/Logo.png'), x = None, y = None, w = 190, h = 35, type = '', link = '')
#    pdf.cell(200, 12, txt = "KUITANSI PEMBAYARAN",
#             ln = 1, align = 'C')
#    pdf.line(10, 55, 200, 55)
#    pdf.line(10, 56, 200, 56)
#    pdf.set_font("Times", size = 15)
#    # add another cell
#    pdf.cell(200, 10, txt = str('NAMA SISWA    = ' + self.NAMA_SISWA.NIS.NAMA),
#             ln = 2, align = 'L')
#    pdf.cell(200, 10, txt = str('KELAS                 = ' + str(self.NAMA_SISWA.KELAS)),
#             ln = 2, align = 'L')
#    pdf.cell(200, 10, txt = str('NOMOR INDUK = ' + str(self.NAMA_SISWA.NIS.NIS)),
#             ln = 2, align = 'L')
#    pdf.cell(200, 10, txt = 'JENIS PEMBAYARAN :',
#             ln = 2, align = 'L')
#    pdf.set_font("Times", size = 15)
#    pdf.set_xy(10, 100)
#    # pdf.ln(1)
#    pdf.multi_cell(20, 10, txt= DPSMR, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(30, 100)
#    # pdf.ln(1)
#    pdf.multi_cell(170, 10, txt= 'Dana Peran Serta Masyarakat Rutin', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 110)
#    pdf.multi_cell(20, 10, txt= DPSMI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(30, 110)
#    # pdf.ln(1)
#    pdf.multi_cell(170, 10, txt= 'Dana Peran Serta Masyarakat Insindental', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 120)
#    pdf.multi_cell(20, 10, txt= BIMBEL, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(30, 120)
#    # pdf.ln(1)
#    pdf.multi_cell(170, 10, txt= 'Bimbel', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 130)
#    pdf.multi_cell(20, 10, txt= SPP, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(30, 130)
#    # pdf.ln(1)
#    pdf.multi_cell(170, 10, txt= 'SPP', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_font("Times", size = 15)
#    pdf.set_xy(10, 140)
#    pdf.multi_cell(75, 10, txt= 'JUMLAH SPP PER BULAN = ', border = 0,
#                 align= 'L', fill=bool)
#    pdf.set_xy(85, 140)
#    # pdf.ln(1)
#    pdf.multi_cell(125, 10, txt= str(self.NOMINAL_SPP), border = 0,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 150)
#    pdf.multi_cell(80, 10, txt= 'PEMBAYARAN BULAN : ', border = 0,
#                 align= 'L', fill=bool)
#    pdf.line(10, 161, 200, 161)
#    pdf.set_font("Times", size = 15)
#    pdf.set_xy(10, 165)
#    pdf.multi_cell(10, 10, txt= JANUARI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(20, 165)
#    pdf.multi_cell(50, 10, txt= 'JANUARI', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(70, 165)
#    pdf.multi_cell(10, 10, txt= FEBRUARI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(80, 165)
#    pdf.multi_cell(50, 10, txt= 'FEBRUARI', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(130, 165)
#    pdf.multi_cell(10, 10, txt= MARET, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(140, 165)
#    pdf.multi_cell(60, 10, txt= 'MARET', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 175)
#    pdf.multi_cell(10, 10, txt= APRIL, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(20, 175)
#    pdf.multi_cell(50, 10, txt= 'APRIL', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(70, 175)
#    pdf.multi_cell(10, 10, txt= MEI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(80, 175)
#    pdf.multi_cell(50, 10, txt= 'MEI', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(130, 175)
#    pdf.multi_cell(10, 10, txt= JUNI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(140, 175)
#    pdf.multi_cell(60, 10, txt= 'JUNI', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 185)
#    pdf.multi_cell(10, 10, txt= JULI, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(20, 185)
#    pdf.multi_cell(50, 10, txt= 'JULI', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(70, 185)
#    pdf.multi_cell(10, 10, txt= AGUSTUS, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(80, 185)
#    pdf.multi_cell(50, 10, txt= 'AGUSTUS', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(130, 185)
#    pdf.multi_cell(10, 10, txt= SEPTEMBER, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(140, 185)
#    pdf.multi_cell(60, 10, txt= 'SEPTEMBER', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(10, 195)
#    pdf.multi_cell(10, 10, txt= OKTOBER, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(20, 195)
#    pdf.multi_cell(50, 10, txt= 'OKTOBER', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(70, 195)
#    pdf.multi_cell(10, 10, txt= NOVEMBER, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(80, 195)
#    pdf.multi_cell(50, 10, txt= 'NOVEMBER', border = 1,
#                 align= 'L', fill=bool)
#    pdf.set_xy(130, 195)
#    pdf.multi_cell(10, 10, txt= DESEMBER, border = 1,
#                 align= 'C', fill=bool)
#    pdf.set_xy(140, 195)
#    pdf.multi_cell(60, 10, txt= 'DESEMBER', border = 1,
#                 align= 'L', fill=bool)
#    pdf.line(10, 207, 200, 207)
#    pdf.line(10, 208, 200, 208)
#    pdf.set_font("Times", size = 15)
#    pdf.set_xy(10, 210)
#    pdf.multi_cell(170, 5, txt= str('TOTAL PEMBAYARAN =  Rp.' + str(total_pembayaran)), border = 0,
#                 align= 'L', fill=bool)
#    pdf.set_xy(100, 215)
#    pdf.multi_cell(90, 10, txt= str('Malang, ' + str(self.TANGGAL_PEMBAYARAN)), border = 0,
#                 align= 'R', fill=bool)
#    pdf.set_xy(10, 225)
#    pdf.multi_cell(90, 5, txt= 'Petugas / Penerima', border = 0,
#                 align= 'C', fill=bool)
#    pdf.set_xy(110, 225)
#    pdf.multi_cell(90, 5, txt= 'Penyetor', border = 0,
#                 align= 'C', fill=bool)
#    pdf.set_xy(10, 267)
#    pdf.multi_cell(90, 5, txt= '.................', border = 0,
#                 align= 'C', fill=bool)
#    pdf.set_xy(110, 267)
#    pdf.multi_cell(90, 5, txt= '.................', border = 0,
#                 align= 'C', fill=bool)
#    pdf.set_font("Times", size = 8)
#    pdf.set_xy(10, 275)
#    pdf.multi_cell(90, 1, txt= '*Mohon slip bukti disimpan dengan baik', border = 0,
#                 align= 'L', fill=bool)

#    # save the pdf with name .pdf
#    # pdf.output("GFG.pdf")
#    byte_string = pdf.output(dest='S').encode('latin-1')  # Probably what you want
#    stream = BytesIO(byte_string)

#    # out_stream = xlsx2html(self.TEMPLATE.path)
#    # out_stream.seek(0)
#    # print(out_stream.read())

#    # xlsx2html(self.TEMPLATE.path, 'output.html')

#    # pw = pdfwriter()
#    # pw.setFont('Courier', 12)
#    # pw.setHeader('XLSXtoPDF.py - convert XLSX data to PDF')
#    # pw.setFooter('Generated using openpyxl and xtopdf')

#    # ws_range = sheet_obj.iter_rows('A1:H13')
#    # for row in ws_range:
#    #    s = ''
#    #    for cell in row:
#    #       if cell.value is None:
#    #             s += ' ' * 11
#    #       else:
#    #             s += str(cell.value).rjust(10) + ' '
#    #    pw.writeLine(s)
#    # pw.savePage()
#    # pw.close()

#    # options =  HtmlSaveOptions()
#    # # show tooltips
#    # options.setAddTooltipText(True)
#    # # save workbook as HTML file
#    # wb.save("workbook.html", options)
#    # wb_obj.save("workbook.html")
#    # df = pd.read_excel(virtual_workbook.getvalue())
#    # df.to_html("file.html")
#    # pdfkit.from_file("file.html", "file.pdf")
#    # Open Microsoft Excel
#    # excel = client.Dispatch("Excel.Application")

#    # # Read Excel File
#    # sheets = excel.Workbooks.Open('Excel File Path')
#    # work_sheets = sheets.Worksheets[0]

#    # # Convert into PDF File
#    # work_sheets.ExportAsFixedFormat(0, 'PDF File Path')

#    return ContentFile(stream.getvalue(), 'kuitansi_' + str(self.NAMA_SISWA.NIS.NAMA) + '_'+ str(self.TANGGAL_PEMBAYARAN)+'_'+ str(self.ID) + '.pdf')
