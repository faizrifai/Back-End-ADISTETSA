# Generated by Django 4.0 on 2022-03-24 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0001_initial'),
        ('keuangan', '0002_delete_pembayaran'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PEMBAYARAN_BULAN', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('Semester', 'Semester'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=255)),
                ('TANGGAL_PEMBAYARAN', models.DateField()),
                ('NOMINAL_PEMBAYARAN', models.PositiveIntegerField()),
                ('JENIS_PEMBAYARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keuangan.jenispembayaran')),
                ('NAMA_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa')),
            ],
        ),
    ]
