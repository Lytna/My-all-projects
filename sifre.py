import random

kucuk_harfler = "".join(chr(s) for s in range(ord('a'), ord('z') + 1))
buyuk_harfler = "".join(chr(s) for s in range(ord('A'), ord('Z') + 1))
sayilar = "0123456789"
ifadeler = "+-*/?}])([{&%$#£"

sifre = ""
a = int(input("b"))

liste = [kucuk_harfler,buyuk_harfler,sayilar,ifadeler]

#for i in range(a):
    #sifre+= random.choice(random.choice(liste))
    
print(sifre)

for i in range(a):
    if i%4 == 0:
        sifre+= random.choice(kucuk_harfler)
    elif i%4 == 1: 
        sifre+= random.choice(sayilar)
    elif i%4 == 2:
        sifre+= random.choice(ifadeler)
    elif i%4 == 3:
        sifre+= random.choice(buyuk_harfler)

print(sifre)
