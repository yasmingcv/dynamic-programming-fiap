numbers = []

quantity = int(input("Type a number: "))

for i in range(quantity): 
    number = float(input("Type a number to create the list"))
    numbers.append(number)

print(f"The list is {numbers}")