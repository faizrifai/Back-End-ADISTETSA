# Generated by Django 4.0 on 2021-12-29 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0010_delete_datasiswauser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datapegawai',
            options={'verbose_name_plural': 'Data Pegawai'},
        ),
        migrations.AlterModelOptions(
            name='datatunjanganpegawai',
            options={'verbose_name_plural': 'Data Tunjangan Pegawai'},
        ),
    ]
