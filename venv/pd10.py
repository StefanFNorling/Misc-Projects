input = open("programaday3.txt", "r")

numberoflines = int(input.readline())

i = 0
while i < numberoflines:
    line = input.readline()
    if line[-1] == '\n':
        line = line[:-1]
    length = len(line)
    firstdig = 0
    firstdigset = False
    questions = 0
    isvalid = True
    j = 0
    while not firstdigset:
        for char in line:
            if char.isdigit():
                firstdig = int(char)
                firstdigset = True
                break
            j += 1
    while j < length:
        if line[j] == "?":
            questions += 1
        if line[j].isdigit():
            if firstdig + int(line[j]) == 10:
                if questions != 3:
                    isvalid = False
                    break
            else:
                firstdig = int(line[j])
                questions = 0
        j += 1
    if isvalid:
        print(line, "is valid")
    else:
        print(line, "is not valid")
    i += 1