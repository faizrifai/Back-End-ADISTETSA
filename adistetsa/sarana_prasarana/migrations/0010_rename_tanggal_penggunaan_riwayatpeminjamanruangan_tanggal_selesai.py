# Generated by Django 4.0 on 2022-02-09 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0009_pengajuanpeminjamanruangan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riwayatpeminjamanruangan',
            old_name='TANGGAL_PENGGUNAAN',
            new_name='TANGGAL_SELESAI',
        ),
    ]