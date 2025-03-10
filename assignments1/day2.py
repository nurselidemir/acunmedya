faiz = 1.50
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))

print(int(vade)+12)
faiz = str(faiz)

print(type(faiz))

vade = int(input("lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
vade = vade + 12

# string interpolation

print("seçtiğiniz vade sonucu ortaya çıkan vade:" + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = 'Halit'
metin = "merhaba {name}".format(name = isim)   # {name} bu takma ad
print(metin)

# f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)

# listeler

dizi = ["ihtiyaç kredisi" , 10 , 5.2 , True]
print(dizi)
krediler = ["ihtiyaç kredisi" , "taşıt kredisi" , "konut kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])
 # print(krediler[5])  list index out of range hatası

print(len(krediler))
krediler.append("özel krediler")
print(krediler)

krediler.pop()    # default olarak son elemanı siler
print(krediler) 
krediler.pop(0)    # 0.indexi sildi
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)
krediler.remove("taşıt kredisi")    # 2 tane var index sırasına göre bulduğu ilk değeri siler
print(krediler)
# pop index ile remove değer ile çalışır

krediler.extend(["y kredisi", "z kredisi"])     # birden fazla eklenir
print(krediler)

# döngüler

# for föngüsü

for i in range(10):     # 0 dan başlar. 10 dahil değil. i < 10
    print(i)
print("*************")
for i in range(5,10):    # 5 den başlar. 10 dahil değil.
    print(i)
print("*************")
for i in range(0,51,10):   # 0 dan başlar, 50 ye kadar 10 artar.
    print(i)
print("*************")   
krediler = ["ihtiyaç kredisi" , "taşıt kredisi" , "konut kredisi"]
for kredi in krediler:
    print(kredi)
print("*************")   
for i in range(len(krediler)):
    print(krediler[i])   
print("*************") 

# while döngüsü
i = 0
while i < 10:
    print("x")
    i += 1        # i++ yok
print("*************")

while True:
    print("x")
    break    # sonsuz döngüyü kırar

print("*************")
 
i = 0
while i < len(krediler):
    if krediler[i] == "konut kredisi":
        break
    print(krediler[i])
    i += 1
     
# fonksiyonlar

fiyat = 100
indirim = 20
 # definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat - indirim)

calculate()
calculateWithParams(50,10)

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)      # çağırdığım yerde değer olarak alabilmek 
                                            # istiyorum. değişkene atamak için değer döndüren fonk kullandım.
print(yeniFiyat)

print("*************")

def calculatePrice(price, discount):
    print(price-discount)
    
def calculatePriceAndReturn(price, discount):
    return price-discount

fonk1 = calculatePrice(100,50)        # 50
fonk2 = calculatePriceAndReturn(300,100)     
  
print(fonk1)      # none    return yok değer fonksiyonun kendi içinde kullanılabilir
print(fonk2)      # 200    return ediliyorsa değer fonksiyonu çağırırken kullanabiliriz







    







