# Generated by Django 4.0 on 2022-03-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubungan_masyarakat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukutamu',
            name='HARI',
            field=models.CharField(max_length=255),
        ),
    ]