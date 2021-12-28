from django.db import models
from django.contrib.auth.models import User

from dataprofil.models import DataSiswa

# Create your models here.
class DataSiswaUser(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    NISN = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)