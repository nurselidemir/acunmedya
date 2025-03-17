puan = int(input("Puanınızı giriniz:"))

if 90 <= puan <= 100 :
    print("Notunuz A")
elif 80 <= puan <= 89:
    print("Notunuz B")
elif 70 <= puan <= 79:
    print("Notunuz C")
elif 60 <= puan <= 69:
    print("Notunuz D")
elif 0 <= puan <= 59:
    print("Notunuz F")