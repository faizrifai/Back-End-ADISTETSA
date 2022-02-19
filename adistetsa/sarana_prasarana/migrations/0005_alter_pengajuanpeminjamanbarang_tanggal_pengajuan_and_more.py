# Generated by Django 4.0 on 2022-02-19 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0004_alter_pengajuanpeminjamanbarang_tanggal_pengajuan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengajuanpeminjamanbarang',
            name='TANGGAL_PENGAJUAN',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='TANGGAL_PENGAJUAN',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
