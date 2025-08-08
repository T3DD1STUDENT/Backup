#======================library==========================================#
import os,time
#======================main==========================================#
class hewan():
    def __init__(self,nama,umur,jenis):
        self.nama=nama
        self.umur=umur
        self.jenis=jenis
class mamalia(hewan):
    def menyusui(self):
        print('Mamalia menyusui')

class anjing(mamalia):
    def mengonggong(self):
        print('Anjing mengonggong')

class platapus(mamalia):
    def bertelur(self):
        print('Platapus bertelur')

    def name(self):
        print(f'{self.nama}')
        return f'alive'
    
class kucing(mamalia):
    def ngeong(self):
        print('Kucing ngeong')

class aves(hewan):
    def bertelur(self):
        print('Aves bertelur')

class ayam(aves):
    def dimasak(self):
        print('Ayam dimasak')

class bebek(aves):
    def berenag(self):
        print('Bebek berenang')

class ikan(hewan):
    def bertelur(self):
        print('Ikan bertelur')

class dori(ikan):
    def findingdori(self):
        print('Dori found')
        
    def name(self):
        print(f'{self.nama}')
        return f'alive'
kucing=hewan('lorem',2,'anjing')
anjing=hewan('ipsum',3,'kucing')
print(kucing.name())
anjing.menyusui()