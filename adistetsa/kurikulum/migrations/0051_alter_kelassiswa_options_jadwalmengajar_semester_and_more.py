# Generated by Django 4.0 on 2022-01-10 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0050_alter_jadwalmengajar_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kelassiswa',
            options={'verbose_name_plural': 'Kelas Siswa'},
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='SEMESTER',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mengajar',
            name='SEMESTER',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kelassiswa',
            name='KELAS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurikulum.offeringkelas'),
        ),
        migrations.AddConstraint(
            model_name='kelassiswa',
            constraint=models.UniqueConstraint(fields=('NIS', 'KELAS'), name='kurikulum_kelassiswa_unique'),
        ),
    ]
