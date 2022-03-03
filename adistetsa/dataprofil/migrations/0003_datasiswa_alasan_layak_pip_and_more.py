# Generated by Django 4.0 on 2022-03-02 08:52

import adistetsa.custom_function
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0002_alter_datasiswa_nis'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasiswa',
            name='ALASAN_LAYAK_PIP',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='ALAT_TRANSPORTASI',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='NAMA_KIP',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='NOMOR_KIP',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='DUSUN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='HP',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='KECAMATAN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='KELURAHAN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NAMA',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NIPD',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NISN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NO_KPS',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='TELEPON',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='TEMPAT_LAHIR',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
    ]