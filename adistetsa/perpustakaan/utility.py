from perpustakaan.models import KatalogBukuCopy


def check_buku_tersedia(list_buku):
    for data in list_buku:
        buku = KatalogBukuCopy.objects.get(pk=data)
        print(buku.STATUS)
        if (buku.STATUS != 'Sudah Dikembalikan'):
            return False

    return True