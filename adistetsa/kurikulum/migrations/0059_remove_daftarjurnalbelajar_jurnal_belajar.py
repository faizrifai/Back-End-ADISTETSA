# Generated by Django 4.0 on 2022-01-11 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0058_daftarjurnalbelajar_jurnal_belajar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daftarjurnalbelajar',
            name='JURNAL_BELAJAR',
        ),
    ]