print("========================================")
print("===============ATM FAMILY===============")
print("========================================")
print("                 WELCOME                ")
print()
print("1.Cek Saldo\n2.Isi Saldo\n3.Tarik Saldo\n4.Transfer Saldo")
saldo = 5_000_000
pilih = int(input("masukkan pilihan anda: "))
if pilih == 1:
    print()
    print("==========Cek Saldo==========")
    print("===Saldo anda Rp.",saldo,"====")
    print("=============================")    
    
elif pilih == 2:
    print()
    print("Isi saldo!")
    iL = int(input("Masukkan jumlah saldo (minimum 50.000) Rp."))
    if iL >= 50000 :
        print(iL+saldo)
    else:
        print("jumlah minimum tidak mencukupi!!!")
elif pilih == 3:
    print()
    print("penarikan saldo!")
    pS = int(input("Masukkan jumlah saldo: Rp."))
    if saldo >= pS:
        print("Saldo anda Rp.",saldo-pS)
        
    else:
        print("Saldo anda Kurang !!")
elif pilih == 4:
    print()
    print("masukkan No ATM!")
    nK = int(input(""))
    nominal = int(input("MAsukkan nominal :Rp."))
    if nominal <= saldo:
        print("Transaksi ke No rek", nK)
        print("senilai",nominal,"berhasil")
        print()
        print("saldo anda : Rp.",saldo-nominal)
    else:
        print()
        print("saldo tidak mencukupi !")
        print("silahkan lakukan pengisian saldo\nsebelum melakukan transaksi lagi")
else:
    print()
    print("pilihan tidak di temukan!")
    
    