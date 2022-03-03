# Generated by Django 4.0 on 2022-03-03 05:34

import adistetsa.custom_function
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0003_datasiswa_alasan_layak_pip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataguru',
            name='DUSUN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='KECAMATAN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='KELURAHAN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='KEWARGANEGARAAN',
            field=models.CharField(default='Indonesia', max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='KOTA',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='LINTANG_1',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='LINTANG_2',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NAMA_IBU_KANDUNG',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NAMA_LENGKAP',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NAMA_PASANGAN',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NAMA_SEKOLAH',
            field=models.CharField(default='SMA NEGERI 4 MALANG', max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar_dengan_angka]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NAMA_WAJIB_PAJAK',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.paksa_huruf_besar]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NIGB',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NIK',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NIP',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NIP_PASANGAN',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NIY',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NPSN',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NSS',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='NUPTK',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.validasi_integer]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='PEKERJAAN_PASANGAN',
            field=models.CharField(blank=True, max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='PROVINSI',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='STATUS_KAWIN',
            field=models.CharField(choices=[('Kawin', 'Kawin'), ('Belum Kawin', 'Belum Kawin'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')], max_length=11),
        ),
        migrations.AlterField(
            model_name='dataguru',
            name='TEMPAT_LAHIR',
            field=models.CharField(max_length=225, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat]),
        ),
        migrations.AlterField(
            model_name='datakaryawan',
            name='STATUS_KAWIN',
            field=models.CharField(choices=[('Kawin', 'Kawin'), ('Belum Kawin', 'Belum Kawin'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')], max_length=11),
        ),
    ]
