#===============library=================#
import os,time

#================class==================#
class Hewan:
    def __init__(self,nama):
        self.nama=nama
#===============mamalia==================#
class Mamalia(Hewan):
    def menyusui(self):
        print(f'{self.nama} menyusui')
    
class Anjing(Mamalia):
    def ngomong(self):
        print(f'{self.nama} mengonggong')

class Kucing(Mamalia):
    def ngomong(self):
        print(f'{self.nama} ngeong')
#===============aves==================#
class Aves(Hewan):
    def bertelur(self):
        print(f'{self.nama} bertelur')

class ayan(Aves):
    def ngomong(self):
        print(f'{self.nama} berkokok')
class bebek(Aves):
    def ngomong(self):
        print(f'{self.nama} berquekquek')
#===============ikan==================#
class fish(Hewan):
    def bertelur(self):
        print(f'{self.nama} bertelur')
    def __init__(self, nama):
        super().__init__(nama)
        self.jenis = 'ikan'

class hiu(fish):
    def makan(self):
        print(f'{self.nama}{self.jenis} makan ikan')
class tuna(fish):
    def makan(self):
        print(f'{self.nama} makan ikan')


#================main==================#
phenolisarosimpacilo = Kucing('phenolisarosimpacilov')
phenolisarosimpacilo.ngomong()
dori=hiu('dori')
dori.makan()