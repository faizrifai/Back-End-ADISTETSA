from telnetlib import STATUS
from django import shortcuts
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.db.models.query_utils import select_related_descend
from django.db.models.signals import post_save

from dataprofil.models import DataGuru, DataSiswa
from kurikulum.models import PoinPelanggaran
import datetime

from .enums import *


class PengajuanLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )
    
class PelanggaranSiswa(models.Model):
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    POIN = models.PositiveBigIntegerField(default=0)
    
class RiwayatLaporanPelanggaran(models.Model):
    ID = models.BigAutoField(primary_key=True)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)
    BUKTI_PELANGGARAN = models.FileField(max_length=255, upload_to='BuktiPelanggaran')
    JENIS_PELANGGARAN = models.ForeignKey(PoinPelanggaran, on_delete=models.CASCADE)
    STATUS_PENGAJUAN = models.CharField(
        max_length=255, 
        choices=ENUM_PENGAJUAN_PELANGGARAN,
        default='Diajukan'
    )

def post_save_persetujuan_laporan(sender, instance, **kwargs):
    try: 
        if instance.STATUS_PENGAJUAN == 'Disetujui' :
            obj = PelanggaranSiswa.objects.get(
                DATA_SISWA = instance.DATA_SISWA
            )
            obj.POIN += instance.JENIS_PELANGGARAN.POIN
            obj.save()
            try:
                riwayat = RiwayatLaporanPelanggaran.objects.create(
                    DATA_SISWA = instance.DATA_SISWA,
                    BUKTI_PELANGGARAN = instance.BUKTI_PELANGGARAN,
                    JENIS_PELANGGARAN = instance.JENIS_PELANGGARAN, 
                    STATUS_PENGAJUAN = instance.STATUS_PENGAJUAN
                )
                riwayat.save()
                instance.delete()
            except Exception as e:
                print(str(e))
                
        elif instance.STATUS_PENGAJUAN == 'Ditolak' :
            instance.delete()
    except:
        pass

post_save.connect(post_save_persetujuan_laporan, sender =  PengajuanLaporanPelanggaran)

# post_save.connect(post_save_pengajuan_laporan_pelanggaran, sender=PengajuanLaporanPelanggaran)
    
    