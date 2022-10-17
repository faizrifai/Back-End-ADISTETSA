from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from kurikulum.models import KelasSiswa
from bimbingan_konseling.models import DataAlumni
from import_export.admin import ImportExportModelAdmin

from .models import *
from .importexportresources import *


# Register your models here.
class DataSiswaUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = [
        "DATA_SISWA",
        "USER",
    ]
    search_fields = ["DATA_SISWA__NIS", "DATA_SISWA__NAMA", "USER__username"]
    list_display = ("nama_lengkap", "username", "role")
    actions = (
        "pindah_alumni",
        "pindah_siswa",
    )

    resource_class = DataSiswaUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse("admin:auth_user_changelist")

        return mark_safe(
            '<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username)
        )

    def nama_lengkap(self, obj):
        return obj.DATA_SISWA.NAMA

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ""
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ", "

        return group_display

    def pindah_alumni(self, request, queryset):
        grup_alumni = Group.objects.get(name="Alumni")
        grup_siswa = Group.objects.get(name="Siswa")
        for d in queryset.values():
            siswa = DataSiswaUser.objects.get(USER_id=d["USER_id"]).USER
            grup_alumni.user_set.add(siswa)
            grup_siswa.user_set.remove(siswa)
            kelas = KelasSiswa.objects.filter(NIS_id=d["DATA_SISWA_id"]).last()
            DataAlumni.objects.update_or_create(
                NAMA_SISWA=kelas.NIS.NAMA,
                KELAS=kelas.KELAS.KELAS.TINGKATAN
                + " "
                + str(kelas.KELAS.KELAS.JURUSAN)
                + " "
                + kelas.KELAS.OFFERING.NAMA,
                NISN=kelas.NIS.NISN,
                NIS=kelas.NIS.NIS,
                TAHUN_AJARAN=str(kelas.KELAS.KELAS.TAHUN_AJARAN),
            )

    def pindah_siswa(self, request, queryset):
        grup_alumni = Group.objects.get(name="Alumni")
        grup_siswa = Group.objects.get(name="Siswa")
        for d in queryset.values():
            print(d)
            siswa = DataSiswaUser.objects.get(USER_id=d["USER_id"]).USER
            grup_alumni.user_set.remove(siswa)
            grup_siswa.user_set.add(siswa)
            DataAlumni.objects.get(NIS=d["DATA_SISWA_id"]).delete()


class DataGuruUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = [
        "DATA_GURU",
        "USER",
    ]
    search_fields = ["DATA_GURU__NIP", "DATA_GURU__NAMA_LENGKAP", "USER__username"]
    list_display = ("nama_lengkap", "username", "role")

    resource_class = DataGuruUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse("admin:auth_user_changelist")

        return mark_safe(
            '<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username)
        )

    def nama_lengkap(self, obj):
        return obj.DATA_GURU.NAMA_LENGKAP

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ""
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ", "

        return group_display


class DataKaryawanUserAdmin(ImportExportModelAdmin):
    autocomplete_fields = [
        "DATA_KARYAWAN",
        "USER",
    ]
    search_fields = [
        "DATA_KARYAWAN__NIK",
        "DATA_KARYAWAN__NAMA_LENGKAP",
        "USER__username",
    ]
    list_display = ("nama_lengkap", "username", "role")

    resource_class = DataKaryawanUserResource

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse("admin:auth_user_changelist")

        return mark_safe(
            '<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username)
        )

    def nama_lengkap(self, obj):
        return obj.DATA_KARYAWAN.NAMA_LENGKAP

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ""
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ", "

        return group_display


class DataOrangTuaUserAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "DATA_ORANG_TUA",
        "USER",
    ]
    search_fields = [
        "DATA_ORANG_TUA__NAMA_AYAH",
        "DATA_ORANG_TUA__NAMA_IBU",
        "DATA_ORANG_TUA__NAMA_WALI",
        "USER__username",
    ]
    list_display = ("aksi", "nama_ayah", "nama_ibu", "nama_wali", "username", "role")

    def aksi(self, obj):
        return "Detail"

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse("admin:auth_user_changelist")

        return mark_safe(
            '<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username)
        )

    def nama_ayah(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_AYAH

    def nama_ibu(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_IBU

    def nama_wali(self, obj):
        return obj.DATA_ORANG_TUA.NAMA_WALI

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ""
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ", "

        return group_display


class DataPelatihUserAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "DATA_PELATIH",
        "USER",
    ]
    search_fields = ["DATA_PELATIH__NAMA", "USER__username"]
    list_display = ("aksi", "nama", "username", "role")

    def aksi(self, obj):
        return "Detail"

    def nama(self, obj):
        return obj.DATA_PELATIH.NAMA

    def username(self, obj):
        user = User.objects.get(pk=obj.USER.id)

        base_url = reverse("admin:auth_user_changelist")

        return mark_safe(
            '<a href="%s%d/change">%s</a>' % (base_url, user.id, user.username)
        )

    def role(self, obj):
        groups = obj.USER.groups.all()

        group_display = ""
        for i, group in enumerate(groups):
            if i == len(groups) - 1:
                group_display += group.name
            else:
                group_display += group.name + ", "

        return group_display


admin.site.register(DataSiswaUser, DataSiswaUserAdmin)
admin.site.register(DataOrangTuaUser, DataOrangTuaUserAdmin)
admin.site.register(DataGuruUser, DataGuruUserAdmin)
admin.site.register(DataKaryawanUser, DataKaryawanUserAdmin)
admin.site.register(DataPelatihUser, DataPelatihUserAdmin)
