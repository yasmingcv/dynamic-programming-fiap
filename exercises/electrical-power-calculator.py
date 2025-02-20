resistence = int(input("Type the Resistence (R): "))
current = int(input("Type the Current (I): "))

def calculate(r, i):
    return r * (i ** 2)

print(f"The Electrical Power is {calculate(resistence, current)}")