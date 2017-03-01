__author__ = 'Sindre'
import random

def getWords(list1):
    list=["Nils", "Gulvmatte", "Potet","Teddy", "Iskrem","Python","Kodeklubben","Hus","Fjell","Nisse","Bjørn","Elefant"]
    pos = random.randint(0, len(list)-1)
    list1.append(list[pos])
    return list1

def checkLists(list1, list2):
    return list1==list2
        
list1=[]
list2=[]
num=0
while(checkLists(list1,list2)):
    list1=getWords(list1)
    print(list1)
    input("Klikk enter når du er klar til å huske")
    for n in range(100):
        print()
    ans=input("Skriv inn ordene i riktig rekkefølge, skill dem med bindestrek -")
    list2=ans.split("-")
    num+=1
print("Bra, du klarte å huske "+str(num-1)+" ord på rad")
    
