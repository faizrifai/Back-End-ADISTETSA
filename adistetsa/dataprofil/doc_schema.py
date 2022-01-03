from typing_extensions import Required
from drf_yasg import openapi

schema_datakompetensiguru = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'BIDANG_STUDI': openapi.Schema(type=openapi.TYPE_STRING),
        'URUTAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_dataanakkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'STATUS': openapi.Schema(type=openapi.TYPE_STRING),
        'JENJANG': openapi.Schema(type=openapi.TYPE_STRING),
        'NISN': openapi.Schema(type=openapi.TYPE_INTEGER),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'JENIS_KELAMIN': openapi.Schema(type=openapi.TYPE_STRING),
        'TEMPAT_LAHIR': openapi.Schema(type=openapi.TYPE_STRING),
        'TANGGAL_LAHIR': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATE),
        'TAHUN_MASUK': openapi.Schema(type=openapi.TYPE_STRING),     
    }
)
schema_dataanakkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS': openapi.Schema(type=openapi.TYPE_STRING),
        'PENYELENGGARA': openapi.Schema(type=openapi.TYPE_STRING),
        'DARI_TAHUN': openapi.Schema(type=openapi.TYPE_INTEGER),
        'SAMPAI_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'MASIH_MENERIMA': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_databukukaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JUDUL_BUKU': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN_BUKU': openapi.Schema(type=openapi.TYPE_STRING),
        'PENERBIT_BUKU': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datadiklatkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS_DIKLAT': openapi.Schema(type=openapi.TYPE_STRING),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'PENYELENGGARA': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'PERAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datakaryatuliskaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JUDUL': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'PUBLIKASI': openapi.Schema(type=openapi.TYPE_STRING),
        'KETERANGAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datakesejahteraankaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS': openapi.Schema(type=openapi.TYPE_STRING),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'PENYELENGGARA': openapi.Schema(type=openapi.TYPE_STRING),
        'DARI_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'SAMPAI_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'STATUS': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datatunjangankaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS': openapi.Schema(type=openapi.TYPE_STRING),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'INSTANSI': openapi.Schema(type=openapi.TYPE_STRING),
        'SUMBER_DANA': openapi.Schema(type=openapi.TYPE_STRING),
        'DARI_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'SAMPAI_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'NOMINAL': openapi.Schema(type=openapi.TYPE_STRING),
        'STATUS': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datatugastambahankaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JABATAN_PTK': openapi.Schema(type=openapi.TYPE_STRING),
        'JPM': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_SK': openapi.Schema(type=openapi.TYPE_STRING),
        'TMT_TAMBAHAN': openapi.Schema(type=openapi.TYPE_STRING),
        'TST_TAMBAHAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datapenghargaankaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'TINGKAT_PERNGHARGAAN': openapi.Schema(type=openapi.TYPE_STRING),
        'JENIS_PENGHARGAAN': openapi.Schema(type=openapi.TYPE_STRING),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'INSTANSI': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datanilaiteskaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS': openapi.Schema(type=openapi.TYPE_STRING),
        'NAMA': openapi.Schema(type=openapi.TYPE_STRING),
        'PENYELENGGARA': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'SKOR': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatgajiberkalakaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'PANGKAT_GOLONGAN': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_SK': openapi.Schema(type=openapi.TYPE_STRING),
        'TANGGAL_SK': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATE),
        'TMT_KGB': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN_MK': openapi.Schema(type=openapi.TYPE_STRING),
        'BULAN_MK': openapi.Schema(type=openapi.TYPE_STRING),
        'GAJI_POKOK': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatjabatanstrukturalkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JABATAN_PTK': openapi.Schema(type=openapi.TYPE_STRING),
        'SK_STRUKTURAL': openapi.Schema(type=openapi.TYPE_STRING),
        'TMT_JABATAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatkepangkatankaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'PANGKAT_GOLONGAN': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_SK': openapi.Schema(type=openapi.TYPE_STRING),
        'TANGGAL_SK': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATE),
        'PANGKAT_GOLONGAN': openapi.Schema(type=openapi.TYPE_STRING),
        'MK_TAHUN': openapi.Schema(type=openapi.TYPE_STRING),
        'MK_BULAN': openapi.Schema(type=openapi.TYPE_STRING),

    }
)
schema_datariwayatpendidikanformalkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'BIDANG_STUDI': openapi.Schema(type=openapi.TYPE_STRING),
        'JENJANG': openapi.Schema(type=openapi.TYPE_STRING),
        'GELAR': openapi.Schema(type=openapi.TYPE_STRING),
        'SATUAN': openapi.Schema(type=openapi.TYPE_STRING),
        'FAKULTAS': openapi.Schema(type=openapi.TYPE_STRING),
        'KEPENDIDIKAN': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN_MASUK': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN_LULUS': openapi.Schema(type=openapi.TYPE_STRING),
        'NIM': openapi.Schema(type=openapi.TYPE_STRING),
        'MASIH': openapi.Schema(type=openapi.TYPE_STRING),
        'SMT': openapi.Schema(type=openapi.TYPE_STRING),
        'IPK': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatsertifikasikaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENIS_SERTIFIKASI': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_SERTIFIKASI': openapi.Schema(type=openapi.TYPE_STRING),
        'TAHUN_SERTIFIKASI': openapi.Schema(type=openapi.TYPE_STRING),
        'BIDANG_STUDI': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_REGISTRASI': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_PESERTA': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatjabatanfungsionalkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JABATAN_FUNGSIONAL': openapi.Schema(type=openapi.TYPE_STRING),
        'SK_JABATAN_FUNGSIONAL': openapi.Schema(type=openapi.TYPE_STRING),
        'TMT_JABATAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
schema_datariwayatkarirkaryawan = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        'JENJANG': openapi.Schema(type=openapi.TYPE_STRING),
        'JENIS_LEMBAGA': openapi.Schema(type=openapi.TYPE_STRING),
        'STS_KEPEGAWAIAN': openapi.Schema(type=openapi.TYPE_STRING),
        'JENIS_PTK': openapi.Schema(type=openapi.TYPE_STRING),
        'LEMBAGA': openapi.Schema(type=openapi.TYPE_STRING),
        'NO_SK_KERJA': openapi.Schema(type=openapi.TYPE_STRING),
        'TGL_SK_KERJA': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATE),
        'TMT_KERJA': openapi.Schema(type=openapi.TYPE_STRING),
        'TST_KERJA': openapi.Schema(type=openapi.TYPE_STRING),
        'TEMPAT_KERJA': openapi.Schema(type=openapi.TYPE_STRING),
        'TTD_SK_KERJA': openapi.Schema(type=openapi.TYPE_STRING),
        'MAPEL_DIAJARKAN': openapi.Schema(type=openapi.TYPE_STRING),
    }
)