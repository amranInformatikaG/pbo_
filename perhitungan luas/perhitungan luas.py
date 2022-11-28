print("NAMA : Muhammad.Amran")
print("NIM : D0221102")
print("1.Menghitung persegi\n2.Menghitung lingkaran\n3.Menghitung segitiga")
print("")
pilih = int(input("Masukkan pilihan: "))
if pilih == 1:
    
    print("MENGHITUNG LUAS & KELILING PERSEGI")
    s = float(input("\nMasukan Panjang Sisi: "))
    Lp = s**2
    print("\nLuas Persegi \t\t:",Lp) 
elif pilih == 2:
    
    print("")
    phi = 3.14
    r = float(input("Masukkan panjang jari-jari lingkaran: "))
    luas = phi*r*r
    print("Luas lingkaran adalah : "+ str(luas))
elif pilih == 3:    
    print("PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA")
    a = float(input("\nMasukan Alas  : "))
    t = float(input("Masukan Tinggi: "))
    luas = 0.5*a*t
    print("\nLuas Segitiga  = %0.2f" % luas)
    
else:
    print("pilihan tidak terdeteksi")