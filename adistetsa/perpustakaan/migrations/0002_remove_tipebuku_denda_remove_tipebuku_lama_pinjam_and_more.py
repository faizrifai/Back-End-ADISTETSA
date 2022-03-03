# Generated by Django 4.0 on 2022-03-03 06:55

import adistetsa.custom_function
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipebuku',
            name='DENDA',
        ),
        migrations.RemoveField(
            model_name='tipebuku',
            name='LAMA_PINJAM',
        ),
        migrations.AlterField(
            model_name='tipebahasa',
            name='BAHASA',
            field=models.CharField(max_length=255, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='tipebuku',
            name='NAMA_TIPE',
            field=models.CharField(max_length=255, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
    ]
