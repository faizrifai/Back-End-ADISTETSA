# Generated by Django 4.0 on 2022-01-12 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0063_alter_jurnalbelajar_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='JADWAL_MENGAJAR',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.jadwalmengajar'),
            preserve_default=False,
        ),
    ]
