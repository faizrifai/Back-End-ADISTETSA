from django import forms

from .models import KatalogKonselor

class KatalogKonselorForm(forms.ModelForm):
    no_whatsapp = forms.CharField(max_length=255)
    
    class Meta:
        model = KatalogKonselor
        exclude = ('WHATSAPP',)
        
    def save(self, commit=True):
        no_wa = self.cleaned_data['no_whatsapp']
        instance = super(KatalogKonselorForm, self).save(commit=False)
        instance.WHATSAPP = 'https://wa.me/+62' + no_wa
        
        if commit:
            instance.save()
            
        return instance