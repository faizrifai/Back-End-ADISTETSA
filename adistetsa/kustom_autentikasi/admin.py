from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import *
from .dependencies import *

# Register your import_export resource model here
class DataSiswaUserResource(resources.ModelResource):
    nisn = Field(
        column_name='nisn',
        attribute='DATA_SISWA',
        widget=ForeignKeyWidget(DataSiswa, 'NISN')
    )
    password = Field(
        column_name='password',
        attribute='USER',
        widget=ForeignKeyWidget(User, 'password')
    )

    class Meta:
        model = DataSiswaUser
        exclude = ('id')
        fields = ('nisn', 'password')
        import_id_fields = ('nisn', 'password')

    def before_import_row(self, row, **kwargs):
        nisn = row['nisn']
        data_siswa = DataSiswa.objects.get(NISN=nisn)

        username = str(data_siswa.NISN)
        password = row['password']

        try:
            user = User.objects.get(username=username)
            user.delete()
        except:
            pass

        new_user = User.objects.get_or_create(username=username, password=password)
        row['USER'] = new_user[0].id

        grup_siswa = Group.objects.get(name='Siswa')
        grup_siswa.user_set.add(new_user[0])

        row['DATA_SISWA'] = data_siswa.NISN

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

# Register your models here.
class DataSiswaUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['DATA_SISWA', 'USER',]
    search_fields = ['DATA_SISWA__NISN', 'DATA_SISWA__NAMA', 'USER__username']
    list_display = ('nama_lengkap', 'username', 'role')

    resource_class = DataSiswaUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse('admin:auth_user_changelist')
        
        return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username))

    def nama_lengkap(self, obj):
        return obj.DATA_SISWA.NAMA

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ''
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ', '

        return group_display

class DataGuruUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['DATA_GURU', 'USER',]
    search_fields = ['DATA_GURU__NIP', 'DATA_GURU__NAMA_LENGKAP', 'USER__username']
    list_display = ('nama_lengkap', 'username', 'role')

    resource_class = DataGuruUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse('admin:auth_user_changelist')
        
        return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username))

    def nama_lengkap(self, obj):
        return obj.DATA_GURU.NAMA_LENGKAP

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ''
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ', '

        return group_display

class DataKaryawanUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = ['DATA_KARYAWAN', 'USER',]
    search_fields = ['DATA_KARYAWAN__NIK', 'DATA_KARYAWAN__NAMA_LENGKAP', 'USER__username']
    list_display = ('nama_lengkap', 'username', 'role')

    resource_class = DataKaryawanUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse('admin:auth_user_changelist')
        
        return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username))

    def nama_lengkap(self, obj):
        return obj.DATA_KARYAWAN.NAMA_LENGKAP

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ''
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ', '

        return group_display

class DataOrangTuaUserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['DATA_ORANG_TUA', 'USER',]
    search_fields = ['DATA_ORANG_TUA__NAMA_AYAH', 'DATA_ORANG_TUA__NAMA_IBU', 'DATA_ORANG_TUA__NAMA_WALI', 'USER__username']
    list_display = ('aksi', 'nama_ayah', 'nama_ibu', 'nama_wali', 'username', 'role')

    def aksi(self, obj):
        return 'Detail'

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse('admin:auth_user_changelist')
        
        return mark_safe(u'<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username))

    def nama_ayah(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_AYAH

    def nama_ibu(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_IBU

    def nama_wali(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_WALI

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ''
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ', '

        return group_display

admin.site.register(DataSiswaUser, DataSiswaUserAdmin)
admin.site.register(DataOrangTuaUser, DataOrangTuaUserAdmin)
admin.site.register(DataGuruUser, DataGuruUserAdmin)
admin.site.register(DataKaryawanUser, DataKaryawanUserAdmin)