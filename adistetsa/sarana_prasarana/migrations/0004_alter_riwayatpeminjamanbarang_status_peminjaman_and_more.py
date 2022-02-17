# Generated by Django 4.0 on 2022-02-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0003_pengajuanpeminjamanruangan_tanggal_pengajuan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat'), ('Hilang', 'Hilang'), ('Ditolak', 'Ditolak'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
