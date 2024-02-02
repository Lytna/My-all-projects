import random

def fonksiyon(a):
    kucuk_harfler = "".join(chr(s) for s in range(ord('a'), ord('z') + 1))
    buyuk_harfler = "".join(chr(s) for s in range(ord('A'), ord('Z') + 1))
    sayilar = "0123456789"
    ifadeler = "+-*/?}])([{&%$#£"

    sifre = ""
    
    liste = [kucuk_harfler,buyuk_harfler,sayilar,ifadeler]
    for i in range(a):
        sifre+= random.choice(random.choice(liste))
    return sifre   
