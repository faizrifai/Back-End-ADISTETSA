# Generated by Django 4.0 on 2022-01-17 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('perpustakaan', '0008_remove_operator_object_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operator',
            name='KODE_OPERATOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
