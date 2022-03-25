# Generated by Django 4.0 on 2022-03-24 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adiwiyata', '0002_alter_jaringankerja_file_alter_karyainovatif_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabunganSampahProxy',
            fields=[
            ],
            options={
                'ordering': ['TANGGAL'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('adiwiyata.tabungansampah',),
        ),
        migrations.RenameField(
            model_name='tabungansampah',
            old_name='JUMLAH_PERTANGGAL',
            new_name='JUMLAH',
        ),
    ]
