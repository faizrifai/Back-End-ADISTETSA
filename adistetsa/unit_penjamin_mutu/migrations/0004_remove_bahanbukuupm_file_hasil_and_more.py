# Generated by Django 4.0 on 2022-04-21 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit_penjamin_mutu', '0003_alter_pembagiantugasgurutik_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bahanbukuupm',
            name='FILE_HASIL',
        ),
        migrations.RemoveField(
            model_name='bahanbukuupm',
            name='TEMPLATE',
        ),
    ]