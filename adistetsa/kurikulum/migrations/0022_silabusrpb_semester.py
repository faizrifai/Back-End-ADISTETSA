# Generated by Django 4.0 on 2022-01-08 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurikulum', '0021_remove_silabusrpb_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='silabusrpb',
            name='SEMESTER',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='kurikulum.datasemester'),
            preserve_default=False,
        ),
    ]
