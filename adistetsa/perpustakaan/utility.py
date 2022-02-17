from perpustakaan.models import KatalogBukuCopy

def check_buku_tersedia(list_buku):
    daftar_buku = list_buku.split(',')
    for data in daftar_buku:
        buku = KatalogBukuCopy.objects.get(pk=data)
        print(buku.STATUS)
        if (buku.STATUS != 'Sudah Dikembalikan'):
            return False

    return True