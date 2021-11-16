import os
os.system("cls")

print("=== Menu Pesanan ===\n")

print("= Makanan =")
print("Sate Ayam : 10 Ribu\nNasi Goreng : 12 Ribu\nNasi Ayam Bakar : 18 Ribu\nGule Daging Kambing : 30 Ribu\nKebab : 8 Ribu")
print("\n= Minuman =")
print("Teh Tawar : 2 Ribu\nTeh Manis : 5 Ribu\nLemon Tea : 8 Ribu\nEs Kelapa : 10 Ribu\nJus Semangka : 15 Ribu")

print("\n=== DISKON ===")
print("Diskon setiap Pembelian 3 Minuman sebesar 10%\nDiskon setiap Pembelian 2 Makanan sebesar 5%\nDiskon setiap pembayaran melalui E-money sebesar 5%\nDiskon saat weekend sebesar 5%\nDiskon saat weekdays sebesar 10%\n")

makanan = {
    'sate ayam': 10,
    'nasi goreng': 12,
    'nasi ayam bakar': 18,
    'gule daging kambing': 30,
    'kebab': 8,
}

minuman = {
    'teh tawar': 2,
    'teh manis': 5,
    'lemon tea': 8,
    'es kelapa': 10,
    'jus semangka': 15
}

keranjang1 = []
keranjang2 = []
total = []
weekdays = ['senin', 'selasa', 'rabu', 'kamis', 'jumat']
weekend = ['sabtu', 'minggu']

def belanja_makan():
    print("Ketik 'quit' untuk keluar")
    user = input("Makanan yang dibeli: ").lower()
    while user != 'quit':
        if user in makanan:
            keranjang1.append(user)
            user = input("\nAda lagi?: ").lower()
        else:
            user = input("\nItem tidak ada, Masukkan item: ")


def belanja_minum():
    print("\nKetik 'quit' untuk keluar")
    user = input("Minuman yang dibeli: ").lower()
    while user != 'quit':
        if user in minuman:
            keranjang2.append(user)
            user = input("\nAda lagi?: ").lower()
        else:
            user = input("\nItem tidak ada, Masukkan item: ")

belanja_makan()
belanja_minum()

print("\nMakanan yang dibeli: ", keranjang1)
print("Minuman yang dibeli: ", keranjang2)

for i in keranjang1:
    total.append(makanan[i])

for j in keranjang2:
    total.append(minuman[j])

harga = 0

for i in total:
    harga += i

def diskon_makan():
    global dis_makan
    if len(keranjang1) >= 2:
        dis_makan = 5/100
    else:
        dis_makan = 0

def diskon_minum():
    global dis_minum
    if len(keranjang2) >= 3:
        dis_minum = 10/100
    else:
        dis_minum = 0

def diskon_emoney():
    global dis_emoney
    print("===============================")
    user = input("\nApakah pembelian menggunakan e-money? y/n: ").lower()
    print("\n===============================")
    if user == 'y'.lower():
        dis_emoney = 5/100
    elif user == 'n'.lower():
        dis_emoney = 0
    else:
        print("Input tidak valid")
        diskon_emoney()

def diskon_hari(hari):
    global dis_hari
    if hari in weekend:
        dis_hari = 5/100
    elif hari in weekdays:
        dis_hari = 10/100
    else:
        print("Input tidak valid")
        diskon_hari()

diskon_makan()
diskon_minum()
diskon_emoney()
diskon_hari("rabu")

diskontotal = dis_makan + dis_minum + dis_emoney + dis_hari
hargatotal = harga * diskontotal
harga -= hargatotal

print("Total diskon: ", diskontotal, "%")
print("=================")
print("\nTotal pesanan anda: ",harga * 1000)
print("\n=================")

print("Program Selesai")
