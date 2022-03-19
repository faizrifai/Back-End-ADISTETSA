
            name='PeminatanLintasMinat',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('KATEGORI', models.CharField(choices=[('Angket Peminatan', 'Angket Peminatan'), ('Angket Lintas Minat', 'Angket Lintas Minat'), ('Angket Data Diri', 'Angket Data Diri')], max_length=255)),
                ('FILE', models.FileField(max_length=255, upload_to='Dokumen_Peminatan_Lintas_Minat')),
                ('KELAS_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.kelassiswa')),
            ],
            options={
                'verbose_name_plural': 'Peminatan dan Lintas Minat',
            },
        ),
        migrations.CreateModel(
            name='Konsultasi',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TANGGAL_KONSULTASI', models.DateField(default=datetime.date.today, max_length=255)),
                ('JAM', models.TimeField(max_length=255)),
                ('JENIS_MASALAH', models.CharField(choices=[('Karier', 'Karier'), ('Pribadi', 'Pribadi'), ('Sosial', 'Sosial'), ('Belajar', 'Belajar')], max_length=255)),
                ('RATING', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('STATUS', models.CharField(choices=[('Dijadwalkan', 'Dijadwalkan'), ('Selesai', 'Selesai'), ('Diajukan', 'Diajukan'), ('Telah Mengisi Feedback', 'Telah Mengisi Feedback'), ('Ditolak', 'Ditolak')], default='Diajukan', max_length=255)),
                ('KONSELOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bimbingan_konseling.katalogkonselor')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Konsultasi',
            },
        ),
    ]