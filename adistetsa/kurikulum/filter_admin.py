from admin_auto_filters.filters import AutocompleteFilter

class TahunFilter(AutocompleteFilter):
    title = 'TAHUN AJARAN'
    field_name = 'TAHUN_AJARAN'

class KelasFilter(AutocompleteFilter):
    title = 'KELAS'
    field_name = 'KELAS'

class MataPelajaranFilter(AutocompleteFilter):
    title = 'MATA PELAJARAN'
    field_name = 'MATA_PELAJARAN'

class SemesterFilter(AutocompleteFilter):
    title = 'SEMESTER'
    field_name = 'SEMESTER'

class PelajaranFilter(AutocompleteFilter):
    title = 'PELAJARAN'
    field_name = 'PELAJARAN'
    
class NamaOfferingKelasFilter(AutocompleteFilter):
    title = 'OFFERING'
    field_name = 'OFFERING'

class WaktuPelajaranFIlter(AutocompleteFilter):
    title = 'WAKTU PELAJARAN'
    field_name = 'WAKTU_PELAJARAN'

class GuruFilter(AutocompleteFilter):
    title = 'GURU'
    field_name = 'GURU'

class KategoriTataTertibFilter(AutocompleteFilter):
    title = 'KATEGORI'
    field_name = 'KATEGORI'