def DosyaAc(adres="defter.csv"):
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")


dosya = DosyaAc()
# print(dosya.read())
# print(dosya.readline(30))
dosya.read(25)
# dosya.write("Faruk;Soner;555741852\n")
dosya.flush()
print(dosya.tell())
dosya.seek(0)
print(dosya.readlines())
