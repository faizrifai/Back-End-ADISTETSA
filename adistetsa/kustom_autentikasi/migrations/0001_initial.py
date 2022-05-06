# Generated by Django 4.0 on 2022-05-06 04:03

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
            name='DataSiswaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_SISWA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Data Siswa User',
            },
        ),
        migrations.CreateModel(
            name='DataPelatihUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_PELATIH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datapelatih')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Data Pelatih User',
            },
        ),
        migrations.CreateModel(
            name='DataOrangTuaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_ORANG_TUA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataorangtua')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Data Orang Tua User',
            },
        ),
        migrations.CreateModel(
            name='DataKaryawanUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_KARYAWAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datakaryawan')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Data Karyawan User',
            },
        ),
        migrations.CreateModel(
            name='DataGuruUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATA_GURU', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Data Guru User',
            },
        ),
    ]
