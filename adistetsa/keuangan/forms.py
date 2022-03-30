from django import forms
from .enums import ENUM_JENIS_PEMBAYARAN
from kurikulum.enums import ENUM_BULAN

from .models import Pembayaran

class PembayaranForm(forms.ModelForm):
    # JENIS_PEMBAYARAN = forms.MultipleChoiceField(
    #     widget= forms.CheckboxSelectMultiple,
    #     choices=ENUM_JENIS_PEMBAYARAN,
    #     label='JENIS PEMBAYARAN', 
    # )
    
    PEMBAYARAN_SPP = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ENUM_BULAN, 
        label = 'PEMBAYARAN SPP', 
        required=False,
    )
    
    class Meta:
        model = Pembayaran
        exclude = ('PEMBAYARAN_SPP',)
    
    def save(self, commit=True):
        instance = super(PembayaranForm, self).save(commit=False)
        instance.PEMBAYARAN_SPP = ", ".join(self.cleaned_data['PEMBAYARAN_SPP'])
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