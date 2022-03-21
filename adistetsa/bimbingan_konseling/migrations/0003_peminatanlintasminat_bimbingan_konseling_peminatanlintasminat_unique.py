from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bimbingan_konseling', '0002_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='peminatanlintasminat',
            constraint=models.UniqueConstraint(fields=('KATEGORI',), name='bimbingan_konseling_peminatanlintasminat_unique'),
        ),
    ]
