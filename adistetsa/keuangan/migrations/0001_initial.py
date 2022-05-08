# Generated by Django 4.0 on 2022-05-08 09:27

from django.db import migrations, models
import django.db.models.deletion
import utility.custom_function


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kurikulum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PEMBAYARAN', models.DateField()),
                ('PEMBAYARAN_DPSM_RUTIN', models.CharField(blank=True, default=0, max_length=1024, validators=[utility.custom_function.validasi_integer])),
                ('PEMBAYARAN_DPSM_INSINDENTAL', models.CharField(blank=True, default=0, max_length=1024, validators=[utility.custom_function.validasi_integer])),
                ('BIMBEL', models.CharField(blank=True, default=0, max_length=1024, validators=[utility.custom_function.validasi_integer])),
                ('NOMINAL_SPP', models.CharField(blank=True, default=0, max_length=1024, validators=[utility.custom_function.validasi_integer])),
                ('PEMBAYARAN_SPP', models.CharField(blank=True, default='', max_length=1024)),
                ('GENERATE', models.BooleanField(default=False)),
                ('KUITANSI', models.FileField(blank=True, max_length=255, upload_to='DataKeuangan')),
                ('NAMA_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa')),
            ],
            options={
                'verbose_name_plural': 'Pembayaran',
            },
        ),
    ]
