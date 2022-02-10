# Generated by Django 4.0 on 2022-02-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_alter_katalogbukucopy_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
