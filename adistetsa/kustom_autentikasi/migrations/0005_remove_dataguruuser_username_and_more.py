# Generated by Django 4.0 on 2021-12-29 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kustom_autentikasi', '0004_alter_dataguruuser_data_guru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataguruuser',
            name='USERNAME',
        ),
        migrations.RemoveField(
            model_name='datakaryawanuser',
            name='USERNAME',
        ),
        migrations.RemoveField(
            model_name='dataorangtuauser',
            name='USERNAME',
        ),
    ]