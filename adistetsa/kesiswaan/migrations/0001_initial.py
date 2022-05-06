# Generated by Django 4.0 on 2022-05-06 04:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprofil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsensiEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(choices=[('Hadir', 'Hadir'), ('Izin', 'Izin'), ('Sakit', 'Sakit'), ('Tanpa Keterangan', 'Tanpa Keterangan')], default='Hadir', max_length=255)),
                ('FILE_KETERANGAN', models.FileField(blank=True, max_length=255, upload_to='AbsensiEkskul')),
            ],
        ),
        migrations.CreateModel(
            name='AnggotaEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('STATUS', models.CharField(choices=[('Aktif', 'Aktif'), ('Nonaktif', 'Nonaktif')], default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DaftarJurnalEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='JadwalEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('HARI', models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jum`at', 'Jum`at'), ('Sabtu', 'Sabtu')], max_length=255)),
                ('WAKTU_MULAI', models.TimeField()),
                ('WAKTU_BERAKHIR', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JurnalEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PERTEMUAN', models.CharField(max_length=255)),
                ('TANGGAL_MELATIH', models.DateField(default=datetime.date.today)),
                ('DESKRIPSI_KEGIATAN', models.TextField()),
                ('FILE_DOKUMENTASI', models.FileField(max_length=255, upload_to='JurnalEkskul')),
            ],
        ),
        migrations.CreateModel(
            name='KatalogEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255)),
                ('KATEGORI', models.CharField(choices=[('Wajib', 'Wajib'), ('Pilihan', 'Pilihan'), ('Mandiri', 'Mandiri')], max_length=255)),
                ('DESKRIPSI', models.CharField(max_length=255)),
                ('DOKUMENTASI', models.ImageField(blank=True, max_length=255, upload_to='KatalogEkskul')),
            ],
        ),
        migrations.CreateModel(
            name='KategoriProgramKebaikan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Kategori Program Kebaikan',
                'ordering': ['NAMA'],
            },
        ),
        migrations.CreateModel(
            name='NilaiEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PREDIKAT', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=255)),
                ('DESKRIPSI', models.TextField(max_length=1020)),
            ],
        ),
        migrations.CreateModel(
            name='PelanggaranSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('POIN', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Pelanggaran Siswa',
            },
        ),
        migrations.CreateModel(
            name='PengajuanEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PENGAJUAN', models.DateField(default=datetime.date.today)),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Pengajuan', 'Pengajuan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pengajuan', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PengajuanLaporanPelanggaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BUKTI_PELANGGARAN', models.FileField(max_length=255, upload_to='BuktiPelanggaran')),
                ('TANGGAL_PENGAJUAN', models.DateTimeField(default=django.utils.timezone.now)),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Diajukan', 'Diajukan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Pengajuan Laporan Pelanggaran',
            },
        ),
        migrations.CreateModel(
            name='PengajuanProgramKebaikan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BUKTI_PROGRAM_KEBAIKAN', models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')),
                ('TANGGAL_PENGAJUAN', models.DateTimeField(default=django.utils.timezone.now)),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Diajukan', 'Diajukan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Pengajuan Program Kebaikan',
            },
        ),
        migrations.CreateModel(
            name='PoinProgramKebaikan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(max_length=255)),
                ('POIN', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Poin Program Kebaikan',
                'ordering': ['KETERANGAN'],
            },
        ),
        migrations.CreateModel(
            name='ProgramKebaikan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Program Kebaikan',
                'ordering': ['KETERANGAN'],
            },
        ),
        migrations.CreateModel(
            name='ProgramKerjaEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('FILE_PROGRAM_KERJA', models.FileField(max_length=255, upload_to='ProgramKerjaEkskul')),
            ],
        ),
        migrations.CreateModel(
            name='RiwayatProgramKebaikan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BUKTI_PROGRAM_KEBAIKAN', models.FileField(max_length=255, upload_to='BuktiProgramKebaikan')),
                ('TANGGAL_PENGAJUAN', models.DateTimeField(default=django.utils.timezone.now)),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Diajukan', 'Diajukan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
                ('DATA_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa')),
                ('JENIS_PROGRAM_KEBAIKAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kesiswaan.poinprogramkebaikan')),
            ],
            options={
                'verbose_name_plural': 'Riwayat Program Kebaikan',
            },
        ),
        migrations.CreateModel(
            name='RiwayatLaporanPelanggaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BUKTI_PELANGGARAN', models.FileField(max_length=255, upload_to='BuktiPelanggaran')),
                ('TANGGAL_PENGAJUAN', models.DateTimeField(default=django.utils.timezone.now)),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Diajukan', 'Diajukan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
                ('DATA_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa')),
            ],
            options={
                'verbose_name_plural': 'Riwayat Laporan Pelanggaran',
            },
        ),
    ]
