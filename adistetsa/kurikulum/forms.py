from xml.dom import ValidationErr
from django import forms

from .models import JadwalMengajar
from django.forms import ValidationError

class JadwalMengajarForm(forms.ModelForm):
    def clean(self):
        waktu_pelajaran = self.cleaned_data.get('WAKTU_PELAJARAN')
        jadwal = JadwalMengajar.objects.filter(GURU=self.cleaned_data.get('GURU'), HARI=self.cleaned_data.get('HARI'))
        
        print(waktu_pelajaran)
        
        for waktu in waktu_pelajaran.all():
            for data in jadwal:
                for waktu_lama in data.WAKTU_PELAJARAN.all():
                    if waktu == waktu_lama:
                        raise ValidationError({'WAKTU_PELAJARAN': 'Jadwal mengajar bentrok'})
        
        # for data in jadwal:
        #     waktu_pelajaran = data.WAKTU_PELAJARAN.all()
        #     for data in waktu_pelajaran:
        #         for waktu in waktu_pelajaran.all():
        #             if data == waktu:
        #                 raise ValidationError({'WAKTU_PELAJARAN': 'Luwe'})