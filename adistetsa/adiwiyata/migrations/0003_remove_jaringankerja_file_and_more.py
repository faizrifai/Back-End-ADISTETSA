# Generated by Django 4.0 on 2022-03-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adiwiyata', '0002_remove_jaringankerja_file_dokumentasi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jaringankerja',
            name='FILE',
        ),
        migrations.AddField(
            model_name='jaringankerja',
            name='FILE_DOKUMENTASI',
            field=models.FileField(default='', max_length=255, upload_to='JaringanKerja/Dokumentasi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jaringankerja',
            name='FILE_MOU',
            field=models.FileField(default='', max_length=255, upload_to='JaringanKerja/MOU'),
            preserve_default=False,
        ),
    ]
