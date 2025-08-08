import os
user1=""
directorti='oop/Perpus'
Alluser=[]
use=[]
class user:
    def __init__(self,nama,password):
        self.nama=nama
        self.password=password
        self.status="tidak"
        self.daftar_User=[]
        # self.bukuPinjaman=""
    def info(self):
        print('='*30)
        print(f'|{"Nama Pengguna:"}{self.nama:<14}|')
        print(f'|{"Password Pengguna:"}{self.password:<10}|')
        print(f'|{"Pinjaman Buku:":<28}|\n|{self.status.judul:<28}|')
        print(f'|{"back":>28}|')
        print('='*30)
    def tambahUser(self,buku):
        self.daftar_User.append(buku)
    def TampikanUser(self):
        pass



        
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print('<'*30)
        print(f"|Judul: {self.judul:<21}|")
        print(f"|Penulis: {self.penulis:<19}|")
        print(f"|Tahun Terbit: {self.tahun_terbit:<14}|")
        print('>'*30)

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def pinjaman_buku(self, buku):
        self.daftar_buku.pop(buku)

    def tampilkan_daftar_buku(self):
        if not self.daftar_buku:
            print("Perpustakaan kosong.")
        else:
            print(f"|Daftar Buku:{'|':>17}")
            print('='*30)
            for i in range(len(self.daftar_buku)):
                print(f'|Buku {i+1:<23}|')
                self.daftar_buku[i].tampilkan_info()
                print('>'*30)
            # for buku in self.daftar_buku:
            #     buku.tampilkan_info()
            #     print('='*30)

def startData():
    try:
        with open(f'{directorti}/Profuser.txt','r') as file:
            for fb in file:
                Alluser.append(fb.strip().split(','))
    except FileNotFoundError:
        with open(f'{directorti}/Profuser.txt','w') as file:
            pass
def signup():
    os.system('cls')
    print('='*30)
    print(f'|{"Perpustakaan Handcode":^28}|')
    print('='*30)
    nm = input('|Nama:')
    pswd = input('|Password:')
    conpswd = input('|Confirm Password:')
    if conpswd==pswd:
        input('Success')
        os.system('cls')
        user1=user(nm,pswd,'None')
        use.append(nm)
        use.append(pswd)
        use.append('None')
        with open(f'{directorti}/Profuser.txt','a') as file:
            sementara=[]
            for fb in use:
                sementara.append(fb)
            sentence = ",".join(sementara)
            file.write(sentence)
        return user1
    else:
        input('Password Tidak Cocok')
        signup()
         

def Profile(nama):#profile
    os.system('cls')
    print('='*30)
    print(f'|{"Perpustakaan Handcode":^28}|')
    nama.info()
    input('Enter to return!')
    MainMenu()

def MainMenu():
    print('='*30)
    print(f'|{"Perpustakaan Handcode":^28}|')
    print('='*30)
    print(f'|{"1.CariBuku":^28}|\n|{"2.PinjamBuku":^28}|\n|{"3.ProfilPengguna":^28}|\n|{"4.pengembalianBuku":^28}|\n|{"5.keluar":^28}|')
    print('='*30)
def pinjembuku(user1):
    print('='*30)
    print(f'|{"Pilihan Buku":^28}|')
    print('='*30)
    perpustakaan.tampilkan_daftar_buku()
    Choice=int(input('Pinjem Buku nomor: '))
    print(perpustakaan.daftar_buku[Choice-1].judul)
    user1.status=perpustakaan.daftar_buku[Choice-1]
    perpustakaan.pinjaman_buku(Choice-1)
    Profile(user1)
buku1 = Buku("Hally Porret", "J.K. bowling", 2025)
buku2 = Buku("Lord Of The bings", "J.P.R. Toikien", 1800)
buku3 = Buku("Sorny The turtle", "wart skibedi", 1958)
buku4 = Buku("Kings And The Lord", "allebngi", 1958)
perpustakaan = Perpustakaan()
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)
perpustakaan.tambah_buku(buku4)
startData()
for i in range(len(Alluser)):
    x=user(Alluser[i][0],Alluser[i][1],Alluser[i][2])
    x.info()
    print(i)
    print(Alluser[i])
    user.tambahUser(x)
os.system('cls')
print('='*30)
print(f'|{"Perpustakaan Handcode":^28}|')
print('='*30)
print(f"|{'1.Sign Up':^28}|\n|{'2.Sign in':^28}|")
print('='*30)
print('Welcome To Handcode Perpustakaan.')
Choice=input('Enter your Pilihan: ')
if Choice=='1'or Choice=='Sign Up':
    user1=signup()
elif Choice=='2'or Choice=='Sign in':
    Name=input('Masukan Nama: ')
    for i in range(len(user.daftar_User)):
        if Name in user.daftar_User[i].nama:
            pasword=input('Masukan Password: ')
            if pasword==user.daftar_User[i].password:
                MainMenu()
            else:
                input('Password Salah')
        else:
            input('User Tidak Ditemukan')



# perpustakaan.tampilkan_daftar_buku()
MainMenu()
Choice=input('Enter your Pilihan: ')
if Choice=='3'or Choice=='ProfilPengguna':
    Profile(user1)
elif Choice=='2'or Choice=='pinjem buku':
    pinjembuku(user1)
elif Choice=='1'or Choice=='CariBuku':
    os.system('cls')
    carlos=input('Cari Buku: ').title()
    listbukuFound=[]
    for i in range(len(perpustakaan.daftar_buku)):
        if carlos in perpustakaan.daftar_buku[i].judul or carlos in perpustakaan.daftar_buku[i].penulis:
            listbukuFound.append(perpustakaan.daftar_buku[i])
            # perpustakaan.daftar_buku[i].tampilkan_info()
    if len(listbukuFound)==0:
        print('tidak di temukan')
    else:
        for i in range(len(listbukuFound)):
            listbukuFound[i].tampilkan_info()
    
'''
tantangan:
-> Menambahkan fitur penyimpanan data ke file

words = ["Hello", "world", "from", "Python!"]
sentence = ",".join(words)
Hello,world,from,Python!

selesaikan ini
masuk UI pakai ttkbootstrap / CustomTkinter
intro DFD dan UI design
finish project UI
review dari basic (tipe data dictionary, list => numpy[array])
error exception, class / oop
numpy, dan pandas
'''