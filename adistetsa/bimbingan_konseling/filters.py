import django_filters
from kurikulum.models import Jurusan, KelasSiswa
from bimbingan_konseling.models import PeminatanLintasMinat

class AngketFilter(django_filters.FilterSet):
    KELAS = django_filters.ModelChoiceFilter(
        field_name="KELAS_SISWA",
        queryset=KelasSiswa.objects.all()
    )
    JURUSAN = django_filters.ModelChoiceFilter(
        field_name="KELAS_SISWA__KELAS__KELAS__JURUSAN",
        queryset=Jurusan.objects.all()
    )

    class Meta:
        model = PeminatanLintasMinat
        fields = ('KELAS', 'JURUSAN')