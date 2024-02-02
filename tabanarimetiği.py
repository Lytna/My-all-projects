print("[1] Ondalık tabandan İKİLİ,SEKİZLİ,ONALTILI tabana dönüştürme [1]")
print("[2] İkili, Sekizli veya Onaltılı Tabandaki Sayıyı Ondalık Tabana Dönüştürme [2]")

def choice1():
    number = int(input("Dönüştürmek İstediğiniz Ondalık sayı: "))
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    print("İkili Taban:", binary)
    print("Sekizli Taban:", octal)
    print("Onaltılı Taban:", hexadecimal)

def choice2():
    print("[ 1 ] İkili Taban (binary)  [ 1 ]")
    print("[ 2 ] Sekizli Taban: (octal)  [ 2 ]")
    print("[ 3 ] Onaltılı Taban  (hexadecimal)  [ 3 ]")
    arithmetic = int(input("Hangi tabanda işlem yapıcaksınız: "))
    if arithmetic == 1:
        binary = input("Ondalık Sayıya dönüştürmek istediğiniz (Binary) İkili taban sayısı: ")
        decimal_representation1 = int(binary, 2)
        print(binary, "Sayısının Ondalık hali:", decimal_representation1)

    elif arithmetic == 2:
        octal = input("Ondalık Sayıya dönüştürmek istediğiniz (Octal) Sekizli taban sayısı: ")
        decimal_representation2 = int(octal, 8)
        print(octal, "Sayısının ondalık hali: ", decimal_representation2) 

    elif arithmetic == 3:
        hexadecimal = input("Ondalık Sayıya dönüştürmek istediğiniz (hexadecimal) Onaltılı taban sayısı: ")
        decimal_representation3 = int(hexadecimal, 16)
        print(hexadecimal, "Sayısının ondalık hali: ", decimal_representation3)

a = int(input("İşleminiz Nedir? "))
if a == 1:
    choice1()
else:
    choice2()