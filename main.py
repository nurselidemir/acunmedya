print("Kodlamio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
# integer => tam sayı
vade = 36
vade2 = "36"
ekVade = 6

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean =>  true or false
yukselisteMi = False

# matematiksel operatörler
print(vade + 12)
print(vade + ekVade)
print(5-5)
print(vade- ekVade)

print(5*5)
print(vade * 2)
print(vade * ekVade)

print(5/5)
print(vade / 2)
print(vade / ekVade)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod operatörü
print(10%2)
print(vade % 5)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 >= 1)
print(1 != 1)

# or, and
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)

# karar yapıları, if else
sayi1 = 10
sayi2 = 15
# indent
if sayi1 > sayi2 :
    print("sayi 1 sayi 2 den küçüktür")
    print("hala if bloğunun içerisindeyim")
# eğer if ve else if bloklarına girmez ise
elif sayi1 == sayi2:
    print("iki sayi eşittir")
else:
    print("sayi 1 sayi 2 den büyüktür")
print("burası if bloğunun dışıdır")
