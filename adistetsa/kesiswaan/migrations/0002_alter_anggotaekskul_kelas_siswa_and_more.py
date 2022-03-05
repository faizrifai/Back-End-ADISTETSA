# Generated by Django 4.0 on 2022-03-05 03:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0002_alter_jurnalbelajar_tanggal_mengajar'),
        ('kesiswaan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggotaekskul',
            name='KELAS_SISWA',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa'),
        ),
        migrations.AlterField(
            model_name='jurnalekskul',
            name='TANGGAL_MELATIH',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='pengajuanekskul',
            name='TANGGAL_PENGAJUAN',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddConstraint(
            model_name='jadwalekskul',
            constraint=models.UniqueConstraint(fields=('PELATIH', 'EKSKUL', 'HARI', 'TAHUN_AJARAN', 'WAKTU_MULAI', 'WAKTU_BERAKHIR'), name='kesiswaan_jadwalekskul_unique'),
        ),
        migrations.AddConstraint(
            model_name='programkerjaekskul',
            constraint=models.UniqueConstraint(fields=('PELATIH', 'EKSKUL', 'TAHUN_AJARAN'), name='kesiswaan_programkerjaekskul_unique'),
        ),
    ]
