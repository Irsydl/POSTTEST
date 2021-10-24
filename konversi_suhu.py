"""""

Rumus mengubah suhu :
Fahrenheit ke Celsius : (Fahrenheit - 32) / 1,8
Kelvin ke Celsius : Kelvin - 273,15
Reamur ke Celsius : Reamur / 0,8 atau 8/10

"""""

def fahrenheit():
    f = float(input("Nilai fahrenheit : "))
    ftoc = (f - 32) * (5/9)
    print("Nilai Celsius : ",ftoc)

def kelvin():
    k = float(input("Nilai kelvin : "))
    ktoc = k - 273,15
    print("Nilai Celsius : ",ktoc)

def reamur():
    r = float(input("Nilai reamur : "))
    rtoc = r / (8/10)
    print("Nilai Celsius : ",rtoc)

def menu():
    print("[1] Fahrenheit ke Celcius")
    print("[2] Kelvin ke Celcius")
    print("[3] Reamur ke Celcius")
    print("[0] Keluar dari program.")

menu()
pilihan = int(input("Masukkan pilihan: "))

while pilihan != 0:
    if pilihan == 1:
        fahrenheit()
    elif pilihan == 2:
        kelvin()
    elif pilihan == 3:
        reamur()
    else:
        print('"Pilihan tidak valid"')
    
    print()
    menu()
    pilihan = int(input("Masukkan pilihan: "))

print('"Telah keluar dari program"')

