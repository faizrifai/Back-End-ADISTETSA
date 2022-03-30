from django.contrib import admin
from django.db.models import Sum

from .forms import ReuseReduceRecycleForm, SanitasiDrainaseForm

from.models import *
from kurikulum.enums import ENUM_BULAN

# Register your models here.
class SanitasiDraineseAdmin (admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'UNSUR_TERLIBAT', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'UNSUR_TERLIBAT', 'KETERANGAN', 'FILE')
    list_per_page = 10
    form = SanitasiDrainaseForm
    
admin.site.register(SanitasiDrainase, SanitasiDraineseAdmin)

class JaringanKerjaAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10
    
admin.site.register(JaringanKerja, JaringanKerjaAdmin)

class PublikasiAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'JENIS_MEDIA', 'KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'JENIS_MEDIA', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(Publikasi, PublikasiAdmin)

class DaftarKaderAdmin(admin.ModelAdmin):
    search_fields = ('NIS__NIS','NIS__NAMA', 'NIS__HP', 'NIS__ALAMAT')
    list_display = ('nis','nama','handphone','alamat')
    autocomplete_fields=('NIS',)
    def nis (self, obj):
        return obj.NIS.NIS
    
    def nama (self, obj):
        return obj.NIS.NAMA
    
    def handphone(self, obj):
        return obj.NIS.HP
    
    def alamat(self,obj):
        return obj.NIS.ALAMAT
    
    list_per_page = 10

admin.site.register(DaftarKader, DaftarKaderAdmin)

class KegiatanKaderAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(KegiatanKader, KegiatanKaderAdmin)

class KonservasiAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'KATEGORI','NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'KATEGORI','NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10
    list_filter = ('KATEGORI',)

admin.site.register(Konservasi, KonservasiAdmin)

class PenanamanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PenanamanPohon, PenanamanPohonAdmin)

class PembibitanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PembibitanPohon, PembibitanPohonAdmin)

class PemeliharaanPohonAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PemeliharaanPohon, PemeliharaanPohonAdmin)

class KaryaInovatifAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_INOVATOR', 'NAMA_KARYA_INOVATIF','JENIS', 'FILE','KETERANGAN')
    list_display = ('TANGGAL', 'NAMA_INOVATOR', 'NAMA_KARYA_INOVATIF','JENIS', 'FILE','KETERANGAN')
    list_per_page = 10

admin.site.register(KaryaInovatif, KaryaInovatifAdmin) 

class PenerapanPRLHAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'PESERTA','KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'PESERTA','KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PenerapanPRLH, PenerapanPRLHAdmin)

class ReuseReduceRecycleAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN','JENIS_KEGIATAN','PIHAK_TERLIBAT', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN','JENIS_KEGIATAN','PIHAK_TERLIBAT', 'KETERANGAN', 'FILE')
    list_per_page = 10
    form = ReuseReduceRecycleForm

admin.site.register(ReuseReduceRecycle, ReuseReduceRecycleAdmin)

class PemeliharaanSampahAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_display = ('TANGGAL', 'NAMA_KEGIATAN', 'KETERANGAN', 'FILE')
    list_per_page = 10

admin.site.register(PemeliharaanSampah, PemeliharaanSampahAdmin)

class TabunganSampahAdmin(admin.ModelAdmin):
    search_fields = ('TANGGAL', 'KATEGORI','JUMLAH')
    list_display = ('TANGGAL', 'KATEGORI','JUMLAH')
    list_per_page = 10

admin.site.register(TabunganSampah, TabunganSampahAdmin)

class TabunganSampahProxyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/adiwiyata/tabungansampahproxy_change_list.html'
    date_hierarchy = 'TANGGAL'
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        tanggal = None
        
        if response.context_data['preserved_filters']:
            qp = response.context_data['preserved_filters'].split('=')[1]
            dan = '%26'
            equal = '%3D'
            splitted = qp.split(dan)
            for i in range(len(splitted)):
                splitted[i] = splitted[i].split(equal)[-1]
            
            if len(splitted) >= 2:
                bulan = int(splitted[-2]) - 1
                bulan = ENUM_BULAN[bulan][0]
                splitted[-2] = str(bulan)
                
            tanggal = " ".join(splitted)
        else:
            tanggal = 'Total Keseluruhan'
        
        print (qs)
        
        basah = 0
        kering = 0
        total = 0
        for data in qs:
            if data.KATEGORI == 'Basah':
                basah += data.JUMLAH
            if data.KATEGORI == 'Kering':
                kering += data.JUMLAH
        response.context_data['total'] = basah + kering
        response.context_data['tanggal'] = tanggal
        response.context_data['basah']=basah
        response.context_data['kering']=kering

        return response
    
admin.site.register(TabunganSampahProxy, TabunganSampahProxyAdmin)
