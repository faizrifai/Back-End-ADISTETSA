from .models import Ruangan, Sarana


def check_ruangan_tersedia(ruangan):
    obj = Ruangan.objects.get(pk=ruangan)
    print(obj.STATUS)
    if obj.STATUS != "Sudah Dikembalikan":
        return False

    return True


def check_sarana_tersedia(katalog_sarana):
    data_sarana = katalog_sarana.split(",")
    for data in data_sarana:
        sarana = Sarana.objects.get(pk=data)
        if sarana.STATUS != "Sudah Dikembalikan":
            return False

    return True
