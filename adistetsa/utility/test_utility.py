from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Model
from django.urls import reverse
from factory.django import DjangoModelFactory
from rest_framework import status

from dataprofil.models import *
from dataprofil.factories import *
from kustom_autentikasi.models import *

def buatRole():
    Group.objects.update_or_create(name='Siswa')
    Group.objects.update_or_create(name='Guru')
    Group.objects.update_or_create(name='Orang Tua')
    Group.objects.update_or_create(name='Karyawan')
    Group.objects.update_or_create(name='Pelatih')
    Group.objects.update_or_create(name='Staf Adiwiyata')
    Group.objects.update_or_create(name='Staf BK')
    Group.objects.update_or_create(name='Staf PPDB')
    Group.objects.update_or_create(name='Staf Humas')
    Group.objects.update_or_create(name='Staf Kesiswaan')
    Group.objects.update_or_create(name='Staf Keuangan')
    Group.objects.update_or_create(name='Staf Kurikulum')
    Group.objects.update_or_create(name='Staf Perpustakaan')
    Group.objects.update_or_create(name='Staf Sarpras')
    Group.objects.update_or_create(name='Staf TU')
    Group.objects.update_or_create(name='Staf UPM')

def get_attribute(instance, name):
    if hasattr(instance, name):
        return getattr(instance, name)

    names = name.split('__')
    name = names.pop(0)
    if len(names) == 0:
        return None

    if hasattr(instance, name):
        value = getattr(instance, name)
        return get_attribute(value, '__'.join(names))

    return None

def generateUserSiswa():
    # Generate data siswa
    DataSiswaFactory()
    data = DataSiswa.objects.last()

    # Set username and password
    username = str(data.NIS)
    password = 'merdeka123'

    # Generate user
    new_user = User.objects.create_user(username, data.EMAIL, password)
    grup = Group.objects.get(name='Siswa')
    grup.user_set.add(new_user)

    DataSiswaUser.objects.create(USER=new_user, DATA_SISWA=data)

    return {'username': username, 'password': password}

def generateUserGuru(extra_roles=None):
    # Generate data guru
    DataGuruFactory()
    data = DataGuru.objects.last()

    # Set username and password
    username = (data.NAMA_LENGKAP + '_' + str(data.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
    password = 'merdeka123'

    # Generate user
    new_user = User.objects.create_user(username, data.EMAIL, password)
    grup = Group.objects.get(name='Guru')
    grup.user_set.add(new_user)

    # Add extra role
    for group in extra_roles:
        grup = Group.objects.get(name=group)
        grup.user_set.add(new_user)

    DataGuruUser.objects.create(USER=new_user, DATA_GURU=data)

    return {'username': username, 'password': password}

def generateUserKaryawan(extra_roles=None):
    # Generate data karyawan
    DataKaryawanFactory()
    data = DataKaryawan.objects.last()

    # Set username and password
    username = (data.NAMA_LENGKAP + '_' + str(data.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
    password = 'merdeka123'

    # Generate user
    new_user = User.objects.create_user(username, data.EMAIL, password)
    grup = Group.objects.get(name='Karyawan')
    grup.user_set.add(new_user)

    # Add extra role
    for group in extra_roles:
        grup = Group.objects.get(name=group)
        grup.user_set.add(new_user)

    DataKaryawanUser.objects.create(USER=new_user, DATA_GURU=data)

    return {'username': username, 'password': password}

def generateUserOrangTua():
    # Generate data orang tua
    DataOrangTuaFactory()
    data = DataOrangTua.objects.last()

    # Set username and password
    username = (data.NAMA_AYAH + '_' + str(data.TAHUN_LAHIR_AYAH.year)).lower().replace(' ', '_')
    password = 'merdeka123'

    # Generate user
    new_user = User.objects.create_user(username, data.EMAIL, password)
    grup = Group.objects.get(name='Orang Tua')
    grup.user_set.add(new_user)

    DataOrangTuaUser.objects.create(USER=new_user, DATA_ORANG_TUA=data)

    return {'username': username, 'password': password}

def generateUserPelatih():
    # Generate data pelatih
    DataPelatihFactory()
    data = DataPelatih.objects.last()

    # Set username and password
    username = (data.NAMA).lower().replace(' ', '_')
    password = 'merdeka123'

    # Generate user
    new_user = User.objects.create_user(username, data.EMAIL, password)
    grup = Group.objects.get(name='Pelatih')
    grup.user_set.add(new_user)

    DataPelatih.objects.create(USER=new_user, DATA_ORANG_TUA=data)

    return {'username': username, 'password': password}

def loginWithUserData(self, data_login):
    login_response = self.client.post(reverse('login'), data_login)
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['access'])

def testListView(self, url: str, factory_class: DjangoModelFactory, factory_length: int, check_length=True):
    for _ in range(factory_length):
        factory_class()

    response = self.client.get(reverse(url))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    if check_length:
        self.assertEqual(len(response.data['results']), factory_length)

    return response

def testPostView(self, url: str, post_data: dict):
    response = self.client.post(reverse(url), post_data)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def testPostWithFileView(self, url: str, post_data: dict, file_key: str):
    # Dummy file
    uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', b"tes abc", content_type='text/plain')
    post_data[file_key] = uploaded_file

    response = self.client.post(reverse(url), post_data)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def testUpdateView(self, url: str, factory_class: DjangoModelFactory, update_data: dict):
    # Generate new data
    factory_class()

    response = self.client.put(reverse(url, kwargs={'pk': 1}), update_data, format='multipart')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

def testUpdateWithFileView(self, url: str, factory_class: DjangoModelFactory, update_data: dict, file_key: str):
    # Generate new data
    factory_class()

    # Dummy file
    uploaded_file = SimpleUploadedFile('data_karyawan_user.csv', b"tes abc", content_type='text/plain')
    update_data[file_key] = uploaded_file
    response = self.client.put(reverse(url, kwargs={'pk': 1}), update_data, format='multipart')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    return response

def testDeleteView(self, url: str, factory_class: DjangoModelFactory, factory_length: int):
    for _ in range(factory_length):
        factory_class()

    # Before delete
    response = self.client.get(reverse(url))
    before_length = len(response.data['results'])
    response = self.client.delete(reverse(url, kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # After delete
    response = self.client.get(reverse(url))
    self.assertEqual(len(response.data['results']), before_length - 1)

    return response

def testListViewWithSearch(self, url: str, factory_class: DjangoModelFactory, factory_length: int, model_class: Model, model_field: str, check_length=True):
    for _ in range(factory_length):
        factory_class()

    response = self.client.get(reverse(url))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    if check_length:
        self.assertEqual(len(response.data['results']), factory_length)

    # search
    data = model_class.objects.get(pk=1)
    search_str = get_attribute(data, model_field)
    url_search = '{base_url}?{querystring}'.format(
        base_url=reverse(url),
        querystring=f'search={search_str}'
    )
    response_search = self.client.get(url_search)

    self.assertLessEqual(len(response_search.data['results']), 1)

    return response