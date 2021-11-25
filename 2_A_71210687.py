def ambil_tengah(a,b = None):
    if b == None:
        count = (round(len(a)/2))
        return (a[count])
    else:
        count = (round(len(a)/2))
        return (a[count+b-1])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))