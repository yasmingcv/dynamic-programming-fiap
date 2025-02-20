power = int(input("Type the Power (P): "))
voltage = int(input("Type the Voltage (V): "))

def calculate(p, v):
    return p / v

print(f"The Electrical Current is {calculate(power, voltage)}")