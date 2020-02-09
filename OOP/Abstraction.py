from abc import abstractclassmethod,ABCMeta

class Animal:

    __metaclass__ = ABCMeta
    @abstractclassmethod
    def beslenme(self):
        print("Ben bir canlıyım")

class Mamal(Animal):
    def __init__(self,adi,yas,tur):
        self.adi = adi
        self.yas = yas
        self.tur = tur

    def beslenme(self):
        super(Mamal,self).beslenme()
        print(self.adi,"Beslenme")

    def SesCikar(self):
        print(self.adi,"Ses Çıkardı")

class Kopek(Mamal):
    def __init__(self,adi,yas):
        super().__init__(adi,yas,"Kopek")
    
    def beslenme(self):
        super(Kopek,self).beslenme()
        print("Kemik Beslendi")


class Kedi(Mamal):
    def __init__(self,adi,yas):
        super().__init__(adi,yas,"Kedi")


Kemik = Kopek("Kemik",10)
Kemik.beslenme()
