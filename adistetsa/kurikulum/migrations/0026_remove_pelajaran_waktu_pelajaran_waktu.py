# Generated by Django 4.0 on 2022-01-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0025_alter_absensisiswa_file_dokumen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelajaran',
            name='WAKTU',
        ),
        migrations.AddField(
            model_name='pelajaran',
            name='WAKTU',
            field=models.ManyToManyField(to='kurikulum.WaktuPelajaran'),
        ),
    ]
