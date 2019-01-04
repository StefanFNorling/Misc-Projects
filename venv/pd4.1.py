def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

while True:
    x = input("Factorial of? (Anything but number to quit) ")
    if not x.isdecimal():
        exit(0)
    print(factorial(int(x)))