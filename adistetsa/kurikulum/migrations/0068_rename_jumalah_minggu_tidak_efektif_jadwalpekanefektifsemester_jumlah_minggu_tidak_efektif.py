# Generated by Django 4.0 on 2022-01-13 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0067_jadwalpekanefektifsemester_bulan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jadwalpekanefektifsemester',
            old_name='JUMALAH_MINGGU_TIDAK_EFEKTIF',
            new_name='JUMLAH_MINGGU_TIDAK_EFEKTIF',
        ),
    ]