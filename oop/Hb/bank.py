def curency(anka):
    return f"Rp {anka:,}"
class bank:
    pass
class Pekerja(bank):
    def __init__(self, nama,umur,gaji):
        self._nama = nama
        self._umur = umur
        self._gaji = gaji
    def display(self):
        print('='*11,"Informasi pekerja Bank",'='*11)
        print(f"Nama: {self._nama}\nUmur: {self._umur}\nGajiper Tahun: RP {self._gaji:,}")
        print('='*46)
        print()
class pengguna(bank):
    def __init__(self, nama, saldo):
        self._nama = nama
        self.__saldo = saldo
    def display(self):

        print(f"Nama: {self._nama}\nsaldo: RP {self.__saldo:,}\n")
        print('='*45)
        print()
user1 = pengguna("Cornilius sebastion decaprio the third", 1)


user2 = pengguna("Ciceli", 295000000)
slave1=Pekerja('Borgol',11,5000000)



nm=input("Display User or Slave? ").lower()
if nm=='user':
    print('='*12,"Informasi Akun Bank",'='*12,'\n')
    user1.display()
    user2.display()
elif nm=='slave':
    slave1.display()
    slave1.display()
