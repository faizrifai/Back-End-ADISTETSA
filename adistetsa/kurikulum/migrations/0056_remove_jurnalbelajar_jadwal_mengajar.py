# Generated by Django 4.0 on 2022-01-11 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0055_remove_poinpelanggaran_kategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurnalbelajar',
            name='JADWAL_MENGAJAR',
        ),
    ]