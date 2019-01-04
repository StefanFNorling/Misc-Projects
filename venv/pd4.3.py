def add(x):
    if x == 1:
        return 1
    else:
        return x + add(x - 1)

while True:
    x = input("Add numbers from 1 to what number? (Anything but number to quit) ")
    if not x.isdecimal():
        exit(0)
    print(add(int(x)))