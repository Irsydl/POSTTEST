import os
os.system('cls')

menu = [
    ['nasi goreng', 'sate ayam', 'nasi ayam bakar'],
    ['teh tawar', 'teh manis', 'lemon tea']
    ]
print("Menu yang tersedia: \n")

for i in menu:
    for j in i:
        print(j)

print("\n=====================\n")

# Menambahkan menu dibelakang atau ditengah (Add)

def add_menu():
    quest = input("Tambahkan menu di belakang [0] atau di tengah [1]: ")
    user = input("\nMasukkan menu yang ingin ditambah: ")
    baris = int(input("\nBaris yang ingin ditambah 0/1: "))
    
    if quest == "0":
        menu[baris].append(user)
        print()
        print(menu)
    elif quest == "1":
        urutan = int(input("\nTambahkan menu setelah urutan berapa?: "))
        menu[baris].insert(urutan, user)
        print()
        print(menu)
    else:
        print("Error")

# Menghapus menu berdasarkan index yang dipilih (edit)

def del_menu():
    baris = int(input("Pilih baris 0/1:  "))
    user = int(input("Pilih index yang mau dihapus: "))
    menu1 = menu[0]
    menu2 = menu[1]
    
    if baris == 0:
        del menu1[user]
        print()
        print(menu)
    elif baris == 1:
        del menu2[user]
        print()
        print(menu)
    else:
        print("Error")

# Menghapus menu berdasarkan objek yang di input user (delete)

def del_menu2():
    baris = int(input("Pilih baris 0/1:  "))
    menu1 = menu[0]
    menu2 = menu[1]

    if baris == 0:
        print(menu1)
        user = input("Silahkan pilih yang ingin anda hapus: ")
        menu1.remove(user)
        print()
        print(menu)
    elif baris == 1:
        print(menu2)
        user = input("Silahkan pilih yang ingin anda hapus: ")
        menu2.remove(user)
        print()
        print(menu)
    else:
        print("Error")

# Mengganti value yang lama dengan value yang baru (edit)

def change_menu():
    baris = int(input("Pilih baris 0/1:  "))
    menu1 = menu[0]
    menu2 = menu[1]

    if baris == 0:
        print(menu1)
        user = int(input("Silahkan pilih index yang ingin anda ganti: "))
        quest = input("Value baru: ")
        menu1[user] = quest
        print()
        print(menu)
    if baris == 1:
        print(menu2)
        user = int(input("Silahkan pilih index yang ingin anda ganti: "))
        quest = input("Value baru: ")
        menu2[user] = quest
        print()
        print(menu)
    else:
        print("Error")


user = ""
while user != "quit":
    user = input("\nMenambah [1]\nMenghapus [2]\nMengganti [3]\n'quit' untuk keluar\nSilahkan masukkan pilihan anda: ")
    if user == "1":
        add_menu()
    elif user == "2":
        x = input("Pilih metode 1/2: ")
        if x == "1":
            del_menu()
        elif x == "2":
            del_menu2()
        else:
            print("Error")
    elif user == "3":
        change_menu()
    else:
        print("Error")
    y = input()
    