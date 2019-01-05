# Stefan Norling

# Checks if a message inside a message

status = True
while status:
    string1 = input("Enter the first message here (enter 'quit' to exit): ")
    if string1 in ("quit", "q", "Quit"):
        exit(0)
    string2 = input("Enter the message that you want to check is inside the other: ")
    length1 = len(string1)
    length2 = len(string2)
    i = 0
    j = 0
    total = 0
    while i < length1 and j < length2:
        if string1[i] == string2[j]:
            total += 1
            i += 1
            j += 1
        else:
            i += 1
    if total >= length2:
        print("The second message is contained in the first message")
    else:
        print("The second message is not contained in the first message")