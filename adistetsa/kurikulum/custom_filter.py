import django_filters

from .models import DaftarJurnalBelajar, JadwalMengajar, TahunAjaran


class DaftarJurnalBelajarFilter(django_filters.FilterSet):
    TAHUN_AJARAN = django_filters.ModelChoiceFilter(
        field_name="JADWAL_MENGAJAR__TAHUN_AJARAN",
        queryset=TahunAjaran.objects.all())
    HARI = django_filters.ChoiceFilter(
        choices=JadwalMengajar._meta.get_field('HARI').choices,
        field_name='JADWAL_MENGAJAR__HARI')

    class Meta:
        model = DaftarJurnalBelajar
        fields = ('TAHUN_AJARAN', 'HARI')