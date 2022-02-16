# Generated by Django 4.0 on 2022-02-16 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0081_nilairaport'),
        ('kesiswaan', '0016_rename_nama_ekskul_programkerjaekskul_ekskul'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggotaekskul',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuanekskul',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
            preserve_default=False,
        ),
    ]
