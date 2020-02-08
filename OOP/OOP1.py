class Araba:
    tur = "Araba"
    __makshiz = 0
    def __init__(self,marka,model):
        self.model = model
        self.marka = marka
        self.__makshiz = 250
    
    def yuru(self):
        print(self.model,self.marka,"Yürüdü")
    
    def dur(self):
        print(self.model,self.marka,"Durdu")


Arac1 = Araba("BMW","5.20")
Arac2 = Araba("Audi","A8L")
Arac1.yuru()
Arac1.__makshiz