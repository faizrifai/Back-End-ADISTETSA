# Generated by Django 4.0 on 2022-03-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keuangan', '0007_alter_pembayaran_pembayaran_bulan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KuitansiPembayaranProxy',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='GENERATE',
            field=models.BooleanField(default=False),
        ),
    ]
