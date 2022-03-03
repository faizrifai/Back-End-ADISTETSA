# Generated by Django 4.0 on 2022-03-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0015_alter_riwayatpeminjamanbarang_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
