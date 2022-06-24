import django_filters

from .models import DaftarJurnalBelajar, JadwalMengajar, TahunAjaran

class TahunAjaranChoiceFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value:
            pk = []
            for data in qs:
                tahun_ajaran = TahunAjaran.objects.get(pk=value)
                jadwal_mengajar = JadwalMengajar.objects.filter(
                    GURU=data.GURU,
                    MATA_PELAJARAN=data.MATA_PELAJARAN,
                    KELAS=data.KELAS,
                    SEMESTER=data.SEMESTER,
                    TAHUN_AJARAN=tahun_ajaran
                )
                if jadwal_mengajar:
                    pk.append(data.ID)
    
            return qs.filter(pk__in=pk)
        
        return qs

class HariChoiceFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value:
            pk = []
            for data in qs:
                jadwal_mengajar = JadwalMengajar.objects.filter(
                    GURU=data.GURU,
                    MATA_PELAJARAN=data.MATA_PELAJARAN,
                    KELAS=data.KELAS,
                    SEMESTER=data.SEMESTER,
                    HARI=value
                )
                if jadwal_mengajar:
                    pk.append(data.ID)
    
            return qs.filter(pk__in=pk)
        
        return qs

class DaftarJurnalBelajarFilter(django_filters.FilterSet):
    TAHUN_AJARAN = TahunAjaranChoiceFilter()
    HARI = HariChoiceFilter()

    class Meta:
        model = DaftarJurnalBelajar
        fields = ('TAHUN_AJARAN', 'HARI')


class JadwalMengajarGuruFilter(django_filters.FilterSet):
    TAHUN_AJARAN = django_filters.ModelChoiceFilter(
        field_name="TAHUN_AJARAN",
        queryset=TahunAjaran.objects.all())
    HARI = django_filters.ChoiceFilter(
        choices=JadwalMengajar._meta.get_field('HARI').choices,
        field_name='HARI')

    class Meta:
        model = JadwalMengajar
        fields = ('TAHUN_AJARAN', 'HARI')