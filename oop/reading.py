import os, time
class buku:
    def __init__(self, judul, penerbit, tahun_terbit):
        self.judul = judul
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.tersedia = True
    def pinjem(self):
        if self.tersedia:
            print(f'pinjem buku {self.judul}')
            self.tersedia = False
        else:
            print(f'buku {self.judul} tidak tersedia')
        time.sleep(1)
    def kembali(self):
        print(f'mengembalikan buku {self.judul}')
        time.sleep(1)
    def view(self):
        print(f'judul buku: {self.judul}')
        print(f'penerbit: {self.penerbit}')
        print(f'tahun terbit: {self.tahun_terbit}')
        if self.tersedia:
            print('buku tersedia')
        else:
            print('buku tidak tersedia')
        time.sleep(1)
def book():
    for i in range(len(bukubuku)):
        print(f'{i+1}. {bukubuku[i].judul}')
def clear():
    os.system('cls')
buku1 = buku('tedcode101','tcu','2003')
buku2 = buku('leluconsianing','artuer','2025')
bukubuku = []
bukubuku.append(buku1)
bukubuku.append(buku2)
buku1.view()
low=''
while True:
    clear()
    print('=========List Buku==========')
    book()
    print('==========================')
    opt=input('pilih buku: ')
    if opt == '1':
        low=buku1
    if opt == '2':
        low=buku2
    opt=input("1.Pinjem\n2.Kembali\n3. view\n").lower()
    if opt == 'pinjem'or opt == '1':
        low.pinjem()
    elif opt == 'view' or opt == '3':
        low.view()
    elif opt == 'kembali' or opt == '2':
        low.kembali()
    else:
        input('exit')
