# Generated by Django 4.0 on 2022-03-28 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0001_initial'),
        ('keuangan', '0009_remove_pembayaran_nama_siswa_pembayaran_data_siswa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='DATA_SISWA',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='KELAS',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='NAMA_SISWA',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa'),
            preserve_default=False,
        ),
    ]
