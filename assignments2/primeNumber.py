 # Is it a prime number

def control1():
    
    number = int(input("Enter the number you want to check:"))
    if number <= 1:
        print("the number is not prime")
        return
    is_prime = True
    
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
    
    if is_prime:
         print("number is prime")
    else:
         print("the number is not prime") 
        
control1()
        
 
         



            