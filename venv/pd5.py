text = input("Type the text in which you want to find the longest word present: ")
tempword = ""
longestword = ""
maxlength = 0

for char in text:
    if char.isalpha():
        tempword += char
    else:
        if len(tempword) > maxlength:
            longestword = tempword
            maxlength = len(tempword)
            tempword = ""
        else:
            tempword = ""

if len(tempword) > maxlength:
    longestword = tempword
    maxlength = len(tempword)

print(longestword)