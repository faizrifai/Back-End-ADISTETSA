# Generated by Django 4.0 on 2022-03-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bimbingan_konseling', '0003_peminatanlintasminat_bimbingan_konseling_peminatanlintasminat_unique'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='peminatanlintasminat',
            name='bimbingan_konseling_peminatanlintasminat_unique',
        ),
        migrations.AddConstraint(
            model_name='peminatanlintasminat',
            constraint=models.UniqueConstraint(fields=('KELAS_SISWA', 'KATEGORI'), name='bimbingan_konseling_peminatanlintasminat_unique'),
        ),
    ]
