from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kustom_autentikasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasiswauser',
            options={'verbose_name_plural': 'Data Siswa User'},
        ),
    ]
