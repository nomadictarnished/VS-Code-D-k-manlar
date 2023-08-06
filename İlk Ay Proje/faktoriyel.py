sayi = int(input("sayı:"))
def Faktoriel(numara):
    Faktoryel = 1
    for x in range(1, numara + 1):
        Faktoryel *= x
        
a = Faktoriel(sayi)
print(a)