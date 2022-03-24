from distutils.command.upload import upload
from django.db import models

# Create your models here.
class SanitasiDrainase(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TANGGAL = models.DateField()
    NAMA_KEGIATAN = models.CharField(max_length=255)
    UNSUR_TERLIBAT = models.CharField(max_length=255)
    KETERANGAN = models.CharField(max_length=255)
    FILE = models.FileField(upload_to=" ", max_length=255)
    
