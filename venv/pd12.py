def recursivepent(x):
    if x == 1:
        return 1
    else:
        return 5 * (x - 1) + pent(x - 1)

def nrpent(x):
    i = 1
    total = 0
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        total = 1
        while i < x:
            total += 5 * i
            i += 1
        return total

while True:
    num = int(input("Enter the pentagon dot dimension (anything but a number to quit): "))
    if not isinstance(num, int):
        exit(0)
    print(nrpent(int(num)))