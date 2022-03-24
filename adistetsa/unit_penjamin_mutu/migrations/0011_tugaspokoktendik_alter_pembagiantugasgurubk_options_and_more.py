# Generated by Django 4.0 on 2022-03-21 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0002_alter_dataanakguru_tanggal_lahir_and_more'),
        ('unit_penjamin_mutu', '0010_alter_bahanbukuupm_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='TugasPokokTendik',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('JENIS_TUGAS', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Tugas Pokok Tendik',
            },
        ),
        migrations.AlterModelOptions(
            name='pembagiantugasgurubk',
            options={'verbose_name_plural': 'Pembagian Tugas Guru BK'},
        ),
        migrations.CreateModel(
            name='PembagianTugasPokokTambahanTendik',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TUGAS_TAMBAHAN', models.TextField()),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('TUGAS_POKOK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_penjamin_mutu.tugaspokoktendik')),
            ],
            options={
                'verbose_name_plural': 'Pembagian Tugas Pokok Tenaga Pendidikan',
            },
        ),
    ]
