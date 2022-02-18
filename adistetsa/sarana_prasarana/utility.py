from .models import Ruangan, Sarana


def check_ruangan_tersedia(katalog_ruangan):
    for data in katalog_ruangan:
        ruangan = Ruangan.objects.get(pk=data)
        if (ruangan.STATUS != 'Selesai Dipinjam'):
            return False

    return True

def check_sarana_tersedia(katalog_sarana):
    for data in katalog_sarana:
        sarana = Sarana.objects.get(pk=data)
        if (sarana.STATUS != 'Sudah Dikembalikan'):
            return False

    return True