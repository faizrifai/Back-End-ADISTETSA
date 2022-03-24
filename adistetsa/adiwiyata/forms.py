from email.policy import default
from django import forms
from adistetsa.adiwiyata.enums import ENUM_3R

from dataprofil.models import DataSiswa

from .models import SanitasiDrainase

# class SanitasiForm(forms.ModelForm):
#     UNSUR_TERLIBAT = forms.MultipleChoiceField(
#         widget= forms.CheckboxSelectMultiple,
#         choices=ENUM_3R,
#         label='UNSUR TERLIBAT',
#     )
    
#     class Meta:
#         model = SanitasiDrainase
#         exclude = ('UNSUR_TERLIBAT',)
        
#     def save(self, commit=True):
#         data_siswa = self.cleaned_data['DATA_SISWA']
#         siswa = DataSiswa.objects.get(NIS=data_siswa.NIS.NIS)
#         kelas = OfferingKelas.objects.get(ID=data_siswa.KELAS.ID)
#         instance = super(MutasiMasukForm, self).save(commit=False)
#         instance.NO_INDUK_BARU = siswa.NIS
#         instance.NAMA_SISWA = siswa.NAMA
#         instance.ALAMAT = siswa.ALAMAT
#         instance.KELAS = kelas.KELAS.TINGKATAN + ' ' + str(kelas.KELAS.JURUSAN) + ' ' + kelas.OFFERING.NAMA
        
#         if commit:
#             instance.save()
            
#         return instance
    
# class MutasiKeluarForm(forms.ModelForm):
#     DATA_SISWA = forms.ModelChoiceField(queryset=KelasSiswa.objects.all(), label='DATA SISWA')
    
#     class Meta:
#         model = MutasiKeluar
#         exclude = ('NAMA_SISWA','KELAS','NO_INDUK',)
        
#     def save(self, commit=True):
#         data_siswa = self.cleaned_data['DATA_SISWA']
#         siswa = DataSiswa.objects.get(NIS=data_siswa.NIS.NIS)
#         kelas = OfferingKelas.objects.get(ID=data_siswa.KELAS.ID)
#         instance = super(MutasiKeluarForm, self).save(commit=False)
#         instance.NO_INDUK = siswa.NIS
#         instance.NAMA_SISWA = siswa.NAMA
#         instance.KELAS = kelas.KELAS.TINGKATAN + ' ' + str(kelas.KELAS.JURUSAN) + ' ' + kelas.OFFERING.NAMA
        
#         if commit:
#             instance.save()
            
#         return instance

# class BukuIndukForms (forms.ModelForm):
#     data_siswa = DataSiswa.objects.get(NIS=instance.NIS.NIS)
#     NAMA = forms.cleaned_data[]
    