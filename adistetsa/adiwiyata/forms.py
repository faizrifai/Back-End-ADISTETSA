from email.policy import default
from django import forms
from .enums import ENUM_UNSUR_TERLIBAT

from .models import SanitasiDrainase, ReuseReduceRecycle


class SanitasiDrainaseForm(forms.ModelForm):
    UNSUR_TERLIBAT = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ENUM_UNSUR_TERLIBAT,
        label="UNSUR TERLIBAT",
    )

    class Meta:
        model = SanitasiDrainase
        exclude = ("UNSUR_TERLIBAT",)

    def save(self, commit=True):

        instance = super(SanitasiDrainaseForm, self).save(commit=False)
        instance.UNSUR_TERLIBAT = ", ".join(self.cleaned_data["UNSUR_TERLIBAT"])

        if commit:
            instance.save()

        return instance


class ReuseReduceRecycleForm(forms.ModelForm):
    PIHAK_TERLIBAT = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ENUM_UNSUR_TERLIBAT,
        label="PIHAK TERLIBAT",
    )

    class Meta:
        model = ReuseReduceRecycle
        exclude = ("PIHAK_TERLIBAT",)

    def save(self, commit=True):

        instance = super(ReuseReduceRecycleForm, self).save(commit=False)
        instance.PIHAK_TERLIBAT = ", ".join(self.cleaned_data["PIHAK_TERLIBAT"])

        if commit:
            instance.save()

        return instance
