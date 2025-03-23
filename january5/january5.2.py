def palindromMu(kelime):
    if kelime == kelime[:: -1]:
        return "palindrom"
    else :
        return "degil"
    
print(palindromMu("kek"))
print(palindromMu("masa"))