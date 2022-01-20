# Generated by Django 4.0 on 2022-01-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0017_rename_katalokbukucopy_katalogbukucopy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peminjamansiswapendek',
            name='BUKU',
            field=models.ManyToManyField(to='perpustakaan.KatalogBukuCopy'),
        ),
        migrations.AlterField(
            model_name='peminjamansiswapendek',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Sedang Dipinjam', 'Sedang Dipinjam'), ('Tenggat', 'Tenggat')], max_length=255),
        ),
    ]
