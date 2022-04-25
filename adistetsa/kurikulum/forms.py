from xml.dom import ValidationErr
from django import forms
from tata_usaha.models import BukuInduk
from .models import JadwalMengajar, KelasSiswa, NilaiRaport
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
        
# class NilaiRaportForm(forms.ModelForm):
    
#     class Meta:
#         model = NilaiRaport
#         fields = "__all__"
        
#     def __init__(self, *args, **kwargs):
#         super(NilaiRaportForm, self).__init__(*args, **kwargs)
#         siswa = BukuInduk.objects.get(ID=self.BUKU_INDUK.ID)
#         self.fields['KELAS_SISWA'].queryset = KelasSiswa.objects.filter(NIS=siswa.NIS)
