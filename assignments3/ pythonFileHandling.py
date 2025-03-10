
with open("file.txt", "w") as file:
    text = input("Enter a text: ")
    file.write(text + "\n")

with open("file.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

with open("file.txt", "a") as file:
    print("Please enter 5 different lines:")
    for i in range(5):
        line = input(f"Line {i+1}: ")
        file.write(line + "\n")

print("\nUpdated File Content:")
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

        
        