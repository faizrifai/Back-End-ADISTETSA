# Generated by Django 4.0 on 2022-01-13 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataguru',
            old_name='NO_TELP',
            new_name='HP',
        ),
        migrations.RenameField(
            model_name='datakaryawan',
            old_name='NO_TELP',
            new_name='HP',
        ),
    ]
