# Generated by Django 4.0 on 2022-02-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0004_jadwalpenggunaanruangan_hari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengajuanpeminjamanruanganpendek',
            name='RUANGAN',
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamanruanganpendek',
            name='RUANGAN',
            field=models.ManyToManyField(to='sarana_prasarana.JadwalPenggunaanRuangan'),
        ),
    ]
