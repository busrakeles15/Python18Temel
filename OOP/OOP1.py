class Araba:
    tur = "Araba"
    def __init__(self,marka,model):
        self.model = model
        self.marka = marka
    
    def yuru(self):
        print(self.model,self.marka,"Yürüdü")
    
    def dur(self):
        print(self.model,self.marka,"Durdu")


Arac1 = Araba("BMW","5.20")
Arac2 = Araba("Audi","A8L")
Arac1.yuru()
      
print(Araba.tur)
print(Arac1.tur)
