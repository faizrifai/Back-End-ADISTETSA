import django_filters

from .models import DaftarJurnalEkskul, JadwalEkskul
from kurikulum.models import TahunAjaran


class DaftarJurnalEkskulFilter(django_filters.FilterSet):
    TAHUN_AJARAN = django_filters.ModelChoiceFilter(
        field_name="JADWAL_EKSKUL__TAHUN_AJARAN", queryset=TahunAjaran.objects.all()
    )
    HARI = django_filters.ChoiceFilter(
        choices=JadwalEkskul._meta.get_field("HARI").choices,
        field_name="JADWAL_EKSKUL__HARI",
    )

    class Meta:
        model = DaftarJurnalEkskul
        fields = ("TAHUN_AJARAN", "HARI")
