# naive prime number checker

file = open("programaday2.1.txt", "r")

quantity = int(file.readline())

counter = 0
while counter < quantity:
    valid = True
    number = int(file.readline())
    if number in (0, 1) or number < 0:
        valid = False
    i = 3
    cap = number // 2
    if  valid and number % 2 == 0:
        valid = False
    elif valid:
        while i < cap and valid:
            if number % i == 0:
                valid = False
            i += 2
    if valid:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    counter += 1