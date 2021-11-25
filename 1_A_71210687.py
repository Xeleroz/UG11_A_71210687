def calculator():
    judul = ("======== Calculator sederhana ========\n")
    menu1 = ("1. Pertambahan\n")
    menu2 = ("2. Pengurangan\n")
    menu3 = ("3. Perkalian\n")
    menu4 = ("4. Pembagian\n")
    menu5 = ("5. Pangkatan")
    print(judul, menu1, menu2, menu3, menu4, menu5)
    return(judul + menu1 + menu2 + menu3 + menu4 + menu5)
def tambah():
    a = int(input("Masukkan bilangan 1: "))
    b = int(input("Masukkan bilangan 2: "))
    hasil = a + b
    print("Hasilnya:",hasil)
    return hasil
def kurang():
    a = int(input("Masukkan bilangan 1: "))
    b = int(input("Masukkan bilangan 2: "))
    hasil = a - b
    print("Hasilnya:",hasil)
    return hasil
def kali():
    a = int(input("Masukkan bilangan 1: "))
    b = int(input("Masukkan bilangan 2: "))
    hasil = a * b
    print("Hasilnya:",hasil)
    return hasil
def bagi():
    a = int(input("Masukkan bilangan 1: "))
    b = int(input("Masukkan bilangan 2: "))
    hasil = a / b
    print("Hasilnya:",hasil)
    return hasil
def pangkat():
    a = int(input("Masukkan bilangan 1: "))
    b = int(input("Masukkan bilangan 2: "))
    hasil = a**b
    print("Hasilnya:",hasil)
    return hasil
calculator()
x = int(input("Masukkan pilihan: "))
if x == 1:
    tambah()
elif x == 2:
    kurang()
elif x == 3:
    kali()
elif x == 4:
    bagi()
elif x == 5:
    pangkat()
else:
    i = int(input("Masukkan bilangan 1: "))
    o = int(input("Masukkan bilangan 2: "))
    print("Hasilnya: Maaf input operasi antara 1-5")