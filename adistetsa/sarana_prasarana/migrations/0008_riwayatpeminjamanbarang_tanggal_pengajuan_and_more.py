# Generated by Django 4.0 on 2022-02-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0007_alter_pengajuanpeminjamanbarang_tanggal_pengajuan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='riwayatpeminjamanbarang',
            name='TANGGAL_PENGAJUAN',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Ditolak', 'Ditolak'), ('Tenggat', 'Tenggat')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]