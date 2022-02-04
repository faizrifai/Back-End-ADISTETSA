# Generated by Django 4.0 on 2022-01-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0023_katalogbukucopy_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='katalogbukucopy',
            name='STATUS_PEMINJAMAN',
        ),
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='peminjamansiswapendek',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(blank=True, choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], max_length=255),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamansiswa',
            name='STATUS_PENGAJUAN',
            field=models.CharField(choices=[('Pengajuan', 'Pengajuan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pengajuan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
