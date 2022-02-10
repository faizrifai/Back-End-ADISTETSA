from turtle import title
from admin_auto_filters.filters import AutocompleteFilter

class StatusFilter(AutocompleteFilter):
    title = 'STATUS'
    field_name = 'STATUS'