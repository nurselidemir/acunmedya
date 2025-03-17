
yas = int(input("yaşınızı giriniz:"))

if 0 <= yas <= 12 :
    print("Çocuk grubundasınız.")
if 13 <= yas <= 29 :
    print("Genç grubundasınız.")
if 20 <= yas <= 59 :
    print("Yetişkin grubundasınız.")
if 60 <= yas :
    print("Yaşlı grubundasınız.")