from subprocess import call

call(["python", "manage.py", "setup_dummy_pre_kustom_autentikasi"])

print('Data Profil\n')
call(["python", "manage.py", "setup_dummy_dataprofil"])

print('\nKustom Autentikasi\n')
call(["python", "manage.py", "setup_dummy_kustom_autentikasi"])

print('\nKurikulum\n')
call(["python", "manage.py", "setup_dummy_pre_kurikulum"])
call(["python", "manage.py", "setup_dummy_kurikulum"])

print('\nAdiwiyata\n')
call(["python", "manage.py", "setup_dummy_adiwiyata"])

print('\nBK\n')
call(["python", "manage.py", "setup_dummy_pre_bk"])
call(["python", "manage.py", "setup_dummy_bk"])

print('\nHumas\n')
call(["python", "manage.py", "setup_dummy_humas"])

print('\nKesiswaan\n')
call(["python", "manage.py", "setup_dummy_kesiswaan"])

print('\nKeuangan\n')
call(["python", "manage.py", "setup_dummy_keuangan"])

print('\nSarana Prasarana\n')
call(["python", "manage.py", "setup_dummy_pre_sarana_prasarana"])
call(["python", "manage.py", "setup_dummy_sarana_prasarana"])

print('\nUnit Penjamin Mutu\n')
call(["python", "manage.py", "setup_dummy_upm"])

# print('\nPerpustakaan\n')
# call(["python", "manage.py", "setup_dummy_perpustakaan"])

print('\nTata Usaha\n')
call(["python", "manage.py", "setup_dummy_tata_usaha"])