from admin_auto_filters.filters import AutocompleteFilter

class BahasaFilter(AutocompleteFilter):
    title = 'BAHASA'
    field_name = 'BAHASA'
    
class AuthorFilter(AutocompleteFilter):
    title = 'AUTHOR'
    field_name = 'KODE_AUTHOR'
    
class MediaFilter(AutocompleteFilter):
    title = 'JENIS MEDIA'
    field_name = 'KODE_MEDIA'
    
class TipeBukuFilter(AutocompleteFilter):
    title = 'TIPE BUKU'
    field_name = 'KODE_TIPE'

class TahunTerbitFilter(AutocompleteFilter):
    title = 'TAHUN TERBIT'
    field_name = 'TAHUN_TERBIT'
