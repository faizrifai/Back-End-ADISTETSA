# Generated by Django 4.0 on 2022-01-19 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0075_delete_bulanminggu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JadwalMingguEfektifNonEfektif',
        ),
        migrations.DeleteModel(
            name='TipeKelas',
        ),
        migrations.AlterModelOptions(
            name='jadwalpekanaktif',
            options={'verbose_name_plural': 'Jadwal Pekan Aktif'},
        ),
        migrations.AlterModelOptions(
            name='jadwalpekanefektifsemester',
            options={'verbose_name_plural': 'Jadwal Pekan Efektif Semester'},
        ),
        migrations.AlterModelOptions(
            name='jadwalpekantidakefektif',
            options={'verbose_name_plural': 'Jadwal Pekan Tidak Efektif'},
        ),
        migrations.AlterModelOptions(
            name='namaofferingkelas',
            options={'verbose_name_plural': 'Nama Offering Kelas'},
        ),
        migrations.AlterModelOptions(
            name='offeringkelas',
            options={'verbose_name_plural': 'Offering Kelas'},
        ),
    ]
