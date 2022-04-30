# Generated by Django 4.0 on 2022-04-27 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprofil', '0001_initial'),
        ('kurikulum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenisBidang',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KODE_BIDANG', models.PositiveIntegerField()),
                ('NAMA_BIDANG', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Jenis Bidang',
            },
        ),
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
        migrations.CreateModel(
            name='TugasTambahanKepanitiaanTendik',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('SUB_BIDANG', models.CharField(blank=True, max_length=255)),
                ('TUGAS', models.CharField(max_length=255)),
                ('BIDANG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_penjamin_mutu.jenisbidang')),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
            options={
                'verbose_name_plural': 'Pembagian Tugas Tambahan dan Kepanitiaan Tendik',
            },
        ),
        migrations.CreateModel(
            name='RincianTugasPokokTambahanTendik',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TUGAS_POKOK', models.TextField()),
                ('TUGAS_TAMBAHAN', models.TextField()),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
            options={
                'verbose_name_plural': 'Rincian Tugas Pokok Tenaga Pendidikan',
            },
        ),
        migrations.CreateModel(
            name='PembagianTugasPokokTambahanTendik',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TUGAS_TAMBAHAN', models.TextField()),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
                ('TUGAS_POKOK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_penjamin_mutu.tugaspokoktendik')),
            ],
            options={
                'verbose_name_plural': 'Pembagian Tugas Pokok Tenaga Pendidikan',
            },
        ),
        migrations.CreateModel(
            name='PembagianTugasGuruTIK',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN_TUGAS', models.TextField(blank=True)),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('DATA_KELAS', models.ManyToManyField(to='kurikulum.OfferingKelas')),
                ('SEMESTER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
            options={
                'verbose_name_plural': 'Pembagian Tugas Guru TIK',
            },
        ),
        migrations.CreateModel(
            name='PembagianTugasGuruBK',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN_TUGAS', models.TextField(blank=True)),
                ('DATA_GURU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('DATA_KELAS', models.ManyToManyField(to='kurikulum.OfferingKelas')),
                ('SEMESTER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
            options={
                'verbose_name_plural': 'Pembagian Tugas Guru BK',
            },
        ),
        migrations.CreateModel(
            name='BahanBukuUPM',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KATEGORI', models.CharField(choices=[('Pembagian Jadwal Mengajar', 'Pembagian Jadwal Mengajar'), ('Rekapitulasi Jumlah Jam Mengajar', 'Rekapitulasi Jumlah Jam Mengajar'), ('Pembagian Tugas BK Semester', 'Pembagian Tugas BK Semester'), ('Pembagian Tugas TIK Semester', 'Pembagian Tugas TIK Semester'), ('Pembagian Tugas Pokok dan Tambahan Tenaga Kependidikan', 'Pembagian Tugas Pokok dan Tambahan Tenaga Kependidikan'), ('Rincian Tugas Pokok dan Tambahan Tenaga Kependidikan', 'Rincian Tugas Pokok dan Tambahan Tenaga Kependidikan'), ('Lampiran Tugas Tambahan dan Kepanitiaan', 'Lampiran Tugas Tambahan dan Kepanitiaan')], default='', max_length=255)),
                ('GENERATE', models.BooleanField()),
                ('FILE', models.FileField(blank=True, max_length=255, upload_to='FileBahanBuku')),
                ('SEMESTER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester')),
                ('TAHUN_AJARAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran')),
            ],
            options={
                'verbose_name_plural': 'Bahan Buku UPM',
            },
        ),
    ]
