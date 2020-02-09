class A:
    def __init__(self):
        self.a = "A"
class B(A):
    def __init__(self):
        self.b = "B"
    def den2(self):
        print("ben B sınıfındayım")
class C(B):
    def __init__(self):
        self.c = "C"
    def den1(self):
        print("ben C sınıfındayım")
class D(C,B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = "D"

obj1 = D()
obj1.den1()
obj1.den2()
