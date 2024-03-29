class dapur:
    def __init__(self) -> None:
        pass

    def makanan(self):
        print (60*('-'))
        print("Menu Makanan".center(60))
        print()
        print("1. Sate ayam     : Rp15.000")
        print("2. Soto          : Rp10.000")
        print("3. Bakso         : Rp12.000")
        print("4. Nasi Padang   : Rp20.000")
        print()

        print (60*('-'))
        makan = input("Silahkan tulis pesanan Anda ---> ('1', '2', '3', '4'): ")
        bayar_makan = 0
        if makan == '1':
            bayar_makan  += 15000
        elif makan == '2':
            bayar_makan  += 10000
        elif makan == '3':
            bayar_makan  += 12000
        elif makan == '4':
            bayar_makan  += 20000
        else:
            print("Pilihan tidak valid, mohon input sesuai prosedur, angka, bukan huruf.")

        return bayar_makan 



    def minuman(self):
        print (60*('-'))
        print("Menu Minuman".center(60))
        print()
        print("1. Es Teh    : Rp3.000")
        print("2. Es Jeruk  : Rp5.000")
        print("3. Es Kelapa : Rp5.000")
        print("4. Es Teler  : Rp10.000")
        print()

        print (60*('-'))
        minum = input("Silahkan tulis pesanan Anda ---> ('1', '2', '3', '4'): ")
        bayar_minum = 0
        if minum == '1':
            bayar_minum += 3000
        elif minum == '2':
            bayar_minum += 5000
        elif minum == '3':
            bayar_minum += 5000
        elif minum == '4':
            bayar_minum += 10000
        else:
            print("Pilihan tidak valid, mohon input sesuai prosedur, angka, bukan huruf.")  

        return bayar_minum
    
    def paket(self):
        print (60*('-'))
        print("Menu Paket".center(60))
        print()
        print('1. Nasi Goreng + Es teh  = Rp15.000')
        print('2. Mie Ayam + Es Teler   = Rp20.000')
        print()

        print (60*('-'))
        paket = input("Silahkan tulis pesanan Anda ---> ('1', '2'): ")
        bayar_paket = 0
        if paket == '1':
            bayar_paket += 15000
        elif paket == '2':
            bayar_paket += 20000
        else:
            print("Pilihan tidak valid, mohon input sesuai prosedur, angka, bukan huruf.")
        
        return bayar_paket

print(60*"=")
print("Ramadhan Kitchen".center(60))
print(60*"=")
print()

# Menu
print('1. Menu Makanan')
print('2. Menu Minuman')
print('3. Menu Paket')
print()

total_pembayaran = 0 

while True:

    # Input Pilihan
    menu = int(input('Masukkan Pilihan: '))
    print()

    masuk = dapur()
    if menu == 1:
        total_pembayaran += masuk.makanan()
        print()
        menu1 = input("Ingin melanjutkan pesanan? (ya/tidak): ")
        print()
        if menu1 != "ya":
            break
    elif menu == 2:
        total_pembayaran += masuk.minuman()
        print()
        menu1 = input("Ingin melanjutkan pesanan? (ya/tidak): ")
        print()
        if menu1 != "ya":
            break
    elif menu == 3:
        total_pembayaran += masuk.paket()
        print()
        menu1 = input("Ingin melanjutkan pesanan? (ya/tidak): ")
        print()
        if menu1 != "ya":
            break

print("Total Pembayaran Anda: Rp", total_pembayaran)
