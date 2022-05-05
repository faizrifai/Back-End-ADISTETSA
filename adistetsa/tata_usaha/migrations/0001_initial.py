# Generated by Django 4.0 on 2022-05-05 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprofil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BukuInduk',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_PANGGILAN', models.CharField(max_length=255)),
                ('KEWARGANEGARAAN', models.CharField(default='WNI', max_length=255)),
                ('JUMLAH_SAUDARA_TIRI', models.CharField(blank=True, max_length=255)),
                ('JUMLAH_SAUDARA_ANGKAT', models.CharField(blank=True, max_length=255)),
                ('ANAK_YATIM_PIATU', models.CharField(blank=True, choices=[('ANAK YATIM', 'ANAK YATIM'), ('ANAK PIATU', 'ANAK PIATU'), ('ANAK YATIM PIATU', 'ANAK YATIM PIATU')], max_length=255)),
                ('BAHASA', models.CharField(default='BAHASA INDONESIA', max_length=255)),
                ('GOLONGAN_DARAH', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('PENYAKIT_PERNAH_DIDERITA', models.CharField(blank=True, max_length=255)),
                ('KELAINAN_JASMANI', models.CharField(blank=True, max_length=255)),
                ('TAMATAN_DARI', models.CharField(blank=True, max_length=255)),
                ('TANGGAL_IJAZAH_S', models.DateField(blank=True, null=True)),
                ('NO_IJAZAH_S', models.CharField(blank=True, max_length=255)),
                ('NO_SKHUN_S', models.CharField(blank=True, max_length=255)),
                ('TANGGAL_SKHUN_S', models.DateField(blank=True, null=True)),
                ('LAMA_BELAJAR', models.CharField(blank=True, max_length=255)),
                ('PINDAHAN_DARI', models.CharField(blank=True, max_length=255)),
                ('ALASAN_PINDAHAN', models.CharField(blank=True, max_length=255)),
                ('DITERIMA_DI_KELAS', models.CharField(blank=True, max_length=255)),
                ('KELOMPOK', models.CharField(max_length=255)),
                ('TANGGAL_DITERIMA', models.DateField(blank=True, null=True)),
                ('KESENIAN', models.CharField(blank=True, max_length=255)),
                ('OLAHRAGA', models.CharField(blank=True, max_length=255)),
                ('KEMASYARAKATAN', models.CharField(blank=True, max_length=255)),
                ('LAIN_LAIN', models.CharField(blank=True, max_length=255)),
                ('TANGGAL_MENINGGALKAN_SEKOLAH', models.DateField(blank=True, null=True)),
                ('ALASAN_MENINGGALKAN_SEKOLAH', models.CharField(blank=True, max_length=255)),
                ('TAMAT_BELAJAR', models.CharField(blank=True, max_length=255)),
                ('TANGGAL_NO_IJAZAH', models.DateField(blank=True, null=True)),
                ('NO_IJAZAH', models.CharField(blank=True, max_length=255)),
                ('TANGGAL_NO_SKHUN', models.DateField(blank=True, null=True)),
                ('NO_SKHUN', models.CharField(blank=True, max_length=255)),
                ('RATA_RATA_NUN', models.CharField(blank=True, max_length=255)),
                ('MELANJUTKAN_KE', models.CharField(blank=True, max_length=255)),
                ('BEKERJA_DI', models.CharField(blank=True, max_length=255)),
                ('GENERATE', models.BooleanField(default=False)),
                ('HASIL_EXPORT', models.FileField(blank=True, max_length=255, upload_to='DataTataUsaha')),
                ('NIS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa')),
                ('ORANG_TUA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataorangtua')),
            ],
            options={
                'verbose_name_plural': 'Buku Induk',
            },
        ),
        migrations.CreateModel(
            name='MutasiKeluar',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_SISWA', models.CharField(max_length=255)),
                ('KELAS', models.CharField(max_length=255)),
                ('NO_INDUK', models.CharField(max_length=255)),
                ('PINDAH_KE', models.CharField(max_length=255)),
                ('TANGGAL_SURAT', models.DateField()),
                ('NO_SURAT', models.CharField(max_length=255)),
                ('BULAN', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=255)),
                ('TAHUN', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Mutasi Keluar',
            },
        ),
        migrations.CreateModel(
            name='MutasiMasuk',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_SISWA', models.CharField(max_length=255)),
                ('ASAL_SEKOLAH', models.CharField(max_length=255)),
                ('NO_INDUK_ASAL', models.CharField(max_length=255)),
                ('ALAMAT', models.CharField(max_length=255)),
                ('KELAS', models.CharField(max_length=255)),
                ('NO_INDUK_BARU', models.CharField(max_length=255)),
                ('TANGGAL_SURAT', models.DateField(max_length=255)),
                ('NO_SURAT', models.CharField(max_length=255)),
                ('BULAN', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=255)),
                ('TAHUN', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Mutasi Masuk',
            },
        ),
        migrations.CreateModel(
            name='DataBeasiswaSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TAHUN', models.CharField(max_length=255)),
                ('KELAS', models.CharField(max_length=255)),
                ('DARI', models.CharField(max_length=255)),
                ('BUKU_INDUK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.bukuinduk')),
            ],
        ),
    ]
