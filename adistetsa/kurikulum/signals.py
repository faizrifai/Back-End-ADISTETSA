from django.db.models.signals import post_save, pre_save

from .models import (
    AbsensiSiswa,
    DaftarJurnalBelajar,
    DataSemester,
    JadwalMengajar,
    JurnalBelajar,
    KelasSiswa,
    Raport,
)


def post_save_buku_induk(sender, instance, created, **kwargs):
    try:
        kelas_siswa = KelasSiswa.objects.filter(NIS=instance.NIS)
        for siswa in kelas_siswa:
            for i in range(2):
                if i == 0:
                    semester = "I"
                elif i == 1:
                    semester = "II"
                Raport.objects.update_or_create(
                    KELAS_SISWA=siswa,
                    SEMESTER=DataSemester.objects.get(KE=semester),
                    BUKU_INDUK=instance,
                )
    except Exception as e:
        print(str(e))


post_save.connect(
    post_save_buku_induk,
    sender="tata_usaha.BukuInduk",
    dispatch_uid="create_raport_data",
)


def post_save_jadwal_mengajar(sender, instance, **kwargs):
    try:
        DaftarJurnalBelajar.objects.get_or_create(
            GURU=instance.GURU,
            MATA_PELAJARAN=instance.MATA_PELAJARAN,
            KELAS=instance.KELAS,
            SEMESTER=instance.SEMESTER,
        )

    except Exception as e:
        print(str(e))


post_save.connect(
    post_save_jadwal_mengajar,
    sender=JadwalMengajar,
    dispatch_uid="create_daftar_jurnal_belajar",
)


def post_save_jurnal_belajar(sender, instance, created, **kwargs):
    try:
        kelas_siswa = KelasSiswa.objects.filter(KELAS=instance.DAFTAR.KELAS)
        for siswa in kelas_siswa:
            AbsensiSiswa.objects.update_or_create(
                NIS=siswa.NIS, JURNAL_BELAJAR=instance
            )
    except Exception as e:
        print(str(e))


post_save.connect(
    post_save_jurnal_belajar, sender=JurnalBelajar, dispatch_uid="create_absensi_siswa"
)


def pre_save_jurnal_belajar(sender, instance, **kwargs):
    try:
        daftar = DaftarJurnalBelajar.objects.get(ID=instance.DAFTAR.ID)
        print(daftar)
        instance.GURU = daftar.GURU
    except Exception as e:
        print(str(e))


pre_save.connect(
    pre_save_jurnal_belajar,
    sender=JurnalBelajar,
    dispatch_uid="set_guru_daftar_jurnal_belajar",
)
