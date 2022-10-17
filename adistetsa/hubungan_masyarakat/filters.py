import django_filters
from .models import BukuTamu


class BukuTamuFilter(django_filters.FilterSet):
    def filter_tanggal(self, qs, name, value):
        if value == "1":  # Terbaru
            return qs.order_by("-TANGGAL")
        elif value == "2":  # Terlama
            return qs.order_by("TANGGAL")

    def filter_nama(self, qs, name, value):
        if value == "1":  # Terbaru
            return qs.order_by("-NAMA")
        elif value == "2":  # Terlama
            return qs.order_by("NAMA")

    TANGGAL = django_filters.CharFilter(method="filter_tanggal")
    NAMA = django_filters.CharFilter(method="filter_nama")

    class Meta:
        model = BukuTamu
        fields = ("TANGGAL", "NAMA")
