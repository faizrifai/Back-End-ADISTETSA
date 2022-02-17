# Generated by Django 4.0 on 2022-02-17 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0004_remove_pengajuanpeminjamanruangan_jam_berakhir_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengajuanpeminjamanruangan',
            name='JAM_BERAKHIR',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamanruangan',
            name='JAM_PENGGUNAAN',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
