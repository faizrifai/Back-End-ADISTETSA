# Generated by Django 4.0 on 2022-03-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keuangan', '0006_kuitansipembayaranproxy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaran',
            name='PEMBAYARAN_BULAN',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]