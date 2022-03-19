# Generated by Django 4.0 on 2022-03-19 03:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataAlumni',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_SISWA', models.CharField(max_length=255)),
                ('KELAS', models.CharField(max_length=255)),
                ('NISN', models.CharField(max_length=255)),
                ('NIS', models.CharField(max_length=255)),
                ('TAHUN_AJARAN', models.CharField(max_length=255)),
                ('NAMA_PT', models.CharField(blank=True, max_length=255)),
                ('PROGRAM_STUDI', models.CharField(blank=True, max_length=255)),
                ('MEDIA_SOSIAL', models.CharField(blank=True, max_length=255)),
                ('EMAIL', models.EmailField(blank=True, max_length=255)),
                ('ALAMAT', models.CharField(blank=True, max_length=255)),
                ('TEMPAT_BEKERJA', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Data Alumni',
            },
        ),
        migrations.CreateModel(
            name='KatalogKonselor',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(blank=True, max_length=255)),
                ('KOMPETENSI', models.CharField(blank=True, max_length=255)),
                ('ALUMNUS', models.CharField(blank=True, max_length=255)),
                ('WHATSAPP', models.URLField(blank=True, max_length=255)),
                ('CONFERENCE', models.URLField(blank=True, max_length=255)),
                ('FOTO', models.ImageField(blank=True, max_length=255, upload_to='Foto_Profil_BK')),
                ('STATUS', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Offline', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Katalog Konselor',
            },
        ),
        migrations.CreateModel(
            name='Konsultasi',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_KONSULTASI', models.DateField(default=datetime.date.today, max_length=255)),
                ('JAM_AWAL', models.TimeField()),
                ('JAM_AKHIR', models.TimeField()),
                ('JENIS_MASALAH', models.CharField(choices=[('Karier', 'Karier'), ('Pribadi', 'Pribadi'), ('Sosial', 'Sosial'), ('Belajar', 'Belajar')], max_length=255)),
                ('RATING', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('STATUS', models.CharField(choices=[('Dijadwalkan', 'Dijadwalkan'), ('Selesai', 'Selesai'), ('Diajukan', 'Diajukan'), ('Telah Mengisi Feedback', 'Telah Mengisi Feedback'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
                ('KRITIK_SARAN', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Konsultasi',
            },
        ),
        migrations.CreateModel(
            name='PeminatanLintasMinat',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KATEGORI', models.CharField(choices=[('Angket Peminatan', 'Angket Peminatan'), ('Angket Lintas Minat', 'Angket Lintas Minat'), ('Angket Data Diri', 'Angket Data Diri')], max_length=255)),
                ('FILE', models.FileField(max_length=255, upload_to='Dokumen_Peminatan_Lintas_Minat')),
            ],
            options={
                'verbose_name_plural': 'Peminatan dan Lintas Minat',
            },
        ),
    ]
