kelimeler = []  

for i in range(5):  # Kullanıcıdan 5 kelime al
    kelime = input("Bir kelime girin: ")
    kelimeler.append(kelime) 

kelimeler.reverse()  # Listeyi ters çevir

print("Ters sıralı liste:", kelimeler)
