def hitung_hapus():
    kalimat = input("Masukkan Kalimat: ")
    start = int(input("Index Start: "))+ 1
    stop = int(input("Index Stop: "))+ 1
    x = stop - start + 1
    hasil = (x/len(kalimat))*100
    print(hasil)
    if hasil < 0:
        return 0.0
    else:
        return hasil
hitung_hapus()