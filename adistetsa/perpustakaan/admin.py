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

def judul(obj):
    name = "%s" % obj.JUDUL
    return Truncator(name).chars(7)

def isbn(obj):
    name = "%s" % obj.ISBN
    return Truncator(name).chars(7)

class KatalogBukuAdmin(ImportExportModelAdmin):
    search_fields = ['REGISTER', 'ISBN', 'JUDUL', 'VOLUME', 'EDISI', 'BAHASA', 'DUPLIKAT', 'TAHUN_TERBIT', 'KOTA_PENERBIT', 'PENERBIT']
    list_per_page = 10
    list_display = ('REGISTER', isbn, judul, 'VOLUME', 'EDISI', 'BAHASA', 'DUPLIKAT', 'KODE_MEDIA','TIPE_KODE', 'NOMER_DEWEY', 'KODE_AUTHOR', 'TAHUN_TERBIT', 'KOTA_PENERBIT', 'PENERBIT', 'DESKRIPSI_FISIK', 'INDEX', 'BIBLIOGRAPHY', 'TANGGAL_PENERIMAAN')
    list_filter = (TahunTerbitFilter, BahasaFilter, AuthorFilter, MediaFilter, TipeBukuFilter,)
    # resource_class = BookMainResource
    
class TahunTerbitAdmin(admin.ModelAdmin):
    search_fields = ['TAHUN_TERBIT']

admin.site.register(TahunTerbit, TahunTerbitAdmin)

admin.site.register(KatalogBuku, KatalogBukuAdmin)

class TipeBahasaAdmin(admin.ModelAdmin):
    search_fields = ['KODE_TIPE', 'KODE_BAHASA']
       
admin.site.register(TipeBahasa,TipeBahasaAdmin)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['KODE_AUTHOR', 'NAMA_AUTHOR'] 

admin.site.register(Author, AuthorAdmin)

class TipeMediaAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_MEDIA', 'NAMA_MEDIA']
    list_per_page = 10
    list_display = ('KODE_MEDIA', 'NAMA_MEDIA')
    # resource_class = MediaTypeResource

admin.site.register(TipeMedia, TipeMediaAdmin)

class TipeBukuAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_TIPE', 'NAMA_TIPE', 'LAMA_PINJAM', 'DENDA']
    list_per_page = 10
    list_display = ('KODE_TIPE', 'NAMA_TIPE', 'LAMA_PINJAM', 'DENDA')
    # resource_class = BookTypeResource
    
admin.site.register(TipeBuku, TipeBukuAdmin)

class PendanaanAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_PENDANAAN', 'NAMA_PENDANAAN']
    list_per_page = 10
    list_display = ('KODE_PENDANAAN', 'NAMA_PENDANAAN')
    # resource_class = FundingResource

admin.site.register(Pendanaan, PendanaanAdmin)

class LokasiAdmin(ImportExportModelAdmin):
    search_fields = ['KODE_LOKASI', 'NAMA_LOKASI']
    list_per_page = 10
    list_display = ('KODE_LOKASI', 'NAMA_LOKASI')
    # resource_class = LocationResource

admin.site.register(Lokasi, LokasiAdmin)

class LokasiSpesifikAdmin(ImportExportModelAdmin):
    search_fields = ['LOKASI_SPESIFIK', 'NAMA']
    list_per_page = 10
    list_display = ('LOKASI_SPESIFIK', 'NAMA')
    # resource_class = LocationSpecificationResource

admin.site.register(LokasiSpesifik, LokasiSpesifikAdmin)

class OperatorAdmin(ImportExportModelAdmin):
    # search_fields = ['KODE_OPERATOR', 'NAMA_OPERATOR', 'NAMA_LENGKAP']
    list_per_page = 10
    list_display = ('KODE_OPERATOR',)
    # resource_class = OperatorResource
    
admin.site.register(Operator, OperatorAdmin)

class LoanSiswaPendekAdmin(ImportExportModelAdmin):
    search_fields = ['NIS', 'OUT_DATE', 'DUE_DATE', 'LOAN_STATUS', 'IS_PRINTED', 'OPERATOR_CODE']
    list_per_page = 10
    list_display = ('NIS', 'OUT_DATE', 'DUE_DATE', 'LOAN_STATUS', 'IS_PRINTED', 'OPERATOR_CODE')
    # resource_class = LoanSiswaPendekResource
    
admin.site.register(LoanSiswaPendek, LoanSiswaPendekAdmin)

class LoanSiswaPanjangAdmin(ImportExportModelAdmin):
    search_fields = ['NIS', 'KELAS', 'ALAMAT', 'TANGGAL_PINJAM', 'REGISTER', 'NO_BARCODE', 'JUMLAH', 'TANDA_TANGAN', 'KETERANGAN', 'LOAN_STATUS']
    list_per_page = 10
    list_display = ('NIS', 'KELAS', 'ALAMAT', 'TANGGAL_PINJAM', 'REGISTER', 'NO_BARCODE', 'JUMLAH', 'TANDA_TANGAN', 'KETERANGAN', 'LOAN_STATUS')
    # resource_class = LoanSiswaPanjangResource
    
admin.site.register(LoanSiswaPanjang, LoanSiswaPanjangAdmin)

class LoanGuruPendekAdmin(ImportExportModelAdmin):
    search_fields = ['NIP', 'OUT_DATE', 'DUE_DATE', 'LOAN_STATUS', 'IS_PRINTED', 'OPERATOR_CODE']
    list_per_page = 10
    list_display = ('NIP', 'OUT_DATE', 'DUE_DATE', 'LOAN_STATUS', 'IS_PRINTED', 'OPERATOR_CODE')
    # resource_class = LoanGuruPendekResource
    
admin.site.register(LoanGuruPendek, LoanGuruPendekAdmin)

class LoanGuruPanjangAdmin(ImportExportModelAdmin):
    search_fields = ['NIP', 'KELAS', 'ALAMAT', 'TANGGAL_PINJAM', 'REGISTER', 'NO_BARCODE', 'JUMLAH', 'TANDA_TANGAN', 'KETERANGAN', 'LOAN_STATUS']
    list_per_page = 10
    list_display = ('NIP', 'KELAS', 'ALAMAT', 'TANGGAL_PINJAM', 'REGISTER', 'NO_BARCODE', 'JUMLAH', 'TANDA_TANGAN', 'KETERANGAN', 'LOAN_STATUS')
    # resource_class = LoanGuruPanjangResource
    
admin.site.register(LoanGuruPanjang, LoanGuruPanjangAdmin)

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