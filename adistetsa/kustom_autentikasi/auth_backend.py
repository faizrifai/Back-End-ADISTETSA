from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import DataSiswaUser

class DataSiswaAuthModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        nisn = kwargs['username']
        password = kwargs['password']

        try:
            nisn = int(nisn)
        except:
            return None

        try:
            data_siswa = DataSiswaUser.objects.get(NISN=nisn)
            if (data_siswa.USER.check_password(password) is True):
                return data_siswa.USER
        except DataSiswaUser.DoesNotExist:
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