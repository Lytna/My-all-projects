liste = [13,45,6,3,54,17,17]
liste2 = []
for i in range(len(liste)):
    liste2.append(liste[i]+5)
    
print(liste2)




listetuple = (1,4,3,6,16,65,42)
#listetuple[2] = 80
print(listetuple)

listeset = {3,52,15,63,58,71,52}
print(listeset)

c = set(liste)
print(liste)
print(c)


dictt = {
    "samet" : "0546060606",
    "ogun" : listetuple,
 }

mliste = [0,-1,1,1,0,0,-1,1,0,-1,0,-1,0,0,1,1,1,-0,1,0,-1,1,0,-1,1]

def mulakat(a):
    vsayac = 0
    toplam = 0 
    for i in range(len(a)):
        toplam += a[i]
        if toplam <= 0:
            if a[i] == -1 and a[i+1] == 1:
                vsayac +=1
           
            
        
        
    print(f"Bu listede {toplam} tane V var. ")
    print(toplam)
mulakat(mliste)
            


sayiliste = [7,25,43,21,65,43,38,91,46,15]
print(sayiliste[2])

def fonk(sayi):
    for i in range(len(sayi)):
        for j in range(len(sayi)):
            if sayi[i] == sayi[j] and i != j:
                return f"eşit sayılar var {sayi[j]} = {sayi[i]} "
                
print(fonk(sayiliste))    



def setfonk(a):
    b = set(a)
    s1 = 0
    s2 = 0
    for i in b:
        s1 += i
    for i in a:
        s2 += i 

    return f"Tekrar eden sayı {s2-s1} "

print(setfonk(sayiliste))




def hashmap(a):
    hashmapdict = {} 
    for i in a:
        if i in hashmapdict:
            hashmapdict[i] += 1
        else:
            hashmapdict[i] = 1 
    for k,v in hashmapdict.items():
        if v == 2:
            return k

print(hashmap(sayiliste))

listeayni = [1,1,44,44,55,55,63,97,97,86,86,70,70,4,4]

def hashmapp(a):
    hashmapdict = {} 
    for i in a:
        if i in hashmapdict:
            hashmapdict[i] += 1
        else:
            hashmapdict[i] = 1 
    for k,v in hashmapdict.items():
        if v == 2:
            return k
        

