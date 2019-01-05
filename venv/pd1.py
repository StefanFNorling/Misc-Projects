file = open("programaday1.txt", "r")

numberofstrings = int(file.readline())

i = 0
while i < numberofstrings:
    original = file.readline()[:-1]
    index = len(original) - 1
    newstring = ""
    while index >= 0:
        newstring += original[index]
        index -= 1
    print(newstring)
    i += 1