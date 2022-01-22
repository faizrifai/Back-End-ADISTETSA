# Generated by Django 4.0 on 2022-01-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0016_alter_peminjamansiswapendek_status_peminjaman_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KatalokBukuCopy',
            new_name='KatalogBukuCopy',
        ),
        migrations.AlterField(
            model_name='peminjamansiswapendek',
            name='STATUS_PEMINJAMAN',
            field=models.CharField(choices=[('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Tenggat', 'Tenggat'), ('Sedang Dipinjam', 'Sedang Dipinjam')], max_length=255),
        ),
    ]
