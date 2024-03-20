def alfabe_kontrol(karakter):
    return 'a' <= karakter <= 'z' or 'A' <= karakter <= 'Z'

def harf_kontrol(metin):
    return metin.lower()


def yuzde_hesapla(sayi, toplam):
    return sayi / toplam * 100

a = int(input("Lütfen bir sayı girin: "))
if a == 1:
    print("Bahtiyar Erener KURT\n211213009\nGeçmişinden ders almayan bir millet yok olmaya mahkumdur")

metin = input("Lütfen bir metin girin: ")
metin = harf_kontrol(metin)
frekanslar = {}

toplam_karakter_sayisi = len(metin)

for karakter in metin:
    if alfabe_kontrol(karakter):
        if karakter in frekanslar:
            frekanslar[karakter] += 1
        else:
            frekanslar[karakter] = 1

for karakter in sorted(frekanslar.keys()):
    sayi = frekanslar[karakter]
    kullanım_oranı = yuzde_hesapla(sayi, toplam_karakter_sayisi)
    print(f"{karakter}: {sayi} (Kullanım Oranı: {kullanım_oranı:.2f}%)")
