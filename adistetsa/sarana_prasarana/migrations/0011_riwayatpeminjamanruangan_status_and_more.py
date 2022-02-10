# Generated by Django 4.0 on 2022-02-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarana_prasarana', '0010_rename_tanggal_penggunaan_riwayatpeminjamanruangan_tanggal_selesai'),
    ]

    operations = [
        migrations.AddField(
            model_name='riwayatpeminjamanruangan',
            name='STATUS',
            field=models.CharField(choices=[('Diajukan', 'Diajukan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Selesai Dipinjam', 'Selesai Dipinjam'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255),
        ),
        migrations.AlterField(
            model_name='jadwalpenggunaanruangan',
            name='STATUS',
            field=models.CharField(choices=[('Diajukan', 'Diajukan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Selesai Dipinjam', 'Selesai Dipinjam'), ('Ditolak', 'Ditolak')], default='Selesai Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='pengajuanpeminjamanruangan',
            name='STATUS',
            field=models.CharField(choices=[('Diajukan', 'Diajukan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Selesai Dipinjam', 'Selesai Dipinjam'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255),
        ),
    ]
