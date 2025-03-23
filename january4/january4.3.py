liste = [1, 2, 2, 3, 4, 4, 5, 6, 6] 

yeniListe = list(set(liste))  # `set()` ile tekrar edenleri kaldır

print("Tekrarsız liste:", yeniListe)
