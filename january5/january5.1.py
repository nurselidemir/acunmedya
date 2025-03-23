def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"  # Bölme hatasını önlemek için kontrol

    return toplam, fark, carpim, bolum
    
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))   

toplam, fark, carpim, bolum = hesap_makinesi(sayi1, sayi2)
# Burada fonksiyonun return ettiği dört değeri sırasıyla toplam, fark, carpim ve bolum değişkenlerine atıyoruz. Böylece daha sonra bunları ekrana yazdırabiliriz.
# Eğer bu atamayı yapmazsak, fonksiyon çalışsa bile sonuçlar kaybolur ve kullanamayız.

print(f"Toplam: {toplam}, Fark: {fark}, Çarpım: {carpim}, Bölüm: {bolum}")