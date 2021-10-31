def data_mahasiswa():
    # Menerima input data mahasiswa dari pengguna / user
    nama = input("Nama mahasiswa: ")
    nim = int(input("NIM: "))
    prodi = input("Prodi: ")
    agama = input("Agama: ")
    tinggi = float(input("Tinggi: "))
    
    # Menyimpan hasil input ke dalam list
    list1 = [nama, nim, prodi, agama, tinggi]

    # Data yang disimpan di list1 dipanggil ke dalam dictionary
    student_dicti = {
        'Nama': list1[0],
        'Nim': list1[1],
        'Prodi': list1[2],
        'Agama': list1[3],
        'Tinggi': list1[4]
    }
    
    # Output dictionary
    print(student_dicti)


def menu():
    # Membuat menu tampilan
    print("[Y] : Masuk ke program ")
    print("[N] : Keluar dari program ")
    
    # Menerima input dari user dan membuat input menjadi huruf kecil
    user = input("Masukkan Pilihan: ")
    user = user.lower()
    
    # Loop ketika input user tidak sama dengan "n" dan menjalankan fungsi data mahasiswa ketika input user sama dengan "y"
    # Program selesai atau keluar ketika user menginput "n"
    while user != "n":
        if user == "y":
            data_mahasiswa()
        else:
            print('"Tidak valid"')
        
        print()
        print("[Y] : Masuk ke program ")
        print("[N] : Keluar dari program ")

        user = input("Masukkan Pilihan: ")
        user = user.lower()

menu()
print('"Program selesai."')

"""

LINK REPO GITHUB:
https://github.com/Irsydl/POSTTEST2.git

"""
