text = input("Input the text you wish to reverse: ")
newstring = ""
length = len(text)

i = length - 1
while i >= 0:
    newstring += text[i]
    i -= 1

print(newstring)