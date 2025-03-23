    
def asalMi(sayi):
    if sayi < 2 :
        return False
    for i in range(2, sayi):
        if sayi % i == 0 :
            return False
    return True
        
        
for sayi in range(101):
    if asalMi(sayi):
        print(sayi)
    
    
    
    
    
