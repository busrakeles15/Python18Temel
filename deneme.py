dosya = open("dataset.csv","w+")
import random as rnd
for i in range(5000):
    print(f"{rnd.randint(1,100)};{rnd.randrange(0,500,50)};{rnd.randint(0,300)}",file=dosya)