# Instalasi pertama kali

## Dependensi
Sebelum melakukan instalasi, pastikan aplikasi di bawah ini telah terinstall di komputer.
* Python 3+ https://www.python.org/downloads/
* VirtualEnv
    ```
    pip install virtualenv
    ```

## Clone Proyek
Buka cmd dan pindah ke direktori baru untuk menyimpan proyek.
```
cd D:\Proyek
git clone https://github.com/arrazy100/Adi_Stetsa_BackEnd.git
```

## Membuat Virtual Environment
Setelah melakukan clone proyek, jalankan perintah berikut pada cmd.
```
cd Adi_Stetsa_BackEnd
virtualenv nama_env
```

## Menggunakan Virtual Environment dan Instalasi Package
Windows
```
nama_env\Scripts\activate
pip install -r requirements.txt
```
Linux
```
source nama_env/bin/activate
pip install -r requirements.txt
```

## Run Server
Lakukan hal ini ketika melakukan run server pertama kali
```
cd adistetsa
python manage.py makemigrations
python manage.py migrate
python run_setup_dummy.py
```
Run server
```
python manage.py runserver
```

# Dokumentasi API
Proyek ini telah menyediakan dokumentasi API secara lengkap yang bisa dibuka ketika sedang menjalankan server
http://localhost:8000

Mencoba API langsung melalui Web
http://localhost:8000/swagger

API menggunakan JWT Token untuk Autentikasi, sehingga diperlukan Token dengan format "Bearer token_autentikasi" untuk mengakses API. Masukkan token ini pada Header atau pada Swagger jika melakukan percobaan API melalui Web.
