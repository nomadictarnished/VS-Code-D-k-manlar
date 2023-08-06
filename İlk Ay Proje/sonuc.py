boy = int(input("Boyunuz:"))
kutle = int(input("Kilonuz:"))
def VK_indeks(boy,kutle):
    sonuc = kutle/(boy*boy)
    return sonuc

a = VK_indeks(3,4)
print(a)