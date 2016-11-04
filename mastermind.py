# Author: Aylin Gumus <aylingumus7@gmail.com>
# License: MIT

import random
import collections

seviyeler = collections.OrderedDict([
    ("kolay", 3),
    ("orta",  5),
    ("zor",  7)
])

print(*seviyeler.keys())
seviye = input("zorluk seviyesi seciniz: ")

if seviye in seviyeler:
    zorluk = seviyeler[seviye]
    print("seviye secildi: ", seviye)
else:
    zorluk = seviyeler["orta"]
    print("ontanimli seviye secildi: orta")

def girdi ():
    while True:
        sonuc = input("{} sayi giriniz :".format(zorluk))
        if sonuc.lower() in ("exit", "e"):
            print("programdan cikiliyor")
            exit(0)
        sonuc_liste = list(sonuc)

        try:
            sonuc_int = [int(i) for i in sonuc_liste]
        except ValueError as e:
            print("HATA: sayi giriniz!")
            continue

        if len(sonuc_int) != zorluk:
            print("HATA: {} sayi giriniz".format(zorluk))
            continue
        else:
            return sonuc_int


liste = random.sample(range(10), zorluk)

for tur in range(10):
    dogrular = []
    yarimlar = []
    sonuc_int = girdi()
    for girilen, beklenen in zip(sonuc_int, liste):
        if girilen == beklenen:
            dogrular.append(girilen)
            if girilen in yarimlar:
                yarimlar.pop(yarimlar.index(girilen))
        elif girilen in liste and girilen not in dogrular+yarimlar:
            yarimlar.append(girilen)

    print("dogru basamak sayisi = ", len(dogrular))
    print("yarim dogru basamak sayisi = ", len(yarimlar))
    print("kalan hak: ", 9-tur)
    if len(dogrular) == zorluk:
        print("tebrikler")
        break
else:
    print("game over")
    print("dogru cevap: ", *liste)

