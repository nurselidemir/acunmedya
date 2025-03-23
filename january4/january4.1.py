numbers = []

for i in range(5):
  sayi = int(input("sayiyi giriniz:"))
  numbers.append(sayi)
  
toplam = sum(numbers)
ortalama = toplam / len(numbers)
enBuyuk = max(numbers)
enKucuk = min(numbers)

print(f"Toplam : {toplam} , Ortalama : {ortalama}, En Buyuk : {enBuyuk}, En Kucuk : {enKucuk}")

