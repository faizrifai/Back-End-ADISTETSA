# Generated by Django 4.0 on 2022-02-19 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0001_initial'),
        ('kesiswaan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NilaiEkskul',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PREDIKAT', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=255)),
                ('DESKRIPSI', models.TextField(max_length=1020)),
                ('DATA_ANGGOTA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kesiswaan.anggotaekskul')),
                ('SEMESTER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester')),
            ],
        ),
    ]
