# Generated by Django 4.0 on 2022-02-08 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kesiswaan', '0004_kategoriprogramkebaikan_pengajuanprogramkebaikan_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoriprogramkebaikan',
            options={'ordering': ['NAMA'], 'verbose_name_plural': 'Kategori Program Kebaikan'},
        ),
        migrations.AlterModelOptions(
            name='pelanggaransiswa',
            options={'verbose_name_plural': 'Pelanggaran Siswa'},
        ),
        migrations.AlterModelOptions(
            name='pengajuanlaporanpelanggaran',
            options={'verbose_name_plural': 'Pengajuan Laporan Pelanggaran'},
        ),
        migrations.AlterModelOptions(
            name='pengajuanprogramkebaikan',
            options={'verbose_name_plural': 'Pengajuan Program Kebaikan'},
        ),
        migrations.AlterModelOptions(
            name='riwayatlaporanpelanggaran',
            options={'verbose_name_plural': 'Riwayat Laporan Pelanggaran'},
        ),
        migrations.AlterField(
            model_name='pengajuanprogramkebaikan',
            name='JENIS_PROGRAM_KEBAIKAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kesiswaan.poinprogramkebaikan'),
        ),
    ]