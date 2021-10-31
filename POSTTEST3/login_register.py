# Akun yang sudah disiapkan
thisdict = {
    'admin': 'admin123',
}

# Fungsi yang dijalankan jika user ingin menggunakan akun yang sudah disiapkan atau akun yang sudah di register
def olduser():
    i = 3
    while i >= 1:
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        if thisdict.get(username) == password:
            print("Login Berhasil!")
            break
        else:
            i -= 1
            print("Login gagal, sisa percobaan:", i)

# Fungsi yang dijalankan jika user belum memiliki akun, dan akan me register akun baru untuk digunakan
def newuser():
    username = input("Username: ")
    password = input("Password: ")
    thisdict.update({username : password})
    choices = input("Sudah selesai? y/n: ")
    if choices == 'y':
        olduser()
    elif choices == 'n':
        newuser()
    else:
        print('Error')

# Mendapatkan input dari user
user = input("Apakah anda memiliki akun? y/n: ").lower()

# Jika input dari user adalah 'y' maka jalankan fungsi olduser()
if user == 'y'.lower():
    olduser()
# Jika input dari user adalah 'n' maka jalankan fungsi newuser()
elif user == 'n'.lower():
    newuser()
