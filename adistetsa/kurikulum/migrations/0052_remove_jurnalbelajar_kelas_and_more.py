# Generated by Django 4.0 on 2022-01-10 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0001_initial'),
        ('kurikulum', '0051_alter_kelassiswa_options_jadwalmengajar_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurnalbelajar',
            name='KELAS',
        ),
        migrations.RemoveField(
            model_name='jurnalbelajar',
            name='PELAJARAN',
        ),
        migrations.RemoveField(
            model_name='jurnalbelajar',
            name='SEMESTER',
        ),
        migrations.AddField(
            model_name='jurnalbelajar',
            name='GURU',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dataprofil.dataguru'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jurnalbelajar',
            name='JADWAL_MENGAJAR',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.jadwalmengajar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jurnalbelajar',
            name='PERTEMUAN',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
