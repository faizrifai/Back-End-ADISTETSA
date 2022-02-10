from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin, ExportMixin

from .filter_admin import *
from .models import *

admin.site.register(JamPenggunaan)
admin.site.register(HariPenggunaan)

class JenisSaranaAdmin (ImportExportModelAdmin):
    search_fields = ('ID',)
    list_display = ('KATEGORI',)
    list_per_page = 10
    
admin.site.register(JenisSarana, JenisSaranaAdmin)

class SaranaAdmin(ImportExportModelAdmin):
    search_fields = ('',)
    list_display = ('NAMA', 'JENIS','STATUS')
    list_per_page = 10
    list_filter = ('STATUS',)
    actions = ('acc_pengembalian',)
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS = 'Sudah Dikembalikan')
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Barang"

admin.site.register(Sarana, SaranaAdmin)
admin.site.register(JenisRuangan)
admin.site.register(Ruangan)

class PengajuanPeminjamanBarangAdmin(admin.ModelAdmin):
    search_fields = ('ALAT',)
    list_display = ('NAMA_PEMINJAM','NO_TELEPON', 'alat', 'KEGIATAN', 'TANGGAL_PENGAJUAN', 'TANGGAL_PENGGUNAAN','TANGGAL_PENGEMBALIAN','KETERANGAN','status_pengajuan', 'TANDA_TANGAN')
    list_per_page = 10 
    filter_horizontal = ('ALAT',)
    # autocomplete_fields = [' ' ]
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

class RiwayatPeminjamanBarangAdmin(admin.ModelAdmin):
    search_fields = ('',)
    list_display = ('NAMA_PEMINJAM','NO_TELEPON','alat','KEGIATAN', 'TANGGAL_PENGGUNAAN', 'TANGGAL_PENGEMBALIAN','KETERANGAN', 'status_peminjaman','TANDA_TANGAN')
    list_per_page = 10
    filter_horizontal = ('ALAT',)
    list_filter = ('STATUS_PEMINJAMAN',)
    # autocomplete_fields = ['', ]
    actions = ('acc_pengembalian',)
    
    def status_peminjaman(self, obj):
        if obj.STATUS_PEMINJAMAN == 'Sedang Dipinjam' :
            date_now = datetime.date.today()
            if date_now > obj.TANGGAL_PENGEMBALIAN :
                return 'Tenggat'
            elif date_now < obj.TANGGAL_PENGEMBALIAN : 
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

admin.site.register(PengajuanPeminjamanRuanganPendek)

class JadwalPenggunaanRuanganAdmin(admin.ModelAdmin):
    search_fields = ('RUANGAN', 'JAM', 'STATUS', 'HARI',)
    list_display = ('RUANGAN', 'JAM', 'STATUS', 'HARI',)
    list_per_page = 10 
    list_filter = ('STATUS',)
    autocomplete_fields = ('RUANGAN', 'JAM')
    actions = ('confirm_action',)


    def confirm_action(self, request, queryset):
        queryset.update(STATUS = 'Selesai Dipinjam')
        for d in queryset.values():
            obj = JadwalPenggunaanRuangan.objects.get(ID=d['ID'])
            obj.save()

    confirm_action.short_description = "Konfirmasi Ruangan"

admin.site.register(JadwalPenggunaanRuangan, JadwalPenggunaanRuanganAdmin)

class PengajuanPeminjamanRuanganAdmin(admin.ModelAdmin):
    search_fields = ('PENGGUNA','PENGGUNA', 'NO_HP', 'KEGIATAN', 'RUANGAN__NAMA', 'KETERANGAN')
    list_display = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'peminjaman_ruangan','TANGGAL_PENGAJUAN', 'TANGGAL_PENGGUNAAN', 'KETERANGAN', 'status_pengajuan')
    list_per_page = 10
    filter_horizontal = ('RUANGAN',)
    list_filter = ('STATUS',)
    # autocomplete_fields = ['RUANGAN', ]
    actions = ('accept_action','decline_action',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "RUANGAN":
            kwargs["queryset"] = JadwalPenggunaanRuangan.objects.filter(STATUS='Selesai Dipinjam')
        return super(PengajuanPeminjamanRuanganAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

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

    def peminjaman_ruangan(self, obj):
        daftar = ""
        for data in obj.RUANGAN.all():
            daftar += str(data) + "<br>"

        return format_html(daftar)

admin.site.register(PengajuanPeminjamanRuangan, PengajuanPeminjamanRuanganAdmin)

class RiwayatPeminjamanRuanganAdmin(admin.ModelAdmin):
    serach_fields = ('ID', 'PENGGUNA', 'NO_HP', 'KEGIATAN',)
    list_display = ('PENGGUNA', 'NO_HP', 'KEGIATAN', 'peminjaman_ruangan', 'TANGGAL_PENGAJUAN', 'TANGGAL_SELESAI', 'KETERANGAN', 'status_peminjaman')
    list_per_page = 10 
    actions = ('accept_action', 'acc_pengembalian',)


    def status_peminjaman(self, obj):
        if obj.STATUS == 'Sedang Dipinjam' :
            date_now = datetime.date.today()
            if date_now > obj.TANGGAL_SELESAI :
                return 'Tenggat'
            elif date_now < obj.TANGGAL_SELESAI : 
                return 'Sedang Dipinjam'
        elif obj.STATUS == 'Selesai Dipinjam' :
            return 'Selesai'
        elif obj.STATUS == 'Ditolak' :
            return 'Peminjaman Ditolak'

    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS = 'Selesai Dipinjam')
        for d in queryset.values():
            riwayat = RiwayatPeminjamanRuangan.objects.get(ID=d['ID'])
            for data in riwayat.RUANGAN.all():
                obj = JadwalPenggunaanRuangan.objects.get(ID=data.ID)
                obj.STATUS = 'Selesai Dipinjam'
                obj.save()


    acc_pengembalian.short_description = "Konfirmasi Pengembalian Ruangan"

    def peminjaman_ruangan(self, obj):
        daftar = ""
        for data in obj.RUANGAN.all():
            daftar += str(data) + "<br>"

        return format_html(daftar)

admin.site.register(RiwayatPeminjamanRuangan, RiwayatPeminjamanRuanganAdmin)
# class RiwayatPeminjamanRuanganPendek(admin.ModelAdmin):
#     search_fields = ('')


class JamPenggunaanAdmin(admin.ModelAdmin):
    search_fields = ('JAM_KE', 'PUKUL',)
    list_display = ('JAM_KE', 'PUKUL')
    list_per_page = 10

admin.site.register(JamPenggunaan, JamPenggunaanAdmin)

class HariPenggunaanAdmin(admin.ModelAdmin):
    search_fields = ('HARI', 'JAM__JAM_KE')
    list_display = ('HARI', 'JAM')
    list_per_page = 10
    autocomplete_fields = ('JAM',)

admin.site.register(HariPenggunaan, HariPenggunaanAdmin)

admin.site.register(JenisSarana)
admin.site.register(Sarana)

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

admin.site.register(PengajuanPeminjamanBarang)