# Generated by Django 4.0 on 2022-02-09 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0004_rename_kode_tipe_katalogbuku_tipe_kode_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='katalogbuku',
            old_name='TIPE_KODE',
            new_name='KODE_TIPE',
        ),
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Hilang', 'Hilang'), ('Tenggat', 'Tenggat'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Pengajuan', 'Pengajuan')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
