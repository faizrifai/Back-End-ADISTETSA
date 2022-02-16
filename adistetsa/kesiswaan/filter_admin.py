from admin_auto_filters.filters import AutocompleteFilter

class DataSiswaFilter(AutocompleteFilter):
    title = 'DATA SISWA'
    field_name = 'DATA_SISWA'

class TahunAjaranFilter(AutocompleteFilter):
    title = 'TAHUN AJARAN'
    field_name = 'TAHUN_AJARAN'