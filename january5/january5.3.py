def fonk(yas):
    if yas >= 100:
        return "Zaten 100 yaşına ulaştınız."
    else :
        sonuc = 100 - yas
        return f"{sonuc} yil sonra 100 yasina ulasacaksiniz."
    
yas = int(input("Yasinizi girin:"))
print(fonk(yas))