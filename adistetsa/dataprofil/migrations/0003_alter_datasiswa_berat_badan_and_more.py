# Generated by Django 4.0 on 2021-12-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0002_alter_datasiswa_hp_alter_datasiswa_telepon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='BERAT_BADAN',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='JARAK_RUMAH_KESEKOLAH_KM',
            field=models.IntegerField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='JUMLAH_SAUDARA_KANDUNG',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='LINGKAR_KEPALA',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NO_KK',
            field=models.BigIntegerField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NO_KKS',
            field=models.BigIntegerField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='NO_KPS',
            field=models.BigIntegerField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='datasiswa',
            name='TINGGI_BADAN',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]
