class Kedi:
    tur = "Ev Kedisi" # class attribute # Sınıf özelliği
    def __init__(self,adi,yas): #constructor # Yapıcı
        self.adi = adi # instance attribute # ornek özellik
        self.yas = yas
        


    def miyavla(self): # instance method # ornek metod
        print(self.adi,Kedi.tur,"Miyavladı")
    
    @classmethod
    def turSoyle(cls): # class method # Sınıf metodu
        return cls.tur
    
    def __del__(self): # destructor # Yıkıcı
        print(self.adi,"Rest In Peace")

    def isimgetir(self):
        print(self.isimgetir.__name__)
    
melek =  Kedi("Melek",4)
duman = Kedi("Duman",3)
misket = Kedi("Misket",3)
melek.miyavla()
duman.miyavla()
misket.miyavla()
print(misket.tur)
print(melek.tur)
print(duman.tur)
print(misket.adi)
print(melek.adi)
print(duman.adi)

duman.isimgetir()