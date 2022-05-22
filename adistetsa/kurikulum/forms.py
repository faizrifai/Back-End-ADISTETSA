from django import forms
from django.apps import apps
from django.forms import ValidationError


class JadwalMengajarForm(forms.ModelForm):
    def clean(self):
        instance_id = self.instance.pk
        hari = self.cleaned_data.get('HARI')
        tahun_ajaran = self.cleaned_data.get('TAHUN_AJARAN')
        semester = self.cleaned_data.get('SEMESTER')
        kelas = self.cleaned_data.get('KELAS')
        waktu_pelajaran = self.cleaned_data.get('WAKTU_PELAJARAN')
        jadwal_mengajar_model = apps.get_model('kurikulum', 'JadwalMengajar')
        jadwal = jadwal_mengajar_model.objects.filter(
            HARI=hari, TAHUN_AJARAN=tahun_ajaran, SEMESTER=semester, KELAS=kelas)

        for waktu in waktu_pelajaran.all():
            for data in jadwal:
                for waktu_lama in data.WAKTU_PELAJARAN.all():
                    if waktu == waktu_lama:
                        if instance_id:
                            if data.pk == int(instance_id):
                                continue
                        
                        raise ValidationError(
                            {'WAKTU_PELAJARAN': 'Jadwal mengajar bentrok'})
