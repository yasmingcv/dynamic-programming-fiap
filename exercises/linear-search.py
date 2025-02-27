list = [10, 17, 19, 90, 109, 55, 11, 41]
number = int(input("Search the number: "))

for i in range(len(list)):
    if (list[i] == number):
        print(i)
