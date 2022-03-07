from atexit import register
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.html import format_html
from .filter_admin import *

from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import *
from .importexportresources import *

# Register your models here.

# admin.site.register(BookOriginalTitle)
# admin.site.register(BookSeriesTitle)
# admin.site.register(BookSubject)

# admin.site.register(CirculationProblemType)
# admin.site.register(BookComment)
# admin.site.register(DigitalLibrary)
# admin.site.register(Abstrak)
# admin.site.register(InfoUmum)
# admin.site.register(NO_KTA)
# admin.site.register(NO_REG)
# admin.site.register(StockOpname)
# admin.site.register(BookCreator)
# admin.site.register(BookAddCopy)
# admin.site.register(BookNoteAdd)
# admin.site.register(BookNote)
# admin.site.register(BookLoanRule)
# admin.site.register(BookStatusLog)
# admin.site.register(CirculationProblemHistory)
# admin.site.register(CirculationProblem)
# admin.site.register(Departement)

# admin.site.register(Faculty)
# admin.site.register(Employe)


# admin.site.register(LoanHistory)
# admin.site.register(Holiday)
# admin.site.register(MemberMaxLoan)
# admin.site.register(MemberFreeOnLoanHistory)
# admin.site.register(MemberType)
# admin.site.register(MemberVisitHistory)
# admin.site.register(MemberRegisterHistory)
# admin.site.register(MemberVisit)

# admin.site.register(Member)

# admin.site.register(Response)
# admin.site.register(Program)
# admin.site.register(Strata)
# admin.site.register(Student)
# admin.site.register(ViewListUser)
# admin.site.register(Anggota_Aktif)
# admin.site.register(Peminjaman_Jenis_Koleksi)
# admin.site.register(Peminjaman)
# admin.site.register(BookMainGrouping)
# admin.site.register(Pengembalian_Jenis_Koleksi)
# admin.site.register(BookRptTitleByStudyProgram)
# admin.site.register(BookRptExemplarByStudyProgram)
# admin.site.register(BookRptAddCopyByStudyProgram)
# admin.site.register(CirculationFine)
# admin.site.register(CirculationMaxLoan)
# admin.site.register(CirculationNeverLate)
# admin.site.register(CirculationMaxVisit)
# admin.site.register(CirculationLoanByFaculty)
# admin.site.register(CirculationStatCheckin)
# admin.site.register(CrossTab)
# admin.site.register(CirculationStatFine)
# admin.site.register(CirculationStatLoan)
# admin.site.register(GroupNoCopy)
# admin.site.register(DailyFinePaid)
# admin.site.register(GroupNoTitle)
# admin.site.register(MemberCard)
# admin.site.register(MemberGroupVisitByFHour)
# admin.site.register(MemberGroupVisitByFacility)
# admin.site.register(MemberStatVisitByFHour)
# admin.site.register(OLapCirculationCheckIn)
# admin.site.register(OLapBookCopyProduction)
# admin.site.register(OLapBookTitleProduction)
# admin.site.register(OLapCirculationFine)
# admin.site.register(OLapLoan)
# admin.site.register(OLapMemberVisit)
# admin.site.register(OLapMemberActive)
# admin.site.register(OLapPengembalianJenisKoleksi)
# admin.site.register(OLapPeminjamanJenisKoleksi)
# admin.site.register(OperatorName)
# admin.site.register(StopN01TitleReference)
# admin.site.register(StopN01DataReference)
# admin.site.register(StudyProgram)
# admin.site.register(TotalOfTitle)
# admin.site.register(TransDataProgram)
# admin.site.register(TestStopnCirculationDtsource)
# admin.site.register(DeskripsiFisik)

