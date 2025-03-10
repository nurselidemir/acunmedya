
def calculate():
    number1 = float(input("enter first number:"))
    number2 = float(input("enter second number:"))
    operation =(input("enter the operation (+, -, *, /) :"))
    
    if operation == "+":
        print(f"{number1} + {number2} = {number1 + number2}")
    elif operation == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
    elif operation == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
    elif operation == "/":
        if number2 == 0:
            print("the second number for division cannot be zero.")
        else:
            print(f"{number1} / {number2} = {number1 / number2}")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
    
calculate()
