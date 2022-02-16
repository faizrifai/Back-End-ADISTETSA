# Generated by Django 4.0 on 2022-02-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0009_alter_katalogbukucopy_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Ditolak', 'Ditolak')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Ditolak', 'Ditolak')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Ditolak', 'Ditolak')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
