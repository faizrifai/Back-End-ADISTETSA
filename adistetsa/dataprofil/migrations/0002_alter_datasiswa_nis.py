# Generated by Django 4.0 on 2022-03-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='NIS',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]