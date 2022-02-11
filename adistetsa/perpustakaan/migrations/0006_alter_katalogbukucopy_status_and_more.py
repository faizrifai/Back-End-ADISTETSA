# Generated by Django 4.0 on 2022-02-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0005_alter_katalogbukucopy_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
