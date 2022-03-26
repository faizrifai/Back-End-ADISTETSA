from django import forms
from .enums import ENUM_JENIS_PEMBAYARAN
from kurikulum.enums import ENUM_BULAN

from .models import Pembayaran

class PembayaranForm(forms.ModelForm):
    PEMBAYARAN_BULAN = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ENUM_BULAN, 
        label = 'PEMBAYARAN BULAN'
    )
    
    class Meta:
        model = Pembayaran
        exclude = ('PEMBAYARAN_BULAN',)
    
    def save(self, commit=True):
        instance = super(PembayaranForm, self).save(commit=False)
        instance.PEMBAYARAN_BULAN = ", ".join(self.cleaned_data['PEMBAYARAN_BULAN'])
        
        if commit: 
            instance.save()
        
        return instance