class KatalogBukuCopyAdmin(ImportExportModelAdmin):
    search_fields = (
        'DATA_DONASI__REGISTER_DONASI__JUDUL',
        'DATA_DONASI__REGISTER_DONASI__KODE_AUTHOR__NAMA_AUTHOR',
        'DATA_DONASI__REGISTER_DONASI__BAHASA__BAHASA',
        'DATA_DONASI__REGISTER_DONASI__KODE_TIPE__NAMA_TIPE',
        'DATA_DONASI__REGISTER_DONASI__TAHUN_TERBIT__TAHUN_TERBIT',
    )
    list_display = ('DATA_DONASI', 'REGISTER_COPY', 'STATUS')
    list_per_page = 10
    list_filter = ('STATUS',)
    actions = ('acc_pengembalian',)

    change_list_template = 'perpustakaan/katalogbukucopy_changelist.html'
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS = 'Sudah Dikembalikan')
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Buku"

admin.site.register(KatalogBukuCopy, KatalogBukuCopyAdmin)

class DonasiBukuAdmin (ImportExportModelAdmin):
    search_fields = ('REGISTER_DONASI',)
    list_display = ('REGISTER_DONASI', 'DUPLIKAT', 'KODE_DONASI','TANGGAL_PENERIMAAN','CATATAN_DONASI')
    list_per_page = 10
    resource_class = DonasiBukuResource

admin.site.register(DonasiBuku, DonasiBukuAdmin)

def judul(obj):
    name = "%s" % obj.JUDUL
    return Truncator(name).chars(7)

def isbn(obj):
    name = "%s" % obj.ISBN
    return Truncator(name).chars(7)

class KatalogBukuAdmin(ImportExportModelAdmin):
    search_fields = ['REGISTER', 'ISBN', 'JUDUL', 'VOLUME', 'EDISI', 'BAHASA__BAHASA', 'TAHUN_TERBIT__TAHUN_TERBIT', 'KOTA_PENERBIT', 'PENERBIT']
    list_per_page = 10
    list_display = ('REGISTER', isbn, judul, 'VOLUME', 'EDISI', 'BAHASA', 'KODE_MEDIA', 'KODE_TIPE', 'NOMER_DEWEY', 'KODE_AUTHOR', 'TAHUN_TERBIT', 'KOTA_PENERBIT', 'PENERBIT', 'DESKRIPSI_FISIK', 'INDEX', 'BIBLIOGRAPHY', 'jumlah_tersedia')
    list_filter = (TahunTerbitFilter, BahasaFilter, AuthorFilter, MediaFilter, TipeBukuFilter,)
    resource_class = BookMainResource
    
    def jumlah_tersedia(self, obj):
        total_tersedia = 0
        total = 0
        
        donasi_buku = DonasiBuku.objects.filter(REGISTER_DONASI=obj.REGISTER)
        for data_donasi in donasi_buku:
            buku_copy = KatalogBukuCopy.objects.filter(DATA_DONASI=data_donasi)
            for data in buku_copy:
                if data.STATUS == 'Sudah Dikembalikan':
                    total_tersedia += 1
                
                total += 1
                
        return str(total_tersedia) + '/' + str(total)
    
admin.site.register(KatalogBuku, KatalogBukuAdmin)
    
class TahunTerbitAdmin(ImportExportModelAdmin):
    search_fields = ['TAHUN_TERBIT']
    resource_class = TahunTerbitResource

admin.site.register(TahunTerbit, TahunTerbitAdmin)

class TipeBahasaAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_TIPE', 'KODE_BAHASA']
    resource_class = TipeBahasaResource
       
admin.site.register(TipeBahasa,TipeBahasaAdmin)

class AuthorAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_AUTHOR', 'NAMA_AUTHOR'] 
    resource_class = AuthorResource

admin.site.register(Author, AuthorAdmin)

class TipeMediaAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_MEDIA', 'NAMA_MEDIA']
    list_per_page = 10
    list_display = ('KODE_MEDIA', 'NAMA_MEDIA')
    resource_class = MediaTypeResource

admin.site.register(TipeMedia, TipeMediaAdmin)

class TipeBukuAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_TIPE', 'NAMA_TIPE']
    list_per_page = 10
    list_display = ('KODE_TIPE', 'NAMA_TIPE')
    resource_class = BookTypeResource
    
admin.site.register(TipeBuku, TipeBukuAdmin)

class PendanaanAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_PENDANAAN', 'NAMA_PENDANAAN']
    list_per_page = 10
    list_display = ('KODE_PENDANAAN', 'NAMA_PENDANAAN')
    resource_class = FundingResource

