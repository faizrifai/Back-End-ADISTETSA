# class Response (models.Model):
#     NUMBER = models.BigIntegerField()
#     RESPONSE = models.CharField()

# class Program (models.Model):
#     PROGRAM_CODE = models.CharField()
#     FULL_NAME = models.CharField()
#     MEMBER_CODE = models.CharField()
#     FACULTY_ID = models.BigIntegerField()

# class Strata (models.Model):
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     STRATA = models.CharField(
#         choices=ENUM_STRATA,
#     )

# class Student (models.Model):
#     STUDENT_ID = models.CharField()
#     NAME = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     PROGRAM_CODE = models.CharField()
#     PERIOD = models.CharField()
#     BIRTH_DATE = models.DateField()
#     ADDRESS = models.CharField()
#     POSTAL_CODE = models.CharField()
#     PHONE = models.CharField()
#     ORG_ADDRESS = models.CharField()
#     ORG_POSTAL_CODE = models.CharField()
#     ORG_PHONE = models.CharField()

# class ViewListUser (models.Model):
#     USER_NAME = models.CharField()
#     PASSWORD =  models.CharField()
#     FULL_ACCESS = models.CharField(
#         choices=ENUM_FULL_ACCESS,
#     )
#     JUMLAH_KOLEKSI_BUKU = models.CharField(
#         choices=ENUM_JUMLAH_KOLEKSI_BUKU,
#     )
#     ENTRY_BUKU_HARI = models.CharField(
#         choices=ENUM_ENTRY_BUKU_HARI,
#     )
#     ENTRY_BUKU_BULAN = models.CharField(
#         choices=ENUM_ENTRY_BUKU_BULAN,
#     )
#     ENTRY_BUKU_TAHUN = models.CharField(
#         choices=ENUM_ENTRY_BUKU_TAHUN,
#     )
#     REKAP_DENDA_HARI = models.CharField(
#         choices=ENUM_REKAP_DENDA_HARI,
#     )
#     REKAP_DENDA_BULAN = models.CharField(
#         choices=ENUM_REKAP_DENDA_BULAN,
#     )
#     REKAP_DENDA_TUHAN = models.CharField(
#         choices=ENUM_REKAP_DENDA_TAHUN,
#     )
#     AKTIVASI_MEMBER = models.CharField(
#         choices=ENUM_AKTIVASI_MEMBER,
#     )
#     GANTI_PASSWORD = models.CharField(
#         choices=ENUM_GANTI_PASSWORD,
#     )
#     JUMLAH_PENGUNJUNG_HARI = models.CharField(
#         choices=ENUM_JUMLAH_PENGUNJUNG_HARI,
#     )
#     JUMLAH_PENGUNJUNG_BULAN = models.CharField(
#         choices=ENUM_JUMLAH_PENGUNJUNG_BULAN,
#     )
#     JUMLAH_PENGUNJUNG_TAHUN = models.CharField(
#         choices=ENUM_JUMLAH_PENGUNJUNG_TAHUN,
#     )
#     PENDAPATAN_REGISTRASI_HARI = models.CharField(
#         choices=ENUM_PENDAPATAN_REGISTRASI_HARI,
#     )
#     PENDAPATAN_REGISTRASI_BULAN = models.CharField(
#         choices=ENUM_PENDAPATAN_REGISTRASI_BULAN,
#     )
#     PENDAPATAN_REGISTRASI_TAHUN = models.CharField(
#         choices=ENUM_PENDAPATAN_REGISTRASI_TAHUN,
#     )
#     TOTAL_MAIL = models.CharField(
#         choices=ENUM_TOTAL_MAIL,
#     )
#     TOTAL_MAIL_WAKTU = models.CharField(
#         choices=ENUM_TOTAL_MAIL_WAKTU,
#     )
#     RESPONSE_MAILBOX = models.CharField(
#         choices=ENUM_RESPONSE_MAILBOX,
#     )
#     INTERN_MAIL = models.CharField(
#         choices=ENUM_INTERN_MAIL,
#     )
#     TOTAL_WARINTEK = models.CharField(
#         choices=ENUM_TOTAL_WARINTEK,
#     )
#     ENTRY_WARINTEK = models.CharField(
#         choices=ENUM_ENTRY_WARINTEK,
#     )
#     TOTAL_E_JOURNAL = models.CharField(
#         choices=ENUM_TOTAL_E_JOURNAL,
#     )
#     ENTRY_INDEX_JOURNAL = models.CharField(
#         choices=ENUM_ENTRY_INDEX_JOURNAL,
#     )
#     ENTRY_E_JOURNAL = models.CharField(
#         choices=ENUM_ENTRY_E_JOURNAL,
#     )
#     TOTAL_E_BOOK = models.CharField(
#         choices=ENUM_TOTAL_E_BOOK,
#     )
#     ENTRY_E_BOOK = models.CharField(
#         choices=ENUM_ENTRY_E_BOOK,
#     )
#     STATISTIK_WEB = models.CharField(
#         choices=ENUM_STATISTIK_WEB,
#     )
#     E_BOOK = models.CharField(
#         choices=ENUM_E_BOOK,
#     )
#     LIHAT_PINJAMAN = models.CharField(
#         choices=ENUM_LIHAT_PINJAMAN,
#     )
#     TAGIHAN = models.CharField(
#         choices=ENUM_TAGIHAN,
#     )
#     MAILBOX = models.CharField(
#         choices=ENUM_MAILBOX,
#     )
#     BERITA = models.CharField(
#         choices=ENUM_BERITA,
#     )

# class Anggota_Aktif (models.Model):
#     JUMLAH = models.CharField()
#     JENIS_KELAMIN = models.CharField(
#         choices=ENUM_JENIS_KELAMIN,
#     )
#     JENIS_ANGGOTA = models.CharField()
#     KELURAHAN = models.CharField()
#     KECAMATAN = models.BigIntegerField()

# class Peminjaman_Jenis_Koleksi (models.Model):
#     JUMLAH = models.BigIntegerField()
#     TANGGAL = models.DateField()
#     JENIS_KOLEKSI = models.CharField(
#         choices=ENUM_JENIS_KOLEKSI,
#     )
#     KELAS = models.CharField()

# class Peminjaman (models.Model):
#     REGISTER = models.CharField()
#     OUT_DATE = models.DateField()

# class BookMainGrouping (models.Model):
#     CLASS = models.CharField()
#     LANGUAGE = models.CharField()
#     YEAR_PUB = models.DateField()
#     JUMLAH = models.CharField()

# class Pengembalian_Jenis_Koleksi (models.Model):
#     JUMLAH = models.BigIntegerField()
#     TANGGAL = models.DateField()
#     JENIS_KOLEKSI = models.CharField(
#         choices=ENUM_JENIS_KOLEKSI
#     )

# class BookRptTitleByStudyProgram (models.Model):
#     REGISTER = models.CharField()
#     DEWEY_NO = models.CharField()
#     STUDY_PROGRAM = models.CharField()

# class BookRptExemplarByStudyProgram (models.Model):
#     REGISTER = models.CharField()
#     GROUP_NO = models.CharField()
#     DEWEY_NO = models.CharField()
#     COPY_NO = models.BigIntegerField()
#     STUDY_PROGRAM = models.CharField()

# class BookRptAddCopyByStudyProgram (models.Model):
#     REGISTER = models.CharField()
#     GROUP_NO = models.CharField()
#     DEWEY_NO = models.CharField()
#     COPY_NO = models.BigIntegerField()
#     STUDY_PROGRAM = models.CharField()

# class CirculationFine (models.Model):
#     TOTAL = models.CharField()
#     OPERATOR_NAME = models.CharField()
#     IN_DATE = models.DateField()
#     HOUR_RANGE = models.BigIntegerField()

# class CirculationMaxLoan (models.Model):
#     MEMBER_ID = models.CharField()
#     NAME = models.CharField()
#     REGISTER = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     MEMBER_TYPE = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FULL_NAME = models.CharField()
#     FACULTY_ID = models.CharField()
#     DEWEY_NO = models.CharField()
#     OUT_DATE = models.DateField()
#     OPERATOR_CODE = models.CharField()

# class CirculationNeverLate (models.Model):
#     MEMBER_ID = models.CharField()
#     NAME = models.CharField()
#     REGISTER = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     MEMBER_TYPE = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FULL_NAME = models.CharField()
#     FACULTY_ID = models.BigIntegerField()
#     FINE_ASSESSED = models.CharField()
#     IN_DATE = models.DateField()

# class CirculationMaxVisit (models.Model):
#     STUDENT_ID = models.CharField()
#     MEMBER_ID = models.CharField()
#     VISIT_DATE = models.DateField()
#     NAME = models.CharField()
#     ADDRESS = models.CharField()
#     FULL_NAME = models.CharField()

# class CirculationLoanByFaculty (models.Model):
#     FACULTY_ID = models.CharField()
#     DEWEY_NO = models.CharField()
#     OUT_DATE = models.DateField()
#     TOTAL = models.BigIntegerField()

# class CirculationStatCheckin (models.Model):
#     REGISTER = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     MEMBER_TYPE = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FACULTY_ID = models.CharField()
#     DEWEY_NO = models.CharField()
#     IN_DATE = models.DateField()
#     IN_OPERATOR_CODE = models.CharField()
#     OPERATOR_NAME = models.CharField()

# class CrossTab (models.Model):
#     CLASS = models.CharField()
#     ENG90_95 = models.CharField()
#     IND90_95 = models.CharField()
#     OTH90_95 = models.CharField()
#     ENG96_00 = models.CharField()
#     IND96_00 = models.CharField()
#     OTH96_00 = models.CharField()
#     TOTAL = models.CharField()

# class CirculationStatFine (models.Model):
#     FINE_PAID = models.CharField()
#     FINE_WAIVED = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     MEMBER_TYPE = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FACULTY_ID = models.CharField()
#     IN_DATE = models.DateField()
#     IN_OPERATOR_CODE = models.CharField()

# class CirculationStatLoan (models.Model):
#     REGISTER = models.CharField()
#     STRATA_CODE = models.CharField(
#         choices=ENUM_STRATA_CODE,
#     )
#     MEMBER_TYPE = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FACULTY_ID = models.CharField()
#     DEWEY_NO = models.CharField()
#     OUT_DATE = models.DateField()
#     OPERATOR_CODE = models.CharField()

# class GroupNoCopy (models.Model):
#     CLASS = models.CharField()
#     LANGUAGE = models.CharField()
#     YEAR_PUB = models.CharField()
#     JUMLAH = models.CharField()

# class DailyFinePaid (models.Model):
#     JUMLAH = models.CharField()
#     OPERATOR_NAME = models.CharField()

# class GroupNoTitle (models.Model):
#     CLASS = models.CharField()
#     LANGUAGE = models.CharField()
#     YEAR_PUB = models.CharField()
#     JUMLAH = models.CharField()

# class MemberCard (models.Model):
#     MEMBER_ID = models.CharField()
#     NAME = models.CharField()
#     STUDENT_ID = models.CharField()
#     ADDRESS = models.CharField()
#     REGISTERED_DATE = models.DateField()
#     ENTRY_DATE = models.DateField()
#     VALID_UNTIL = models.DateField()
#     FULL_NAME = models.CharField()
#     FACULTY = models.CharField()

# class MemberGroupVisitByFHour (models.Model):
#     TOTAL = models.CharField()
#     FACULTY_ID = models.CharField()
#     VISIT_DATE = models.DateField()
#     HOUR_RANGE = models.CharField()

# class MemberGroupVisitByFacility (models.Model):
#     TOTAL = models.CharField()
#     FACULTY_ID = models.CharField()
#     VISIT_DATE = models.DateField()
#     TIME_PERIOD = models.CharField()

# class MemberStatVisitByFHour (models.Model):
#     MEMBER_ID = models.CharField()
#     FACULTY_ID = models.CharField()
#     VISIT_DATE = models.DateField()
#     HOUR_RANGE = models.CharField()

# class OLapCirculationCheckIn (models.Model):
#     TANGGAL_KEMBALI = models.DateField()
#     JENIS_ANGGOTA = models.CharField()
#     JENIS_KELAMIN = models.CharField(
#         choices=ENUM_JENIS_KELAMIN,
#     )
#     JURUSAN = models.CharField()
#     KELAS = models.CharField()
#     KLASIFIKASI = models.CharField()
#     NAMA_OPERATOR = models.CharField()
#     JUMLAH_ESKEMPLAR = models. BigIntegerField()

# class OLapBookCopyProduction (models.Model):
#     NAMA_OPERATOR = models.CharField()
#     KELAS = models.CharField()
#     DATA_ENTRY = models.DateField()
#     BAHASA = models.CharField()
#     TAHUN_TERBIT = models.CharField()
#     JENIS_KOLEKSI = models.CharField(
#         choices=ENUM_JENIS_KOLEKSI,
#     )
#     JUMLAH_KOPI = models.BigIntegerField()

# class OLapBookTitleProduction(models.Model):
#     NAMA_OPERATOR = models.CharField()
#     KELAS = models.CharField()
#     TANGGAL_ENTRY = models.DateField()
#     BAHASA = models.CharField()
#     TAHUN_TERBIT = models.CharField()
#     JENIS_KOLEKSI = models.CharField()
#     JUMLAH_JUDUL = models.BigIntegerField()

# class OLapCirculationFine (models.Model):
#     TANGGAL_KEMBALI = models.DateField()
#     JENIS_ANGGOTA = models.CharField()
#     JENIS_KELAMIN = models.CharField(
#         choices=ENUM_JENIS_KELAMIN,
#     )
#     JURUSAN = models.CharField()
#     KELAS = models.CharField()
#     NAMA_OPERATOR = models.CharField()
#     DENDA_DIBAYAR = models.CharField()
#     KEKURANGAN_DENDA = models.CharField()

# class OLapLoan (models.Model):
#     TANGGAL_PINJAM = models.DateField()
#     JENIS_ANGGOTA = models.CharField()
#     JENIS_KELAMIN = models.CharField()
#     JURUSAN = models.CharField()
#     KELAS = models.CharField()
#     KLASIFIKASI = models.CharField()
#     NAMA_OPERATOR = models.CharField()
#     JUMLAH_EKSEMPLAR = models.CharField()

# class OLapMemberVisit (models.Model):
#     KELAS = models.CharField()
#     JURUSAN = models.CharField()
#     JENIS_ANGGOTA = models.CharField()
#     JENIS_KELAMIN = models.CharField(
#         choices=ENUM_JENIS_KELAMIN,
#     )
#     TANGGAL_KUNJUNGAN = models.DateField()
#     JUMLAH_PENGUNJUNG = models.BigIntegerField()

# class OLapMemberActive (models.Model):
#     JUMLAH = models.CharField()
#     JENIS_KELAMIN = models.CharField(
#         choices=ENUM_JENIS_KELAMIN,
#     )
#     JENIS_ANGGOTA = models.CharField()
#     JURUSAN = models.CharField()
#     KELAS = models.BigIntegerField()

# class OLapPengembalianJenisKoleksi (models.Model):
#     JUMLAH = models.CharField()
#     TANGGAL = models.DateField()
#     JENIS_KOLEKSI = models.CharField(
#         choices=ENUM_JENIS_KOLEKSI,
#     )
#     KLASIFIKASI = models.CharField()

# class OLapPeminjamanJenisKoleksi (models.Model):
#     JUMLAH = models.CharField()
#     TANGGAL = models.DateField()
#     JENIS_KOLEKSI = models.CharField(
#         choices=ENUM_JENIS_KOLEKSI,
#     )
#     KLASIFIKASI = models.CharField()

# class OperatorName (models.Model):
#     REGISTER = models.CharField()
#     GROUP_NO = models.CharField()
#     STATUS = models.CharField(
#         choices=ENUM_STATUS,
#     )
#     TITLE = models.CharField()
#     DEWEY_NO = models.CharField()

# class StopN01TitleReference (models.Model):
#     REGISTER = models.CharField()
#     REG_STOPN = models.CharField()
#     YEAR_PUB = models.CharField()
#     DEWEY_NO = models.CharField()
#     TYPE_NAME = models.CharField()
#     STATUS = models.CharField()

# class StopN01DataReference (models.Model):
#     REGISTER = models.CharField()
#     STATUS = models.CharField()

# class StudyProgram (models.Model):
#     FACULTY_ID = models.CharField()
#     FACULTY = models.CharField()
#     PROGRAM_CODE = models.CharField()
#     FULL_NAME = models.CharField()

# class TotalOfTitle (models.Model):
#     CLASS = models.CharField()
#     ENG90_95 = models.CharField()
#     IND90_95 = models.CharField()
#     OTH90_95 = models.CharField()
#     ENG96_00 = models.CharField()
#     IND96_00 = models.CharField()
#     OTH96_00 = models.CharField()
#     TOTAL = models.CharField()

# class TransDataProgram (models.Model):
#     PROGRAM_CODE = models.CharField()
#     FULL_NAME = models.CharField()
#     FACULTY_ID = models.CharField()
#     FACULTY = models.CharField()

# class TestStopnCirculationDtsource (models.Model):
#     REGISTER = models.CharField()
#     PROCESS_DATE = models.DateField()
#     PROCESS_TYPE = models.CharField()

# class BookOriginalTitle (models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     REGISTER = models.CharField()
#     ORG_TITLE = models.CharField()

# class BookSeriesTitle (models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     REGISTER = models.CharField()
#     SERIES_TITLE = models.CharField()

# class BookSubject (models.Model):
#     ID = models.BigAutoField(primary_key=True)
#     REGISTER = models.CharField()
#     SUBJECT = models.CharField()

# class CirculationProblemType (models.Model):
#     PROBLEM_CODE = models.BigIntegerField(primary_key=True)
#     PROBLEM_NAME = models.CharField()

# class BookComment (models.Model):
#     NUMBER = models.BigIntegerField()
#     NAME = models.CharField()
#     ADDRESS = models.CharField()
#     FACULTY = models.CharField()
#     EMAIL = models.CharField()
#     SUBJECT = models.CharField()
#     TIMECOMMENT = models.TimeField()
#     ISRESPONSED = models.CharField(
#         choices = ENUM_ISRESPONSED
#     )
#     TIMERESPONSE = models.DateField()
#     COMMENT = models.CharField()
#     MEMBER_ID = models.CharField()

# class DaftarBerita (models.Model):
#     INDEK = models.BigIntegerField()
#     JUDUL = models.CharField()
#     BERITA = models.CharField()
#     TANGGAL = models.TimeField()
#     FILE_GAMBAR = models.FileField(max_length=255,blank=True, upload_to='Gambar_DaftarBerita')

# class DigitalLibrary (models.Model):
#     ID = models.CharField(primary_key=True)
#     TITLE = models.CharField()
#     CREATOR = models.CharField()
#     SOURCE = models.CharField()
#     DESCRIPTION_I = models.CharField()
#     FILE_NAME = models.FileField(max_length=255, upload_to='DigitalLibrary')
#     DATA_ENTRY = models.DateField()


# class InfoUmum (models.Model):
#     TATA_TERTIB = models.CharField()
#     JENIS_KOLEKSI = models.CharField()
#     RUANG_FUNGSI = models.CharField()
#     BENTUK_LAYANAN = models.CharField()
#     KEANGGOTAAN = models.CharField()
#     PROSEDUR_PEMINJAMAN = models.CharField()
#     JAM_LAYANAN = models.CharField()

# class NO_KTA (models.Model):
#     NO_ANGGOTA = models.CharField()

# class NO_REG (models.Model):
#     REGISTER = models.CharField()

# class StockOpname (models.Model):
#     REGISTER = models.CharField()
#     DATE_CHECK = models.TimeField()
#     OPERATOR_CODE = models.CharField()


# class BookAddCopy (models.Model):
#     REGISTER = models.CharField()
#     GROUP_NO = models.CharField()
#     PRINTING = models.BigIntegerField()
#     YEAR_PUB = models.CharField()
#     COPY_NO = models.BigIntegerField()
#     STATUS = models.CharField(
#         choices=ENUM_STATUS,
#     )
#     PRICE = models.CharField()
#     FUND_CODE = models.CharField()
#     LOCATION_CODE = models.CharField()
#     SPEC_LOCATION = models.CharField()
#     ACCEPT_DATE = models.DateField()
#     DATA_ENTRY = models.DateField()
#     OPERATOR_CODE = models.CharField()

# class BookNoteAdd (models.Model):
#     REGISTER = models.CharField()
#     NOTE = models.CharField()

# class BookNote (models.Model):
#     REGISTER = models.CharField()
#     NOTE = models.CharField()

# class BookLoanRule (models.Model):
#     TYPE_CODE = models.CharField()
#     IS_FIRST_COPY = models.CharField(
#         choices=ENUM_IS_FIRST_COPY,
#     )
#     DATE_LIMITED = models.DateField()
#     CLASS_LIMITED = models.CharField()
#     FINE = models.CharField()
#     ON_DATE = models.DateField()
#     MAIN_CLASS = models.CharField()
#     LOAN_PERIOD = models.DateField()

# class BookStatusLog (models.Model):
#     REGISTER = models.CharField()
#     FROM_STATUS = models.CharField()
#     TO_STATUS = models.CharField()
#     CHANGE_DATE = models.DateField()
#     OPERATOR_CODE = models.CharField()

# class CirculationProblemHistory (models.Model):
#     MEMBER_ID = models.CharField()
#     PROBLEM_CODE = models.CharField()
#     PROBLEM_DATE = models.DateField()
#     PROBLEM_DESCRIPTION = models.CharField()
#     PROBLEM_OPERATOR = models.CharField()
#     SOLVING_DATE = models.CharField()
#     SOLVING_OPERATOR = models.CharField()

# class CirculationProblem (models.Model):
#     MEMBER_ID = models.CharField()
#     PROBLEM_CODE = models.CharField()
#     PROBLEM_DATE = models.DateField()
#     PROBLEM_DESCRIPTION = models.CharField()
#     PROBLEM_OPERATOR = models.CharField()

# class Departement (models.Model):
#     DEPT_ID = models.CharField()
#     DEPT_NAME = models.CharField()
#     MEMBER_CODE = models.CharField()


# class LoanHistory (models.Model):
#     REGISTER = models.CharField()
#     MEMBER_ID = models.CharField()
#     OUT_DATE = models.DateField()
#     DUE_DATE = models.DateField()
#     FINE_ASSESSED = models.CharField()
#     FINE_PAID = models.CharField()
#     FINE_WAIVED = models.CharField()
#     IS_PRINTED = models.CharField(
#         choices=ENUM_IS_PRINTED,
#     )
#     NOTE = models.CharField()
#     OPERATOR_CODE = models.CharField()
#     IN_OPERATOR_CODE = models.CharField()

# class Holiday (models.Model) :
#     HOLY_DATE = models.DateField()
#     NOTE = models.CharField()

# class MemberMaxLoan (models.Model):
#     MEMBER_TYPE = models.CharField()
#     BK_TYPE_CODE = models.CharField()
#     COPY_ORDER = models.CharField()
#     MAX_LOAN = models.CharField()

# class MemberFreeOnLoanHistory (models.Model):
#     MEMBER_ID = models.CharField()
#     FREE_DATE = models.DateField()
#     EXPENSE = models.CharField()
#     OPERATOR_CODE = models.CharField()

# class MemberType (models.Model):
#     MEMBER_TYPE = models.CharField()
#     TYPE_NAME = models.CharField()
#     MAX_LOAN = models.BigIntegerField()

# class MemberVisitHistory(models.Model):
#     MEMBER_ID = models.CharField()
#     VISIT_DATE = models.DateField()

# class MemberRegisterHistory (models.Model):
#     MEMBER_ID = models.CharField()
#     REGISTERED_DATE = models.DateField()
#     VALID_UNTIL = models.DateField()
#     EXPENSE = models.CharField()
#     OPERATOR_CODE = models.CharField()

# class Member (models.Model):
#     MEMBER_ID = models.CharField()
#     STUDENT_ID = models.CharField()
#     MEMBER_TYPE = models.CharField()
#     REGISTERED_DATE = models.TimeField()
#     VALID_UNTIL = models.TimeField()
#     EXPENSE = models.CharField()
#     STATUS = models.CharField()
#     ENTRY_DATE = models.DateField()
#     OPERATOR_CODE = models.CharField()


# class BookCreator (models.Model):
#     REGISTER = models.ForeignKey(BookMain, on_delete=models.CASCADE)
#     FULL_NAME = models.CharField()
#     CREATOR_TYPE = models.CharField()
