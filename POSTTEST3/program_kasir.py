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
    user = input("Makanan yang dibeli: ").lower()
    while user != 'quit':
        if user in makanan:
            keranjang1.append(user)
            user = input("Ketik 'quit' untuk keluar\nAda lagi?: ").lower()
        else:
            user = input("ketik 'quit' untuk keluar\nItem tidak ada, Masukkan item: ")


def belanja_minum():
    user = input("\nMinuman yang dibeli: ").lower()
    while user != 'quit':
        if user in minuman:
            keranjang2.append(user)
            user = input("Ketik 'quit' untuk keluar\nAda lagi?: ").lower()
        else:
            user = input("ketik 'quit' untuk keluar\nItem tidak ada, Masukkan item: ")
            
belanja_makan()
belanja_minum()

print("Makanan yang dibeli: ", keranjang1)
print("Minuman yang dibeli: ", keranjang2)

for i in keranjang1:
    total.append(makanan[i])

for j in keranjang2:
    total.append(minuman[j])

harga = 0

for totals in total:
    harga += totals

harga_total = harga * 1000.0

if len(keranjang1) >= 2:
    diskon1 = harga_total * 5/100
else:
    diskon1 = 0
if len(keranjang2) >= 3:
    diskon2 = harga_total * 10/100
else:
    diskon2 = 0

emoney = input("\nPembayaran melalui E-Money? [Y] [N]: ").lower()
if emoney == 'y'.lower():
    diskon3 = harga_total * 5/100
else:
    diskon3 = 0
hari = input("Masukkan hari: ").lower()
if hari.lower() in weekend:
    diskon4 = harga_total * 5/100
elif hari.lower() in weekdays:
    diskon4 = harga_total * 10/100

diskon = diskon1 + diskon2 + diskon3 + diskon4
print()
print("Total Harga yang dibayar: Rp.", harga_total - diskon)
