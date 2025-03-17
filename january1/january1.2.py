
sayi1 = int(input("Birinci sayiyi giriniz:"))
sayi2 = int(input("İkinci sayiyi giriniz:"))

print(f"Sayıların toplamı {sayi1+sayi2}")
print(f"Sayiların farkı {abs(sayi1-sayi2)}")
print(f"Sayıların çarpımı {sayi1*sayi2}")

if sayi2 != 0:
    print(f"Sayıların bölümü {sayi1/sayi2}")
else:
    print("Hata: Sayıyı sıfıra bölemezsiniz!")