admin.site.register(Pendanaan, PendanaanAdmin)

class LokasiAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_LOKASI', 'NAMA_LOKASI']
    list_per_page = 10
    list_display = ('KODE_LOKASI', 'NAMA_LOKASI')
    resource_class = LocationResource

admin.site.register(Lokasi, LokasiAdmin)

class LokasiSpesifikAdmin(ImportExportModelAdmin):
    search_fields = ['LOKASI_SPESIFIK', 'NAMA']
    list_per_page = 10
    list_display = ('LOKASI_SPESIFIK', 'NAMA')
    resource_class = LocationSpecificationResource

admin.site.register(LokasiSpesifik, LokasiSpesifikAdmin)

class OperatorAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_OPERATOR', 'UNIT']
    list_per_page = 10
    list_display = ('KODE_OPERATOR',)
    # resource_class = OperatorResource
    
admin.site.register(Operator, OperatorAdmin)


class PengajuanPeminjamanSiswaAdmin(admin.ModelAdmin):
    search_fields = search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'NIS__NIS', 'NIS__NAMA',)
    list_display = ('NIS', 'buku', 'TANGGAL_PENGAJUAN', 'status_pengajuan', 'JANGKA_PEMINJAMAN', 'FILE_TTD_PENGAJUAN')
    list_per_page = 10 
    filter_horizontal = ('BUKU',)
    autocomplete_fields = ['NIS', ]
    list_filter = ('STATUS_PENGAJUAN', )
    actions = ('accept_action', 'decline_action',)
    exclude = ('STATUS_PENGAJUAN',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "BUKU":
            kwargs["queryset"] = KatalogBukuCopy.objects.filter(STATUS='Sudah Dikembalikan')
        return super(PengajuanPeminjamanSiswaAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanPeminjamanSiswa.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan peminjaman"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanPeminjamanSiswa.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan peminjaman"
    
    def status_pengajuan(self, obj):
        return (obj.STATUS_PENGAJUAN == 'Disetujui')       
        
    status_pengajuan.boolean = True
    
    def setuju(self, obj):
        data = PengajuanPeminjamanSiswa.objects.get(ID=obj.ID)
        data.STATUS_PENGAJUAN = 'Disetujui'
        data.save()
    
    setuju.short_description = 'Setujui'
    
    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(PengajuanPeminjamanSiswa, PengajuanPeminjamanSiswaAdmin)

class RiwayatPeminjamanSiswaAdmin(ExportMixin,admin.ModelAdmin):
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'NIS__NIS', 'NIS__NAMA', 'JANGKA_PEMINJAMAN')
    list_display = ('NIS','buku', 'TANGGAL_PEMINJAMAN', 'TANGGAL_PENGEMBALIAN', 'JANGKA_PEMINJAMAN', 'FILE_TTD_PENGAJUAN', 'status_peminjaman')
    list_per_page = 10
    filter_horizontal = ('BUKU',)
    list_filter = ('STATUS_PEMINJAMAN',)
    autocomplete_fields = ['NIS', ]
    actions = ('acc_pengembalian',)
    resource_class = RiwayatPeminjamanSiswaResource
    
    
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
            return 'Peminjaman Ditolak'
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS_PEMINJAMAN = 'Sudah Dikembalikan')
        for d in queryset.values():
            riwayat = RiwayatPeminjamanSiswa.objects.get(ID=d['ID'])
            for data in riwayat.BUKU.all():
                obj = KatalogBukuCopy.objects.get(id=data.id)
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Buku"
    
    
    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(RiwayatPeminjamanSiswa, RiwayatPeminjamanSiswaAdmin)

