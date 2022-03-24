# Generated by Django 4.0 on 2022-03-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0002_alter_jurnalbelajar_tanggal_mengajar'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='offeringkelas',
            constraint=models.UniqueConstraint(fields=('KELAS', 'OFFERING'), name='kurikulum_offeringkelas_unique'),
        ),
    ]
