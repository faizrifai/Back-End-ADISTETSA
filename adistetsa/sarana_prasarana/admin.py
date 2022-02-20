from django.contrib import admin

from django.utils.html import format_html
from django.utils import timezone

from import_export.admin import ImportExportModelAdmin, ExportMixin

from .filter_admin import *
from .models import *

class JenisSaranaAdmin (ImportExportModelAdmin):
    search_fields = ('KATEGORI',)
    list_display = ('KATEGORI',)
    list_per_page = 10
    
admin.site.register(JenisSarana, JenisSaranaAdmin)

class SaranaAdmin(ImportExportModelAdmin):
    search_fields = ('NAMA','JENIS__KATEGORI',)
    list_display = ('NAMA', 'JENIS','STATUS')
    list_per_page = 10
    list_filter = ('STATUS',)
    actions = ('acc_pengembalian',)
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS = 'Sudah Dikembalikan')
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Barang"

admin.site.register(Sarana, SaranaAdmin)

class PengajuanPeminjamanBarangAdmin(admin.ModelAdmin):
    search_fields = ('NAMA_PEMINJAM','ALAT__NAMA',)
    list_display = ('NAMA_PEMINJAM','NO_TELEPON', 'alat', 'KEGIATAN', 'TANGGAL_PENGAJUAN', 'TANGGAL_PENGGUNAAN','TANGGAL_PENGEMBALIAN','KETERANGAN','status_pengajuan', 'TANDA_TANGAN')
    list_per_page = 10 
    filter_horizontal = ('ALAT',)

    list_filter = ('STATUS_PENGAJUAN', )
    actions = ('accept_action', 'decline_action',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "ALAT":
            kwargs["queryset"] = Sarana.objects.filter(STATUS='Sudah Dikembalikan')
        return super(PengajuanPeminjamanBarangAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def alat(self, obj):
        daftar = ""
        for data in obj.ALAT.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanPeminjamanBarang.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan peminjaman"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanPeminjamanBarang.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan peminjaman"
    
    def status_pengajuan(self, obj):
        return (obj.STATUS_PENGAJUAN == 'Disetujui')       
        
    status_pengajuan.boolean = True
    
    def setuju(self, obj):
        data = PengajuanPeminjamanBarang.objects.get(ID=obj.ID)
        data.STATUS_PENGAJUAN = 'Disetujui'
        data.save()
    
    setuju.short_description = 'Setujui'
    
    def alat(self, obj):
        daftar = ""
        for data in obj.ALAT.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(PengajuanPeminjamanBarang, PengajuanPeminjamanBarangAdmin)

class RiwayatPeminjamanBarangAdmin(ImportExportModelAdmin):
    search_fields = ('NAMA_PEMINJAM','ALAT__NAMA',)
    list_display = ('NAMA_PEMINJAM','NO_TELEPON','alat','KEGIATAN', 'TANGGAL_PENGGUNAAN', 'TANGGAL_PENGEMBALIAN','KETERANGAN', 'status_peminjaman','TANDA_TANGAN')
    list_per_page = 10
    filter_horizontal = ('ALAT',)
    list_filter = ('STATUS_PEMINJAMAN', AlatFilter,)
    # autocomplete_fields = ['', ]
    actions = ('acc_pengembalian', )
    
    def status_peminjaman(self, obj):
        if obj.STATUS_PEMINJAMAN == 'Sedang Dipinjam' :
            date_now = timezone.localtime()
            if date_now.date() > obj.TANGGAL_PENGEMBALIAN :
                return 'Tenggat'
            elif date_now.date() <= obj.TANGGAL_PENGEMBALIAN : 
                return 'Sedang Dipinjam'
        elif obj.STATUS_PEMINJAMAN == 'Sudah Dikembalikan' :
            return 'Selesai'
        elif obj.STATUS_PEMINJAMAN == 'Ditolak' :
            return 'Ditolak'
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS_PEMINJAMAN = 'Sudah Dikembalikan')
        for d in queryset.values():
            riwayat = RiwayatPeminjamanBarang.objects.get(ID=d['ID'])
            for data in riwayat.ALAT.all():
                obj = Sarana.objects.get(ID=data.ID)
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
    
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Barang"
    
    def alat(self, obj):
        daftar = ""
        for data in obj.ALAT.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(RiwayatPeminjamanBarang, RiwayatPeminjamanBarangAdmin)

class PengajuanPeminjamanRuanganAdmin(admin.ModelAdmin):
    search_fields = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'RUANGAN__NAMA', 'KETERANGAN')
    list_display = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'RUANGAN' ,'TANGGAL_PENGAJUAN', 'TANGGAL_PEMAKAIAN','TANGGAL_BERAKHIR','JAM_PENGGUNAAN','JAM_BERAKHIR', 'JENIS_PEMINJAMAN', 'KETERANGAN','TANDA_TANGAN',)
    list_per_page = 10
    autocomplete_fields = ('RUANGAN',)
    list_filter = ('STATUS','JENIS_PEMINJAMAN')
    actions = ('accept_action','decline_action',)

    def accept_action(self, request, queryset):
        queryset.update(STATUS = 'Sedang Dipinjam')
        for d in queryset.values():
            obj = PengajuanPeminjamanRuangan.objects.get(ID=d['ID'])
            obj.save()

    accept_action.short_description = "Setujui pengajuan peminjaman"

    def decline_action(self, request, queryset):
        queryset.update(STATUS = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanPeminjamanRuangan.objects.get(ID=d['ID'])
            obj.save()

    decline_action.short_description = "Tolak pengajuan peminjaman"

    def status_pengajuan(self, obj):
        return (obj.STATUS == 'Sedang Dipinjam')       

    status_pengajuan.boolean = True

admin.site.register(PengajuanPeminjamanRuangan, PengajuanPeminjamanRuanganAdmin)

class RiwayatPeminjamanRuanganAdmin(ImportExportModelAdmin):
    search_fields = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'RUANGAN__NAMA', 'KETERANGAN')
    list_display = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'RUANGAN' ,'TANGGAL_PENGAJUAN', 'TANGGAL_PEMAKAIAN','TANGGAL_BERAKHIR','JAM_PENGGUNAAN','JAM_BERAKHIR', 'JENIS_PEMINJAMAN', 'KETERANGAN','TANDA_TANGAN', 'status_peminjaman',)
    list_per_page = 10 
    actions = ('acc_pengembalian',)
    list_filter = ('STATUS', RuanganFilter,)


    def status_peminjaman(self, obj):
        if obj.STATUS == 'Sedang Dipinjam' :
            date_now = timezone.localtime()
            print (type(date_now.date))
            if date_now.date() >= obj.TANGGAL_BERAKHIR and date_now.time() > obj.JAM_BERAKHIR :
                return 'Tenggat'
            elif date_now.date() <= obj.TANGGAL_BERAKHIR and date_now.time() <= obj.JAM_BERAKHIR : 
                return 'Sedang Dipinjam'
        elif obj.STATUS == 'Selesai Dipinjam' :
            return 'Selesai'
        elif obj.STATUS == 'Ditolak' :
            return 'Peminjaman Ditolak'

    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS = 'Selesai Dipinjam')
            
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Ruangan"

admin.site.register(RiwayatPeminjamanRuangan, RiwayatPeminjamanRuanganAdmin)


class JenisRuanganAdmin(admin.ModelAdmin):
    search_fields = ('KATEGORI', )
    list_display = ('KATEGORI',)
    list_per_page = 10

admin.site.register(JenisRuangan, JenisRuanganAdmin)

class RuanganAdmin(admin.ModelAdmin):
    search_fields = ('NAMA', 'JENIS__KATEGORI')
    list_display = ('NAMA', 'JENIS')
    list_per_page = 10
    autocomplete_fields = ('JENIS',)

admin.site.register(Ruangan, RuanganAdmin)

