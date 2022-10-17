from admin_auto_filters.filters import AutocompleteFilter


class StatusFilter(AutocompleteFilter):
    title = "STATUS"
    field_name = "STATUS"


class AlatFilter(AutocompleteFilter):
    title = "ALAT"
    field_name = "ALAT"


class RuanganFilter(AutocompleteFilter):
    title = "RUANGAN"
    field_name = "RUANGAN"
