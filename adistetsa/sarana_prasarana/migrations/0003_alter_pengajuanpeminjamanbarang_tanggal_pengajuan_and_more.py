# Generated by Django 4.0 on 2022-02-19 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0002_alter_riwayatpeminjamanbarang_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengajuanpeminjamanbarang',
            name='TANGGAL_PENGAJUAN',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanbarang',
            name='TANGGAL_PENGEMBALIAN',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='JAM_BERAKHIR',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='JAM_PENGGUNAAN',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='TANGGAL_BERAKHIR',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='TANGGAL_PEMAKAIAN',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanbarang',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='STATUS',
            field=models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='sarana',
            name='STATUS',
            field=models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Hilang', 'Hilang'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255),
        ),
    ]
