from django.urls import reverse
from django.db import models
from django.forms import ValidationError


# Create your models here.
class KalenderPendidikan(models.Model):
    TANGGAL_MULAI = models.DateField()
    TANGGAL_BERAKHIR = models.DateField()
    KEGIATAN = models.CharField(max_length=255)
    WARNA = models.CharField(max_length=255)

    class Meta:
        app_label = "kurikulum"
        verbose_name = "Kalender Pendidikan"
        verbose_name_plural = "Kalender Pendidikan"

    def clean(self):
        kalender_obj = KalenderPendidikan.objects.filter(
            TANGGAL_MULAI=self.TANGGAL_MULAI
        ).exclude(pk=self.pk)

        for data in kalender_obj:
            raise ValidationError("Sudah ada event pada tanggal yang dimasukkan")

    def get_url(self, day):
        url = reverse(
            "admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name),
            args=[self.id],
        )
        return '<a href="%s" style="position: relative; display: block;">%s</a>' % (
            url,
            str(day),
        )
