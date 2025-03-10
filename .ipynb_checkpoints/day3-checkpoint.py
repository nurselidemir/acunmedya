# sınıflar

class Human:
    name = "Halit"      # default value
    # built-in
    def __init__(self, name):       # nesne üretildiğinde çalışan yapıcı blok
        self.name = name
        print("bir human instance'i üretildi")   
    def __str__(self):
        return f"str fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):       # classlarda fonk tanımlıyorsan parametre olmalı(self)
        print(f"{self.name} {sentence}")    # classın içindeki diğer alanlara erişebilmek için self gerekli
    def walk(self):                 # self => this
        print(f"{self.name} is walking")
        
# instance (örnek)      nesnelere erişebilmek için instance oluşturmalıyız.

human1 = Human("Enes")       # instance oluşturuldu
human1.talk("merhaba")
print(human1)

human2 = Human("Halit")   
human2.talk("Selam")
human2.walk()
print(human2)



