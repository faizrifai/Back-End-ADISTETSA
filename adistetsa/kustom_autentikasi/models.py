from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_delete, post_save

from dataprofil.models import (
    DataSiswa,
    DataOrangTua,
    DataGuru,
    DataKaryawan,
    DataPelatih,
)


# Create your models here.
class DataSiswaUser(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DATA_SISWA = models.ForeignKey(DataSiswa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.DATA_SISWA)

    class Meta:
        verbose_name_plural = "Data Siswa User"


def post_save_data_siswa(sender, instance, **kwargs):
    try:
        data_siswa_user = DataSiswaUser.objects.get(DATA_SISWA__NIS=instance.NIS)
        user = data_siswa_user.USER
        user.email = instance.EMAIL
        user.save()
    except:
        pass


post_save.connect(post_save_data_siswa, sender=DataSiswa)


def post_delete_data_siswa_user(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.USER.username)
        user.delete()
    except:
        pass


post_delete.connect(post_delete_data_siswa_user, sender=DataSiswaUser)


class DataOrangTuaUser(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DATA_ORANG_TUA = models.ForeignKey(DataOrangTua, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Data Orang Tua User"


class DataGuruUser(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DATA_GURU = models.OneToOneField(DataGuru, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.DATA_GURU.NAMA_LENGKAP)

    class Meta:
        verbose_name_plural = "Data Guru User"


def post_save_data_guru(sender, instance, **kwargs):
    try:
        data_guru_user = DataGuruUser.objects.get(DATA_GURU__NIK=instance.NIK)
        user = data_guru_user.USER
        user.email = instance.EMAIL
        user.save()
    except:
        pass


post_save.connect(post_save_data_guru, sender=DataGuru)


def post_delete_data_guru_user(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.USER.username)
        user.delete()
    except:
        pass


post_delete.connect(post_delete_data_guru_user, sender=DataGuruUser)


class DataKaryawanUser(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DATA_KARYAWAN = models.ForeignKey(DataKaryawan, on_delete=models.CASCADE)

    def __str__(self):
        return (
            str(self.DATA_KARYAWAN.NAMA_LENGKAP)
            + " Username: "
            + str(self.USER.username)
        )

    class Meta:
        verbose_name_plural = "Data Karyawan User"


def post_save_data_karyawan(sender, instance, **kwargs):
    try:
        data_karyawan_user = DataKaryawanUser.objects.get(
            DATA_KARYAWAN__NIK=instance.NIK
        )
        user = data_karyawan_user.USER
        user.email = instance.EMAIL
        user.save()
    except:
        pass


post_save.connect(post_save_data_karyawan, sender=DataKaryawan)


class DataPelatihUser(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DATA_PELATIH = models.ForeignKey(DataPelatih, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.DATA_PELATIH.NAMA) + " Username: " + str(self.USER.username)

    class Meta:
        verbose_name_plural = "Data Pelatih User"


def post_save_data_pelatih(sender, instance, created, **kwargs):
    if created:
        try:
            nama = str(instance.NAMA).lower().replace(" ", "_")
            new_username = nama + "_" + str(instance.ID)
            user = User.objects.create(
                username=new_username, password=make_password("merdeka123")
            )
            user.save()

            role = Group.objects.get(name="Pelatih")
            role.user_set.add(user)

            data_pelatih_user = DataPelatihUser.objects.create(
                DATA_PELATIH=instance, USER=user
            )
            data_pelatih_user.save()
        except Exception as e:
            print(str(e))


post_save.connect(post_save_data_pelatih, sender=DataPelatih)


def post_delete_data_pelatih_user(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.USER.username)
        user.delete()
    except:
        pass


post_delete.connect(post_delete_data_pelatih_user, sender=DataPelatihUser)
