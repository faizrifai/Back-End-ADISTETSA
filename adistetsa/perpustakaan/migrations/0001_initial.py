# Generated by Django 4.0 on 2022-02-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dataprofil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstrak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ABSTRAK', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('KODE_AUTHOR', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA_AUTHOR', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DonasiBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DUPLIKAT', models.BigIntegerField()),
                ('TANGGAL_PENERIMAAN', models.DateField(max_length=255)),
                ('CATATAN_DONASI', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KatalogBuku',
            fields=[
                ('REGISTER', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('ISBN', models.CharField(blank=True, max_length=255)),
                ('JUDUL', models.CharField(max_length=255)),
                ('VOLUME', models.CharField(blank=True, max_length=255)),
                ('EDISI', models.CharField(blank=True, max_length=255)),
                ('NOMER_DEWEY', models.CharField(max_length=255)),
                ('KODE_JUDUL', models.CharField(blank=True, max_length=255)),
                ('KOTA_PENERBIT', models.CharField(max_length=255)),
                ('PENERBIT', models.CharField(max_length=255)),
                ('DESKRIPSI_FISIK', models.CharField(max_length=255)),
                ('INDEX', models.CharField(max_length=255)),
                ('BIBLIOGRAPHY', models.CharField(blank=True, max_length=255)),
                ('HARGA', models.CharField(max_length=255)),
                ('DATA_ENTRY', models.DateField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Data Book Main',
            },
        ),
        migrations.CreateModel(
            name='KatalogBukuCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGISTER_COPY', models.CharField(max_length=255)),
                ('STATUS', models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sudah Dikembalikan', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KunjunganGuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TANGGAL_KUNJUNGAN', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='KunjunganSiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TANGGAL_KUNJUNGAN', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lokasi',
            fields=[
                ('KODE_LOKASI', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA_LOKASI', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LokasiSpesifik',
            fields=[
                ('LOKASI_SPESIFIK', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('UNIT', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pendanaan',
            fields=[
                ('KODE_PENDANAAN', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA_PENDANAAN', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PengajuanPeminjamanGuru',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PENGAJUAN', models.DateField()),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Pengajuan', 'Pengajuan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
                ('JANGKA_PEMINJAMAN', models.CharField(blank=True, choices=[('Jangka Pendek', 'Jangka Pendek'), ('Jangka Panjang', 'Jangka Panjang')], max_length=255)),
                ('FILE_TTD_PENGAJUAN', models.FileField(blank=True, max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Guru')),
            ],
        ),
        migrations.CreateModel(
            name='PengajuanPeminjamanSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PENGAJUAN', models.DateField()),
                ('STATUS_PENGAJUAN', models.CharField(choices=[('Pengajuan', 'Pengajuan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pengajuan', max_length=255)),
                ('JANGKA_PEMINJAMAN', models.CharField(blank=True, choices=[('Jangka Pendek', 'Jangka Pendek'), ('Jangka Panjang', 'Jangka Panjang')], max_length=255)),
                ('FILE_TTD_PENGAJUAN', models.FileField(blank=True, max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Siswa')),
            ],
        ),
        migrations.CreateModel(
            name='RiwayatPeminjamanGuru',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PEMINJAMAN', models.DateField()),
                ('TANGGAL_PENGEMBALIAN', models.DateField()),
                ('JANGKA_PEMINJAMAN', models.CharField(blank=True, choices=[('Jangka Pendek', 'Jangka Pendek'), ('Jangka Panjang', 'Jangka Panjang')], max_length=255)),
                ('FILE_TTD_PENGAJUAN', models.FileField(blank=True, max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Guru')),
                ('STATUS_PEMINJAMAN', models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiwayatPeminjamanSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_PEMINJAMAN', models.DateField()),
                ('TANGGAL_PENGEMBALIAN', models.DateField()),
                ('JANGKA_PEMINJAMAN', models.CharField(blank=True, choices=[('Jangka Pendek', 'Jangka Pendek'), ('Jangka Panjang', 'Jangka Panjang')], max_length=255)),
                ('FILE_TTD_PENGAJUAN', models.FileField(blank=True, max_length=255, upload_to='Dokumen_Peminjaman_Jangka_Panjang_Siswa')),
                ('STATUS_PEMINJAMAN', models.CharField(choices=[('Tenggat', 'Tenggat'), ('Ditolak', 'Ditolak'), ('Sudah Dikembalikan', 'Sudah Dikembalikan'), ('Hilang', 'Hilang'), ('Pengajuan', 'Pengajuan'), ('Sedang Dipinjam', 'Sedang Dipinjam')], default='Sedang Dipinjam', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TahunTerbit',
            fields=[
                ('TAHUN_TERBIT', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TipeBahasa',
            fields=[
                ('KODE_BAHASA', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('BAHASA', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipeBuku',
            fields=[
                ('KODE_TIPE', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA_TIPE', models.CharField(max_length=255)),
                ('LAMA_PINJAM', models.CharField(blank=True, max_length=255, null=True)),
                ('DENDA', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipeMedia',
            fields=[
                ('KODE_MEDIA', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA_MEDIA', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'TIPE MEDIA',
            },
        ),
        migrations.AddConstraint(
            model_name='tipemedia',
            constraint=models.UniqueConstraint(fields=('KODE_MEDIA', 'NAMA_MEDIA'), name='perpustakaan_tipemedia_unique'),
        ),
        migrations.AddField(
            model_name='riwayatpeminjamansiswa',
            name='BUKU',
            field=models.ManyToManyField(to='perpustakaan.KatalogBukuCopy'),
        ),
        migrations.AddField(
            model_name='riwayatpeminjamansiswa',
            name='NIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa'),
        ),
        migrations.AddField(
            model_name='riwayatpeminjamanguru',
            name='BUKU',
            field=models.ManyToManyField(to='perpustakaan.KatalogBukuCopy'),
        ),
        migrations.AddField(
            model_name='riwayatpeminjamanguru',
            name='DATA_GURU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamansiswa',
            name='BUKU',
            field=models.ManyToManyField(to='perpustakaan.KatalogBukuCopy'),
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamansiswa',
            name='NIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa'),
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamanguru',
            name='BUKU',
            field=models.ManyToManyField(to='perpustakaan.KatalogBukuCopy'),
        ),
        migrations.AddField(
            model_name='pengajuanpeminjamanguru',
            name='DATA_GURU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='operator',
            name='KODE_OPERATOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='kunjungansiswa',
            name='NIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa'),
        ),
        migrations.AddField(
            model_name='kunjunganguru',
            name='NIP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='katalogbukucopy',
            name='DATA_DONASI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.donasibuku'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='BAHASA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.tipebahasa'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='KODE_AUTHOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.author'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='KODE_LOKASI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.lokasi'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='KODE_MEDIA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.tipemedia'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='KODE_TIPE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.tipebuku'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='LOKASI_SPESIFIK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.lokasispesifik'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='OPERATOR_CODE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.operator'),
        ),
        migrations.AddField(
            model_name='katalogbuku',
            name='TAHUN_TERBIT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.tahunterbit'),
        ),
        migrations.AddField(
            model_name='donasibuku',
            name='KODE_DONASI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.pendanaan'),
        ),
        migrations.AddField(
            model_name='donasibuku',
            name='REGISTER_DONASI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.katalogbuku'),
        ),
        migrations.AddField(
            model_name='abstrak',
            name='REGISTER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.katalogbuku'),
        ),
    ]
