# Generated by Django 4.0 on 2022-02-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0012_alter_riwayatpeminjamanbarang_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]