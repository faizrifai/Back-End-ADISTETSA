from django.contrib.auth.models import User, Group

from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources

from .models import *
class BookMainResource(resources.ModelResource):
    
    
    kode_media = Field(
        column_name='KODE_MEDIA',
        attribute='KODE_MEDIA',
        widget=ForeignKeyWidget(TipeMedia, 'KODE_MEDIA')
    )
    
    kode_tipe = Field(
        column_name='KODE_TIPE',
        attribute='KODE_TIPE',
        widget=ForeignKeyWidget(TipeBuku, 'KODE_TIPE')
    )
    
    kode_lokasi = Field(
        column_name='KODE_LOKASI',
        attribute='KODE_LOKASI',
        widget=ForeignKeyWidget(Lokasi, 'KODE_LOKASI')
    )
    
    lokasi_spesifik = Field(
        column_name='LOKASI_SPESIFIK',
        attribute='LOKASI_SPESIFIK',
        widget=ForeignKeyWidget(LokasiSpesifik, 'LOKASI_SPESIFIK')
    )
    
    class Meta:
        model = KatalogBuku
        fields = ('REGISTER','ISBN','JUDUL','VOLUME','EDISI','BAHASA','kode_media','kode_tipe','NOMER_DEWEY','KODE_AUTHOR','KODE_JUDUL','TAHUN_TERBIT','KOTA_PENERBIT','PENERBIT','DESKRIPSI_FISIK','INDEX','BIBLIOGRAPHY','kode_lokasi','lokasi_spesifik','HARGA','DATA_ENTRY','OPERATOR_CODE')
        import_id_fields = ('REGISTER',)
        export_order = ['REGISTER','ISBN','JUDUL','VOLUME','EDISI','BAHASA','kode_media','kode_tipe','NOMER_DEWEY','KODE_AUTHOR','KODE_JUDUL','TAHUN_TERBIT','KOTA_PENERBIT','PENERBIT','DESKRIPSI_FISIK','INDEX','BIBLIOGRAPHY','kode_lokasi','lokasi_spesifik','HARGA','DATA_ENTRY','OPERATOR_CODE']

class DonasiBukuResource(resources.ModelResource):
    
    kode_donasi = Field(
        column_name='KODE_DONASI',
        attribute='KODE_DONASI',
        widget=ForeignKeyWidget(Pendanaan, 'KODE_PENDANAAN')
    )
    
    def before_import_row(self, row, **kwargs):
        tanggal_penerimaan = datetime.datetime.fromisoformat(row['TANGGAL_PENERIMAAN']).astimezone(datetime.timezone.utc)
        data_entry = datetime.datetime.fromisoformat(row['DATA_ENTRY']).astimezone(datetime.timezone.utc)
        
        row['TANGGAL_PENERIMAAN'] = tanggal_penerimaan
        row['DATA_ENTRY'] = data_entry
        
    class Meta:
        model = DonasiBuku
        fields = ('REGISTER_DONASI', 'DUPLIKAT', 'KODE_DONASI','TANGGAL_PENERIMAAN','CATATAN_DONASI')
        import_id_fields = ('id',)
        export_order = ['REGISTER_DONASI', 'DUPLIKAT', 'KODE_DONASI','TANGGAL_PENERIMAAN','CATATAN_DONASI']

class MediaTypeResource(resources.ModelResource):

    class Meta:
        model = TipeMedia
        import_id_fields = ('KODE_MEDIA',)

class AuthorResource(resources.ModelResource):

    class Meta:
        model = Author
        import_id_fields = ('KODE_AUTHOR',)

class TipeBahasaResource(resources.ModelResource):

    class Meta:
        model = TipeBahasa
        import_id_fields = ('KODE_BAHASA',)

class BookTypeResource(resources.ModelResource):

    class Meta:
        model = TipeBuku
        import_id_fields = ('KODE_TIPE',)

class FundingResource(resources.ModelResource):

    class Meta:
        model = Pendanaan
        exclude = ('ID',)
        import_id_fields = ('KODE_PENDANAAN',)

class TahunTerbitResource(resources.ModelResource):

    class Meta:
        model = TahunTerbit
        import_id_fields = ('TAHUN_TERBIT',)
        
class LocationResource(resources.ModelResource):

    class Meta:
        model = Lokasi
        import_id_fields = ('KODE_LOKASI',)

class LocationSpecificationResource(resources.ModelResource):

    class Meta:
        model = LokasiSpesifik
        import_id_fields = ('LOKASI_SPESIFIK',)


# # Register your import_export resource model here
# class BookMainResource(resources.ModelResource):

#     class Meta:
#         model = BookMain

# class MediaTypeResource(resources.ModelResource):

#     class Meta:
#         model = MediaType

# class BookTypeResource(resources.ModelResource):

#     class Meta:
#         model = BookType

# class FundingResource(resources.ModelResource):

#     class Meta:
#         model = Funding
        
# class LocationResource(resources.ModelResource):

#     class Meta:
#         model = Location 

# class LocationSpecificationResource(resources.ModelResource):

#     class Meta:
#         model = LocationSpecification

# class OperatorResource(resources.ModelResource):

#     class Meta:
#         model = Operator   

# class LoanSiswaPendekResource(resources.ModelResource):

#     class Meta:
#         model = LoanSiswaPendek 
        
# class LoanSiswaPanjangResource(resources.ModelResource):

#     class Meta:
#         model = LoanSiswaPanjang

# class LoanGuruPendekResource(resources.ModelResource):

#     class Meta:
#         model = LoanSiswaPendek 
        
# class LoanGuruPanjangResource(resources.ModelResource):

#     class Meta:
#         model = LoanSiswaPanjang

# class AbstrakResource(resources.ModelResource):

#     class Meta:
#         model = Abstrak

# class SiswaVisitResource(resources.ModelResource):

#     class Meta:
#         model = SiswaVisit

# class GuruVisitResource(resources.ModelResource):

#     class Meta:
#         model = GuruVisit
        
# # class BookOriginalTitleResource(resources.ModelResource):

# #     class Meta:
# #         model = BookOriginalTitle
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK_AYAH', 'NIK_IBU')

# # class BookSeriesTitleResource(resources.ModelResource):

# #     class Meta:
# #         model = BookSeriesTitle
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)

# # class BookSubjectResource(resources.ModelResource):
# #     class Meta:
# #         model = BookSubject
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookTypeResource(resources.ModelResource):
# #     class Meta:
# #         model = BookType
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookCreatorResource(resources.ModelResource):
# #     class Meta:
# #         model = BookCreator
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)    
        
# # class BookAddCopyResource(resources.ModelResource):
# #     class Meta:
# #         model = BookAddCopy
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookNoteAddResource(resources.ModelResource):
# #     class Meta:
# #         model = BookNoteAdd
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookNoteResource(resources.ModelResource):
# #     class Meta:
# #         model = BookNote
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookLoanRuleResource(resources.ModelResource):
# #     class Meta:
# #         model = BookLoanRule
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
# # class BookStatusLogResource(resources.ModelResource):
# #     class Meta:
# #         model = BookStatusLog
# #         exclude = ('ID',)
# #         import_id_fields = ('NIK',)
        
    