class HandsomeCafe:
    def __init__(self,nama,umur,Jabatan):
        self.nama=nama
        self.umur=umur
        self.Jabatan=Jabatan
    def display(self):
        return f'{self.nama} berumur {self.umur} dengan jabatan {self.Jabatan}'

pekerja1=HandsomeCafe("\033[32m"'Cornilius sebastion decaprio the third''\033[0m',90,'CEO')
print(pekerja1.nama)
print(pekerja1.display())   
