from django.db import models
from django.contrib.auth.models import User

from dataprofil.models import DataSiswa, DataOrangTua, DataGuru, DataKaryawan

# Create your models here.
class DataSiswaUser(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.DATA_SISWA)

    class Meta:
        verbose_name_plural = "Data Siswa User"

class DataOrangTuaUser(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    DATA_ORANG_TUA = models.ForeignKey(DataOrangTua, on_delete=models.CASCADE)
    USERNAME = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.DATA_ORANG_TUA.NAMA_LENGKAP) + " Username: " + str(self.USERNAME)

    class Meta:
        verbose_name_plural = "Data Orang Tua User"

class DataGuruUser(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    DATA_GURU = models.OneToOneField(DataGuru, on_delete=models.CASCADE)
    USERNAME = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.DATA_GURU.NAMA_LENGKAP) + " Username: " + str(self.USERNAME)

    class Meta:
        verbose_name_plural = "Data Guru User"

class DataKaryawanUser(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    DATA_KARYAWAN = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)
    USERNAME = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.DATA_KARYAWAN.NAMA_LENGKAP) + " Username: " + str(self.USERNAME)

    class Meta:
        verbose_name_plural = "Data Karyawan User"