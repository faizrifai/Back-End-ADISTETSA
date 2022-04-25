# Generated by Django 4.0 on 2022-04-24 20:16

import adistetsa.custom_function
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprofil', '0001_initial'),
        ('tata_usaha', '0002_alter_mutasikeluar_bulan_alter_mutasimasuk_bulan'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsensiSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(choices=[('Hadir', 'Hadir'), ('Izin', 'Izin'), ('Sakit', 'Sakit'), ('Tanpa Keterangan', 'Tanpa Keterangan')], default='Hadir', max_length=255)),
                ('FILE_KETERANGAN', models.FileField(blank=True, max_length=255, upload_to='AbsensiSiswa')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
            ],
            options={
                'ordering': ('-change_date',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DaftarJurnalBelajar',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Daftar Jurnal Belajar',
                'ordering': ['KELAS'],
            },
        ),
        migrations.CreateModel(
            name='DataSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KE', models.CharField(choices=[('I', 'I'), ('II', 'II')], max_length=255)),
                ('NAMA', models.CharField(blank=True, max_length=255, verbose_name='SEMESTER')),
            ],
            options={
                'verbose_name_plural': 'Semester',
                'ordering': ['KE'],
            },
        ),
        migrations.CreateModel(
            name='JadwalMengajar',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('HARI', models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jum`at', 'Jum`at'), ('Sabtu', 'Sabtu')], max_length=255)),
                ('JUMLAH_WAKTU', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Jadwal Mengajar',
                'ordering': ['TAHUN_AJARAN', 'KELAS', 'HARI', 'JUMLAH_WAKTU'],
            },
        ),
        migrations.CreateModel(
            name='JadwalPekanAktif',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Jadwal Pekan Aktif',
            },
        ),
        migrations.CreateModel(
            name='JadwalPekanEfektifSemester',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BULAN', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=255)),
                ('JUMLAH_MINGGU', models.IntegerField()),
                ('JUMLAH_MINGGU_EFEKTIF', models.IntegerField()),
                ('JUMLAH_MINGGU_TIDAK_EFEKTIF', models.IntegerField()),
                ('KETERANGAN', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Jadwal Pekan Efektif Semester',
            },
        ),
        migrations.CreateModel(
            name='JadwalPekanTidakEfektif',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('URAIAN_KEGIATAN', models.TextField()),
                ('JUMLAH_MINGGU', models.IntegerField()),
                ('KETERANGAN', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Jadwal Pekan Tidak Efektif',
            },
        ),
        migrations.CreateModel(
            name='JurnalBelajar',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PERTEMUAN', models.CharField(max_length=255)),
                ('TANGGAL_MENGAJAR', models.DateField(default=datetime.date.today)),
                ('DESKRIPSI_MATERI', models.TextField()),
                ('FILE_DOKUMENTASI', models.FileField(max_length=255, upload_to='JurnalBelajar')),
            ],
            options={
                'verbose_name_plural': 'Jurnal Belajar',
                'ordering': ['PERTEMUAN'],
            },
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255, validators=[adistetsa.custom_function.paksa_huruf_besar])),
            ],
            options={
                'verbose_name_plural': 'Jurusan',
            },
        ),
        migrations.CreateModel(
            name='KategoriTataTertib',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat])),
            ],
            options={
                'verbose_name_plural': 'Kategori Tata Tertib',
                'ordering': ['NAMA'],
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TINGKATAN', models.CharField(choices=[('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], max_length=255)),
                ('KODE_KELAS', models.CharField(blank=True, max_length=255, unique=True, verbose_name='KELAS')),
            ],
            options={
                'verbose_name_plural': 'Kelas',
                'ordering': ['TAHUN_AJARAN'],
            },
        ),
        migrations.CreateModel(
            name='KelasSiswa',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Kelas Siswa',
            },
        ),
        migrations.CreateModel(
            name='KTSP',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_FILE', models.FileField(max_length=255, upload_to='Dokumen_KTSP')),
            ],
            options={
                'verbose_name_plural': 'KTSP',
            },
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('KODE', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255, validators=[adistetsa.custom_function.cek_huruf_besar_awal_kalimat], verbose_name='MATA PELAJARAN')),
            ],
            options={
                'verbose_name_plural': 'Mata Pelajaran',
                'ordering': ['NAMA'],
            },
        ),
        migrations.CreateModel(
            name='NamaOfferingKelas',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA', models.CharField(max_length=255, validators=[adistetsa.custom_function.paksa_huruf_besar])),
            ],
            options={
                'verbose_name_plural': 'Nama Offering Kelas',
            },
        ),
        migrations.CreateModel(
            name='NilaiRaport',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KELOMPOK_MATA_PELAJARAN', models.CharField(choices=[('Kelompok A (UMUM)', 'Kelompok A (UMUM)'), ('Kelompok B (UMUM)', 'Kelompok A (UMUM)'), ('Kelompok C (PEMINATAN)', 'Kelompok C (PEMINATAN)')], max_length=255)),
                ('BEBAN', models.BigIntegerField()),
                ('NILAI_PENGETAHUAN', models.BigIntegerField()),
                ('NILAI_KETERAMPILAN', models.BigIntegerField()),
                ('DESKRIPSI_PENGETAHUAN', models.CharField(max_length=255)),
                ('DESKRIPSI_KETERAMPILAN', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Nilai Raport',
            },
        ),
        migrations.CreateModel(
            name='OfferingKelas',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Offering Kelas',
            },
        ),
        migrations.CreateModel(
            name='PoinPelanggaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(max_length=255)),
                ('POIN', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Poin Pelanggaran',
                'ordering': ['KETERANGAN'],
            },
        ),
        migrations.CreateModel(
            name='Raport',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Raport',
            },
        ),
        migrations.CreateModel(
            name='SilabusRPB',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('NAMA_FILE', models.FileField(max_length=255, upload_to='Dokumen_SilabusRPB')),
            ],
            options={
                'verbose_name_plural': 'Silabus RPB',
            },
        ),
        migrations.CreateModel(
            name='TahunAjaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TAHUN_AJARAN_AWAL', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9999)])),
                ('TAHUN_AJARAN_AKHIR', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'verbose_name_plural': 'Tahun Ajaran',
            },
        ),
        migrations.CreateModel(
            name='WaktuPelajaran',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('WAKTU_MULAI', models.TimeField()),
                ('WAKTU_BERAKHIR', models.TimeField()),
                ('JAM_KE', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Waktu Pelajaran',
                'ordering': ['JAM_KE'],
            },
        ),
        migrations.CreateModel(
            name='TataTertib',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KETERANGAN', models.CharField(max_length=255)),
                ('KATEGORI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kategoritatatertib')),
            ],
            options={
                'verbose_name_plural': 'Tata Tertib',
                'ordering': ['KETERANGAN'],
            },
        ),
        migrations.AddConstraint(
            model_name='tahunajaran',
            constraint=models.UniqueConstraint(fields=('TAHUN_AJARAN_AWAL', 'TAHUN_AJARAN_AKHIR'), name='kurikulum_tahunajaran_unique'),
        ),
        migrations.AddField(
            model_name='silabusrpb',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelas'),
        ),
        migrations.AddField(
            model_name='silabusrpb',
            name='MATA_PELAJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.matapelajaran'),
        ),
        migrations.AddField(
            model_name='silabusrpb',
            name='SEMESTER',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
        ),
        migrations.AddField(
            model_name='silabusrpb',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
        ),
        migrations.AddField(
            model_name='raport',
            name='BUKU_INDUK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tata_usaha.bukuinduk'),
        ),
        migrations.AddField(
            model_name='raport',
            name='KELAS_SISWA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa'),
        ),
        migrations.AddField(
            model_name='raport',
            name='SEMESTER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
        ),
        migrations.AddConstraint(
            model_name='poinpelanggaran',
            constraint=models.UniqueConstraint(fields=('KETERANGAN', 'POIN'), name='kurikulum_poinpelanggaran_unique'),
        ),
        migrations.AddField(
            model_name='offeringkelas',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelas'),
        ),
        migrations.AddField(
            model_name='offeringkelas',
            name='OFFERING',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.namaofferingkelas'),
        ),
        migrations.AddField(
            model_name='nilairaport',
            name='MATA_PELAJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.matapelajaran'),
        ),
        migrations.AddField(
            model_name='nilairaport',
            name='RAPORT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.raport'),
        ),
        migrations.AddConstraint(
            model_name='matapelajaran',
            constraint=models.UniqueConstraint(fields=('KODE', 'NAMA'), name='kurikulum_matapelajaran_unique'),
        ),
        migrations.AddField(
            model_name='ktsp',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
        ),
        migrations.AddField(
            model_name='kelassiswa',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.offeringkelas'),
        ),
        migrations.AddField(
            model_name='kelassiswa',
            name='NIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa'),
        ),
        migrations.AddField(
            model_name='kelas',
            name='JURUSAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.jurusan'),
        ),
        migrations.AddField(
            model_name='kelas',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
        ),
        migrations.AddConstraint(
            model_name='kategoritatatertib',
            constraint=models.UniqueConstraint(fields=('NAMA',), name='kurikulum_kategoritatatertib_unique'),
        ),
        migrations.AddField(
            model_name='jurnalbelajar',
            name='DAFTAR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.daftarjurnalbelajar'),
        ),
        migrations.AddField(
            model_name='jurnalbelajar',
            name='GURU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='jadwalpekanaktif',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelas'),
        ),
        migrations.AddField(
            model_name='jadwalpekanaktif',
            name='MATA_PELAJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.matapelajaran'),
        ),
        migrations.AddField(
            model_name='jadwalpekanaktif',
            name='MINGGU_EFEKTIF',
            field=models.ManyToManyField(to='kurikulum.JadwalPekanEfektifSemester'),
        ),
        migrations.AddField(
            model_name='jadwalpekanaktif',
            name='MINGGU_TIDAK_EFEKTIF',
            field=models.ManyToManyField(to='kurikulum.JadwalPekanTidakEfektif'),
        ),
        migrations.AddField(
            model_name='jadwalpekanaktif',
            name='SEMESTER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='GURU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.offeringkelas'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='MATA_PELAJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.matapelajaran'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='SEMESTER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='TAHUN_AJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='WAKTU_PELAJARAN',
            field=models.ManyToManyField(to='kurikulum.WaktuPelajaran'),
        ),
        migrations.AddConstraint(
            model_name='datasemester',
            constraint=models.UniqueConstraint(fields=('KE',), name='kurikulum_datasemester_unique'),
        ),
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='GURU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
        ),
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='JADWAL_MENGAJAR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.jadwalmengajar'),
        ),
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.offeringkelas'),
        ),
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='MATA_PELAJARAN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.matapelajaran'),
        ),
        migrations.AddField(
            model_name='daftarjurnalbelajar',
            name='SEMESTER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='TAHUN_AJARAN_AKTIF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.tahunajaran'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='changed_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.user', verbose_name='Changed by'),
        ),
        migrations.AddField(
            model_name='absensisiswa',
            name='JURNAL_BELAJAR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.jurnalbelajar'),
        ),
        migrations.AddField(
            model_name='absensisiswa',
            name='NIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa'),
        ),
        migrations.AddConstraint(
            model_name='tatatertib',
            constraint=models.UniqueConstraint(fields=('KETERANGAN',), name='kurikulum_tatatertib_unique'),
        ),
        migrations.AddConstraint(
            model_name='silabusrpb',
            constraint=models.UniqueConstraint(fields=('MATA_PELAJARAN', 'TAHUN_AJARAN', 'KELAS', 'SEMESTER'), name='kurikulum_silabusrpb_unique'),
        ),
        migrations.AddConstraint(
            model_name='raport',
            constraint=models.UniqueConstraint(fields=('KELAS_SISWA', 'SEMESTER'), name='kurikulum_raport_unique'),
        ),
        migrations.AddConstraint(
            model_name='offeringkelas',
            constraint=models.UniqueConstraint(fields=('KELAS', 'OFFERING'), name='kurikulum_offeringkelas_unique'),
        ),
        migrations.AddConstraint(
            model_name='nilairaport',
            constraint=models.UniqueConstraint(fields=('MATA_PELAJARAN',), name='kurikulum_nilairaport_unique'),
        ),
        migrations.AddConstraint(
            model_name='ktsp',
            constraint=models.UniqueConstraint(fields=('TAHUN_AJARAN',), name='kurikulum_ktsp_unique'),
        ),
        migrations.AddConstraint(
            model_name='kelassiswa',
            constraint=models.UniqueConstraint(fields=('NIS', 'KELAS'), name='kurikulum_kelassiswa_unique'),
        ),
        migrations.AddConstraint(
            model_name='kelas',
            constraint=models.UniqueConstraint(fields=('TAHUN_AJARAN', 'TINGKATAN', 'JURUSAN'), name='kurikulum_kelas_unique'),
        ),
        migrations.AddConstraint(
            model_name='jurnalbelajar',
            constraint=models.UniqueConstraint(fields=('PERTEMUAN', 'DAFTAR'), name='kurikulum_jurnalbelajar_unique'),
        ),
        migrations.AddConstraint(
            model_name='jadwalmengajar',
            constraint=models.UniqueConstraint(fields=('KELAS', 'MATA_PELAJARAN', 'HARI'), name='kurikulum_jadwalmengajar_unique'),
        ),
        migrations.AddConstraint(
            model_name='daftarjurnalbelajar',
            constraint=models.UniqueConstraint(fields=('JADWAL_MENGAJAR',), name='kurikulum_daftarjurnalbelajar_unique'),
        ),
    ]
