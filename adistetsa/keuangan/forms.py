from django import forms
from pyparsing import replaceWith
from .enums import ENUM_JENIS_PEMBAYARAN
from kurikulum.enums import ENUM_BULAN

from .models import Pembayaran

class PembayaranForm(forms.ModelForm):
    # JENIS_PEMBAYARAN = forms.MultipleChoiceField(
    #     widget= forms.CheckboxSelectMultiple,
    #     choices=ENUM_JENIS_PEMBAYARAN,
    #     label='JENIS PEMBAYARAN', 
    # )
    
    BULAN_PEMBAYARAN_DPSM_RUTIN = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ENUM_BULAN, 
        label = 'BULAN PEMBAYARAN DPSM RUTIN', 
        required=False,
    )
    
    BULAN_PEMBAYARAN_BIMBEL =  forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices= ENUM_BULAN, 
        label = 'BULAN PEMBAYARAN BIMBEL', 
        required=False,
    )
    
    class Meta:
        model = Pembayaran
        exclude = ('BULAN_PEMBAYARAN_DPSM_RUTIN', 'BULAN_PEMBAYARAN_BIMBEL')
    
    def save(self, commit=True):
        instance = super(PembayaranForm, self).save(commit=False)
        instance.BULAN_PEMBAYARAN_DPSM_RUTIN = ", ".join(self.cleaned_data['BULAN_PEMBAYARAN_DPSM_RUTIN'])
        instance.BULAN_PEMBAYARAN_BIMBEL = ", ".join(self.cleaned_data['BULAN_PEMBAYARAN_BIMBEL'])
        # instance.JENIS_PEMBAYARAN = ", ".join(self.cleaned_data['JENIS_PEMBAYARAN'])
        
        if commit: 
            instance.save()
        
        return instance

# class JenisPembayaran(forms.ModelForm):
#     JENIS_PEMBAYARAN = forms.MultipleChoiceField(
#         widget= forms.MultipleChoiceField,
#         choices=ENUM_JENIS_PEMBAYARAN,
#         label='JENIS PEMBAYARAN', 
#     )
    
#     class Meta: 
#         model = Pembayaran
#         exclude = ('JENIS_PEMBAYARAN',)
        
#     def save(self, commit = True):
#         instance = super(PembayaranForm, self).save(commit=False)
#         instance.JENIS_PEMBAYARAN = ", ".join(self.cleaned_data['JENIS_PEMBAYARAN'])
        
#         if commit: 
#             instance.save()
        
#         return instance