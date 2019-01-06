while True:
    reps = 0
    num = input("Enter the number for which you want to find Kaprekars Constant: ")
    while num != "6174":
        if len(num) < 4:
            while len(num) != 4:
                num = '0' + num
        ascending = [int(num[0]), int(num[1]), int(num[2]), int(num[3])]
        ascending.sort()
        descending = ascending[::-1]
        print(ascending)
        print(descending)
        a = ""
        b = ""
        for item in ascending:
            a += str(item)
        for item in descending:
            b += str(item)
        a = int(a)
        b = int(b)
        done = False
        bigger = max(a,b)
        smaller = min(a,b)
        num = str(bigger - smaller)
        print("blah")
        reps += 1
    print(reps)