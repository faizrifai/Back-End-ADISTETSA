# Generated by Django 4.0 on 2022-02-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0003_remove_pengajuanpeminjamanruanganpendek_hari_penggunaan'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwalpenggunaanruangan',
            name='HARI',
            field=models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jum`at', 'Jum`at'), ('Sabtu', 'Sabtu')], default=0, max_length=255),
            preserve_default=False,
        ),
    ]
