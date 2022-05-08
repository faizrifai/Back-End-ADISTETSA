from .models import *
from kurikulum.models import KelasSiswa
from rest_framework import serializers

class DataSiswaSerializer(serializers.ModelSerializer):
    KELAS = serializers.SerializerMethodField('get_kelas')

    class Meta:
        model = DataSiswa
        fields = '__all__'

    def get_kelas(self, obj):
        kelas_siswa = KelasSiswa.objects.filter(NIS=obj).last()
        return str(kelas_siswa.KELAS.KELAS.TINGKATAN) + " " + str(kelas_siswa.KELAS.KELAS.JURUSAN) + " " + str(kelas_siswa.KELAS.OFFERING.NAMA)  

class DataOrangTuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataOrangTua
        fields = '__all__'
        
class DataKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryawan
        fields = '__all__'
       
class DataGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataGuru
        fields = '__all__'

class DataKompetensiGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiGuru
        exclude = ['OWNER']

class DataKompetensiKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKompetensiKaryawan
        exclude = ['OWNER']

class DataAnakGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakGuru
        exclude = ['OWNER']

class DataAnakKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnakKaryawan
        exclude = ['OWNER']

class DataBeasiswaGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaGuru
        exclude = ['OWNER']

class DataBeasiswaKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBeasiswaKaryawan
        exclude = ['OWNER']
        
class DataBukuGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBukuGuru
        exclude = ['OWNER']

class DataBukuKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBukuKaryawan
        exclude = ['OWNER']

class DataDiklatKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDiklatKaryawan
        exclude = ['OWNER']

class DataKaryaTulisKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryaTulisKaryawan
        exclude = ['OWNER']

class DataKesejahteraanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKesejahteraanKaryawan
        exclude = ['OWNER']

class DataTunjanganKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTunjanganKaryawan
        exclude = ['OWNER']

class DataTugasTambahanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTugasTambahanKaryawan
        exclude = ['OWNER']

class DataPenghargaanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPenghargaanKaryawan
        exclude = ['OWNER']

class DataNilaiTesKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataNilaiTesKaryawan
        exclude = ['OWNER']

class DataRiwayatGajiBerkalaKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatGajiBerkalaKaryawan
        exclude = ['OWNER']

class DataRiwayatJabatanStrukturalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanStrukturalKaryawan
        exclude = ['OWNER']

class DataRiwayatKepangkatanKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKepangkatanKaryawan
        exclude = ['OWNER']
        
class DataRiwayatPendidikanFormalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatPendidikanFormalKaryawan
        exclude = ['OWNER']
        
class DataRiwayatSertifikasiKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatSertifikasiKaryawan
        exclude = ['OWNER']
        
class DataRiwayatJabatanFungsionalKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanFungsionalKaryawan
        exclude = ['OWNER']
        
class DataRiwayatKarirKaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKarirKaryawan
        exclude = ['OWNER']
        
class DataDiklatGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDiklatGuru
        exclude = ['OWNER']

class DataKaryaTulisGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKaryaTulisGuru
        exclude = ['OWNER']

class DataKesejahteraanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataKesejahteraanGuru
        exclude = ['OWNER']

class DataTunjanganGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTunjanganGuru
        exclude = ['OWNER']

class DataTugasTambahanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTugasTambahanGuru
        exclude = ['OWNER']

class DataPenghargaanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPenghargaanGuru
        exclude = ['OWNER']

class DataNilaiTesGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataNilaiTesGuru
        exclude = ['OWNER']

class DataRiwayatGajiBerkalaGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatGajiBerkalaGuru
        exclude = ['OWNER']

class DataRiwayatJabatanStrukturalGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanStrukturalGuru
        exclude = ['OWNER']

class DataRiwayatKepangkatanGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKepangkatanGuru
        exclude = ['OWNER']

class DataRiwayatPendidikanFormalGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatPendidikanFormalGuru
        exclude = ['OWNER']

class DataRiwayatSertifikasiGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatSertifikasiGuru
        exclude = ['OWNER']

class DataRiwayatJabatanFungsionalGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatJabatanFungsionalGuru
        exclude = ['OWNER']

class DataRiwayatKarirGuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRiwayatKarirGuru
        exclude = ['OWNER']
