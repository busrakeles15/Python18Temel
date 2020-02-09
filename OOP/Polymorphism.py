
class Mamal():
    def __init__(self,adi,yas,tur):
        self.adi = adi
        self.yas = yas
        self.tur = tur

    def beslenme(self):
        print(self.adi,"Beslenme")

    def SesCikar(self):
        print(self.adi,"Ses Çıkardı")

class Kopek(Mamal):
    def __init__(self,adi,yas):
        super().__init__(adi,yas,"Kopek")

    def SesCikar(self):   # overriding
        print(self.adi," Hav Hav")
    def ataSesCikar(self):
        super(Kopek,self).SesCikar()

class Kedi(Mamal):
    def __init__(self,adi,yas):
        super().__init__(adi,yas,"Kedi")
    
    def SesCikar(self):
        print(self.adi," Miyav Miyav")

Kemik = Kopek("Kemik",5)
Kemik.ataSesCikar()
Kemik.SesCikar()
# Kemik.beslenme()
# print(Kemik.tur)
# Kemik.SesCikar()
# Melek = Kedi("Melek",3)
# Melek.beslenme()
# Melek.SesCikar()
# print(Melek.tur)
