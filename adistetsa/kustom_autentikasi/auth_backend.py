from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import DataSiswaUser, DataGuruUser

class DataSiswaAuthModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        nis = kwargs['username']
        password = kwargs['password']

        try:
            data_siswa = DataSiswaUser.objects.get(DATA_SISWA=nis)
            if (data_siswa.USER.check_password(password) is True):
                return data_siswa.USER
        except DataSiswaUser.DoesNotExist:
            return None
        except ValueError:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailAuthModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']

        try:
            user = User.objects.get(email=email)
            if (user.check_password(password) is True):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class DataGuruPNSAuthModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        nip = kwargs['username']
        password = kwargs['password']

        try:
            data_guru = DataGuruUser.objects.get(DATA_GURU__NIP=nip)
            
            if (data_guru.USER.check_password(password) is True):
                return data_guru.USER
        except DataGuruUser.DoesNotExist:
            print("Tidak ada data gaes")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None