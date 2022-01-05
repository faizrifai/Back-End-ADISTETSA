from django.contrib.auth.models import User, Group

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources

from dataprofil.models import DataSiswa, DataGuru, DataKaryawan
from .models import *

# Register your import_export resource model here
class DataSiswaUserResource(resources.ModelResource):
    nis = Field(
        column_name='nis',
        attribute='DATA_SISWA',
        widget=ForeignKeyWidget(DataSiswa, 'NIS')
    )
    password = Field(
        column_name='password',
        attribute='USER',
        widget=ForeignKeyWidget(User, 'password')
    )

    class Meta:
        model = DataSiswaUser
        exclude = ('id')
        fields = ('nis', 'password')
        import_id_fields = ('nis', 'password')

    def before_import_row(self, row, **kwargs):
        nis = row['nis']
        data_siswa = DataSiswa.objects.get(NIS=nis)

        username = str(data_siswa.NIS)
        password = row['password']

        try:
            user = User.objects.get(username=username)
            user.delete()
        except:
            pass
        
        new_user = User.objects.get_or_create(username=username, password=password, email=data_siswa.EMAIL)
        row['USER'] = new_user[0].id

        grup_siswa = Group.objects.get(name='Siswa')
        grup_siswa.user_set.add(new_user[0])

        row['DATA_SISWA'] = data_siswa.NIS

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            new_password = instance.USER.password
            if not (instance.USER.check_password(new_password)):
                instance.USER.set_password(new_password)
                instance.USER.save()

            instance.save()

        except:
            pass

class DataGuruUserResource(resources.ModelResource):
    nik = Field(
        column_name='nik',
        attribute='DATA_GURU',
        widget=ForeignKeyWidget(DataGuru, 'NIK')
    )
    password = Field(
        column_name='password',
        attribute='USER',
        widget=ForeignKeyWidget(User, 'password')
    )

    class Meta:
        model = DataGuruUser
        exclude = ('id')
        fields = ('nik', 'password')
        import_id_fields = ('nik', 'password')

    def before_import_row(self, row, **kwargs):
        nik = row['nik']
        data_guru = DataGuru.objects.get(NIK=nik)

        username = (data_guru.NAMA_LENGKAP + '_' + str(data_guru.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
        password = row['password']

        try:
            user = User.objects.get(username=username)
            user.delete()
        except:
            pass

        new_user = User.objects.get_or_create(username=username, password=password)
        row['USER'] = new_user[0].id

        grup_guru = Group.objects.get(name='Guru')
        grup_guru.user_set.add(new_user[0])

        row['DATA_GURU'] = data_guru.ID

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            new_password = instance.USER.password
            if not (instance.USER.check_password(new_password)):
                instance.USER.set_password(new_password)
                instance.USER.save()

            instance.save()

        except:
            pass

class DataKaryawanUserResource(resources.ModelResource):
    nik = Field(
        column_name='nik',
        attribute='DATA_KARYAWAN',
        widget=ForeignKeyWidget(DataKaryawan, 'NIK')
    )
    password = Field(
        column_name='password',
        attribute='USER',
        widget=ForeignKeyWidget(User, 'password')
    )

    class Meta:
        model = DataKaryawanUser
        exclude = ('id')
        fields = ('nik', 'password')
        import_id_fields = ('nik', 'password')

    def before_import_row(self, row, **kwargs):
        nik = row['nik']
        data_karyawan = DataKaryawan.objects.get(NIK=nik)

        username = (data_karyawan.NAMA_LENGKAP + '_' + str(data_karyawan.TANGGAL_LAHIR.year)).lower().replace(' ', '_')
        password = row['password']

        try:
            user = User.objects.get(username=username)
            user.delete()
        except:
            pass

        new_user = User.objects.get_or_create(username=username, password=password)
        row['USER'] = new_user[0].id

        grup_karyawan = Group.objects.get(name='Karyawan')
        grup_karyawan.user_set.add(new_user[0])

        row['DATA_KARYAWAN'] = data_karyawan.ID

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            new_password = instance.USER.password
            if not (instance.USER.check_password(new_password)):
                instance.USER.set_password(new_password)
                instance.USER.save()

            instance.save()

        except:
            pass