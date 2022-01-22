#Funkcje - są po to żeby nie powtarzać w kółko tego samego
#def add(a, b): #add nazwa funkcji
#    return a + b
#def myMax(numbers):
    
#a = int(input())
#b = int(input())
#mySum = add(a,b)
#print(mySum)
#print(add(int(input("Podaj a:")), int(input("Podaj b:"))))

#n = int(input())

#first_number = input()
#areTheSame = True
#for i in range(n-1):
#    next_number = input()
#   if(next_number != first_number):
#        areTheSame = False
#        break
    
#print(areTheSame)


#n = int(input("podaj n liczb do wczytania, a nastepnie wartosci: "))
  
#liczba = int(input("podaj liczbe: "))
#max = liczba
#min = liczba
#i = 1
 
#while i < n:
#    liczba = int(input("podaj liczbe: "))
#    if liczba > max:
#        max = liczba
#    if liczba < min:
#        min = liczba
#    i += 1
     
#print(max)
#print(min)
import random

def max(tab):
    m=tab[0]
    for i in tab: #pętla for w Pythonie to bardziej "foreach"
        if i>m:   #i przyjmuje wartości kolejnych komórek tablicy tab
            m=i
    return m
 
def min(tab):
    m=tab[0]
    for i in tab:
        if i<m:
            m=i
    return m
 
tab=[]; #utworzenie tablicy
for i in range(10):
    tab.append(random.randint(0,20)) #wylosowanie wartośći
print "tablica: "+str(tab) #wypisanie całej tablicy
print "min: "+str(min(tab))
print "max: "+str(max(tab))
