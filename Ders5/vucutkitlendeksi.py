boy = float(input("Boyunuz:"))
kutle = float(input("Kilonuz:"))
def VK_indeks(boy,kutle):
    sonuc = kutle/(boy*boy)
    print(sonuc)
    return sonuc

a = VK_indeks(boy,kutle)
print("Kitle Endeks Değeriniz:",a)

if a <= 18.5:
    print("BİRAZ YE BE")
elif a >= 18.5 and  a <= 24.9:
    print("İYİSİN BÖYLE DEVAM")
elif a >= 25 and a <= 29.9:
    print("BİRAZ AZ YE BANA GÜVEEN :)")
elif a >= 30:
    print("KARDEŞİM ÇOLUĞUN ÇOCUĞUN RIZKINI YEMİŞİN")
else:
    print("VAR MISIN YOK MUSUN BEN ANLAMADIM Kİ")

