# Generated by Django 4.0 on 2022-02-16 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0081_nilairaport'),
        ('dataprofil', '0003_datapelatih'),
        ('kesiswaan', '0014_delete_programkerjaekskul'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramKerjaEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('FILE_PROGRAM_KERJA', models.FileField(max_length=255, upload_to='ProgramKerjaEkskul')),
                ('NAMA_EKSKUL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kesiswaan.katalogekskul')),
                ('PELATIH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datapelatih')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
        ),
    ]
