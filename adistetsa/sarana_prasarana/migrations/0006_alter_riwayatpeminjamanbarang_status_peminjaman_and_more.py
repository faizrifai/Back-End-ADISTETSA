# Generated by Django 4.0 on 2022-02-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0005_alter_riwayatpeminjamanbarang_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Pengajuan', 'Pengajuan'), ('Hilang', 'Hilang')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Ditolak', 'Ditolak'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Pengajuan', 'Pengajuan'), ('Hilang', 'Hilang')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
