# Generated by Django 4.0 on 2022-02-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absensisiswa',
            name='KETERANGAN',
            field=models.CharField(choices=[('Hadir', 'Hadir'), ('Izin', 'Izin'), ('Sakit', 'Sakit'), ('Tanpa Keterangan', 'Tanpa Keterangan')], default='Hadir', max_length=255),
        ),
    ]
