# Generated by Django 4.0 on 2022-01-08 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0017_datasemester_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='NAMA',
            field=models.CharField(max_length=255, verbose_name='Mata Pelajaran'),
        ),
    ]
