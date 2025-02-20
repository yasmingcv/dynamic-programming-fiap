resistence = int(input("Type the Resistence (R): "))
current = int(input("Type the Current (I): "))

def calculate(i, r):
    return i * r 

print(f"The Electrical Voltage is {calculate(current, resistence)}")