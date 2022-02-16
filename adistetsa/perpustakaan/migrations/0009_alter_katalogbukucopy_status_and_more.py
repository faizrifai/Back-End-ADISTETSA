# Generated by Django 4.0 on 2022-02-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0008_alter_katalogbukucopy_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
