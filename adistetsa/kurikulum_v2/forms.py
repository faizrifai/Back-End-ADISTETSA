from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import KalenderPendidikan


class KalenderPendidikanForm(ModelForm):
    class Meta:
        model = KalenderPendidikan
        fields = "__all__"
        widgets = {
            "WARNA": TextInput(attrs={"type": "color"}),
        }
