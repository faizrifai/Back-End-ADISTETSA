# Generated by Django 4.0 on 2022-01-09 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0048_alter_jadwalmengajar_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jadwalmengajar',
            options={'ordering': ['KELAS', 'HARI', 'JUMLAH_WAKTU'], 'verbose_name_plural': 'Jadwal Mengajar'},
        ),
        migrations.RemoveField(
            model_name='jadwalmengajar',
            name='TAHUN_AJARAN',
        ),
    ]
