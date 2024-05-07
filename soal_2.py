def is_kabisat(Tahun):
    if (Tahun % 400 == 0) or (Tahun % 4 == 0 and Tahun % 100 != 0):
        return True
    else:
        return False

Tahun = int(input("Masukkan tahun: "))
if is_kabisat(Tahun):
    print(Tahun, "adalah tahun kabisat.")
else:
    print(Tahun, "bukan tahun kabisat.")