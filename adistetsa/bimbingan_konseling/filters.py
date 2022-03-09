import django_filters

from bimbingan_konseling.models import PeminatanLintasMinat
class JurusanFilter(django_filters.FilterSet):
    class Meta:
        model = PeminatanLintasMinat
        #use __ (double underscore) to target foreign key values
        fields = ['KELAS_SISWA__KELAS__KELAS__JURUSAN']   