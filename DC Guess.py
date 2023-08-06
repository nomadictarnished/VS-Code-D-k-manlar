sayi = int(input("Sayı gir:"))
def FaktöriyelBulma(sayi):
    Faktöriyel = 1
    for i in range(1, sayi +1):
        Faktöriyel *= i
    return Faktöriyel


