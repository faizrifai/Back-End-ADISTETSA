# Generated by Django 4.0 on 2022-02-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0078_absensisiswa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absensisiswa',
            name='FILE_KETERANGAN',
            field=models.FileField(blank=True, max_length=255, upload_to='AbsensiSiswa'),
        ),
    ]