class PengajuanPeminjamanGuruAdmin(admin.ModelAdmin):
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PENGAJUAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP',)
    list_display = ('DATA_GURU', 'buku', 'TANGGAL_PENGAJUAN', 'status_pengajuan', 'JANGKA_PEMINJAMAN', 'FILE_TTD_PENGAJUAN')
    list_per_page = 10 
    filter_horizontal = ('BUKU',)
    autocomplete_fields = ['DATA_GURU', ]
    list_filter = ('STATUS_PENGAJUAN', )
    actions = ('accept_action', 'decline_action',)
    exclude = ('STATUS_PENGAJUAN',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "BUKU":
            kwargs["queryset"] = KatalogBukuCopy.objects.filter(STATUS='Sudah Dikembalikan')
        return super(PengajuanPeminjamanGuruAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)
    
    def accept_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Disetujui')
        for d in queryset.values():
            obj = PengajuanPeminjamanGuru.objects.get(ID=d['ID'])
            obj.save()
        
    
    accept_action.short_description = "Setujui pengajuan peminjaman"
    
    def decline_action(self, request, queryset):
        queryset.update(STATUS_PENGAJUAN = 'Ditolak')
        for d in queryset.values():
            obj = PengajuanPeminjamanGuru.objects.get(ID=d['ID'])
            obj.save()
    
    decline_action.short_description = "Tolak pengajuan peminjaman"
    
    def status_pengajuan(self, obj):
        return (obj.STATUS_PENGAJUAN == 'Disetujui')       
        
    status_pengajuan.boolean = True
    
    def setuju(self, obj):
        data = PengajuanPeminjamanGuru.objects.get(ID=obj.ID)
        data.STATUS_PENGAJUAN = 'Disetujui'
        data.save()
    
    setuju.short_description = 'Setujui'
    
    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(PengajuanPeminjamanGuru, PengajuanPeminjamanGuruAdmin)

class RiwayatPeminjamanGuruAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ('BUKU__DATA_DONASI__REGISTER_DONASI__JUDUL', 'STATUS_PEMINJAMAN', 'DATA_GURU__NIK', 'DATA_GURU__NAMA_LENGKAP', 'JANGKA_PEMINJAMAN')
    list_display = ('DATA_GURU','buku', 'TANGGAL_PEMINJAMAN', 'TANGGAL_PENGEMBALIAN', 'JANGKA_PEMINJAMAN', 'FILE_TTD_PENGAJUAN', 'status_peminjaman')
    list_per_page = 10
    filter_horizontal = ('BUKU',)
    list_filter = ('STATUS_PEMINJAMAN',)
    autocomplete_fields = ['DATA_GURU', ]
    actions = ('acc_pengembalian',)
    resource_class = RiwayatPeminjamanGuruResource
    
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
            return 'Peminjaman Ditolak'
    
    def acc_pengembalian(self, request, queryset):
        queryset.update(STATUS_PEMINJAMAN = 'Sudah Dikembalikan')
        for d in queryset.values():
            riwayat = RiwayatPeminjamanGuru.objects.get(ID=d['ID'])
            for data in riwayat.BUKU.all():
                obj = KatalogBukuCopy.objects.get(id=data.id)
                obj.STATUS = 'Sudah Dikembalikan'
                obj.save()
    
    
    acc_pengembalian.short_description = "Konfirmasi Pengembalian Buku"
    
    
    def buku(self, obj):
        daftar = ""
        for data in obj.BUKU.all():
            daftar += str(data) + "<br>"
            
        return format_html(daftar)

admin.site.register(RiwayatPeminjamanGuru, RiwayatPeminjamanGuruAdmin)



# class AbstrakAdmin(ImportExportModelAdmin):
#     search_fields = ['REGISTER', 'ABSTRAK']
#     list_per_page = 10
#     list_display = ('REGISTER', 'ABSTRAK')
#     resource_class = AbstrakResource

# admin.site.register(Abstrak, AbstrakAdmin)

# class SiswaVisitAdmin(ImportExportModelAdmin):
#     search_fields = ['NIS', 'VISIT_DATE']
#     list_per_page = 10
#     list_display = ('NIS', 'VISIT_DATE')
#     resource_class = SiswaVisitResource

# admin.site.register(SiswaVisit, SiswaVisitAdmin)

# class GuruVisitAdmin(ImportExportModelAdmin):
#     search_fields = ['NIP', 'VISIT_DATE']
#     list_per_page = 10
#     list_display = ('NIP', 'VISIT_DATE')
#     resource_class = GuruVisitResource

# admin.site.register(GuruVisit, GuruVisitAdmin)