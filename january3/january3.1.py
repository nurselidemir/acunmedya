for i in range(1, 101):
    print(i)
    
print("***************************************")

for i in range (2, 100, 2):
    print(i)

print("***************************************")

num = int(input("sayiyi giriniz:"))

def fact(num):
    if num == 0 or num == 1:
        return 1
    else :
        result = 1
        for i in range (1, num+1):
            result *= i
        return result
    
print(f"{num} ! = {fact(num)}")
    