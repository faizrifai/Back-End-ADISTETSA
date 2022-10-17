from django import forms

from dataprofil.models import DataSiswa

from .models import *
from kurikulum.models import KelasSiswa, OfferingKelas


class LogUKSSiswaForm(forms.ModelForm):
    DATA_SISWA = forms.ModelChoiceField(
        queryset=KelasSiswa.objects.all(), label="DATA SISWA"
    )

    class Meta:
        model = LogUKSSiswa
        exclude = (
            "NAMA",
            "KELAS",
            "NISN",
        )

    def save(self, commit=True):
        data_siswa = self.cleaned_data["DATA_SISWA"]
        siswa = DataSiswa.objects.get(NIS=data_siswa.NIS.NIS)
        kelas = OfferingKelas.objects.get(ID=data_siswa.KELAS.ID)
        instance = super(LogUKSSiswaForm, self).save(commit=False)
        instance.NISN = siswa.NISN
        instance.NAMA = siswa.NAMA
        instance.KELAS = (
            kelas.KELAS.TINGKATAN
            + " "
            + str(kelas.KELAS.JURUSAN)
            + " "
            + kelas.OFFERING.NAMA
        )
        if commit:
            instance.save()

        return instance
