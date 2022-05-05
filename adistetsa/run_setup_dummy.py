from subprocess import call

print('Data Profil\n')
call(["python", "manage.py", "setup_dummy_dataprofil"])

print('\nKustom Autentikasi\n')
call(["python", "manage.py", "setup_dummy_pre_kustom_autentikasi"])
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