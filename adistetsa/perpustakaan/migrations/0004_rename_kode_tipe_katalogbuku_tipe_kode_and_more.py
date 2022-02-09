# Generated by Django 4.0 on 2022-02-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_alter_katalogbukucopy_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='katalogbuku',
            old_name='KODE_TIPE',
            new_name='TIPE_KODE',
        ),
        migrations.AlterField(
            model_name='katalogbukucopy',
            name='STATUS',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat')], default='Sudah Dikembalikan', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamanguru',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat')], default='Sedang Dipinjam', max_length=255),
        ),
        migrations.AlterField(
            model_name='riwayatpeminjamansiswa',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sedang Dipinjam', 'Sedang Dipinjam'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat')], default='Sedang Dipinjam', max_length=255),
        ),
    ]
