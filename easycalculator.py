def tambah(x, y):
    return x + y
    
def kurang(x, y):
    return x - y
    
def kali(x, y):
    return x * y
    
def bagi(x, y):
    return x / y
    
    
print("ZyraXen mathematics tools (BETA)")
print("Bahasa Indonesia")
print('\n')
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
    
while True:
        choice = input("Pilih operasi(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            no1 = float(input("Masukkan angka pertama: "))
            no2 = float(input("Masukkan angka kedua: "))
            if choice == "1":
                print(no1, '+', no2, '=', tambah(no1, no2))
            elif choice == "2":
                print(no1, '-', no2, '=', kurang(no1, no2))
            elif choice == "3":
                print(no1, '*', no2, '=', kali(no1, no2))
            elif choice == "4":
                print(no1, '/', no2, '=', bagi(no1, no2))
                
            lanjut = input('Ulangi? (y/g): ')
                
            if lanjut == "g" or lanjut == "G":
                    break