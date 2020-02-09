class MarvelHero:
    tip = "Marvel"
    def __init__(self,guc,saglik,isim):
        self.guc = guc
        self.saglik = saglik
        self.isim = isim
    
    def vur(self):
        return self.guc

    def darbe(self,guc):
        self.saglik -= guc
        return self.saglik


    
P1 = MarvelHero(100,500,"DeadPool")
P2 = MarvelHero(50,450,"IronMan")
print(P1.darbe(P2.vur()))
print(f"{P2.isim} ==> {P1.isim} vurdu :\
    {P1.isim} Saglık:{P1.saglik} {P2.isim} Saglık:{P2.saglik}")
