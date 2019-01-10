import re
a = ["timmy","tammy", "billy"]
b = [10, 20, 43]
c = {}
i = 0
for each in a:
    c[each] = b[i]
    i += 1
print(c)
sentence = "Way over 15 years ago there was a man named Billy. Billy was the best at what he did and he did it for 29 years while working as a student for 4 of those years. This issue is not a particulairty of python; for instance, if you try to write a shell script, e.g. a for loop for creating directories: for i in dir1 in order for this script to run, there must be no space after the backslash. DavidC"
temp = re.findall(r"\d+", sentence)
print(temp)
temp = re.findall(r"[A-Z][a-z]*", sentence)
print(temp)
sentence = "@yomama Yo that meal was #bangin #delish"
temp = re.findall(r"@\w+", sentence)
print(temp)
temp = re.findall(r"#\w+", sentence)
print(temp)
sentence = "asdfjkcn13nam@gmail.com, stefannorling@gmail.com 12sfjmq_21dcj@yahool_blah.emb: yah@swab.net"
temp = re.findall(r"\w+@[A-Za-z]+\.[a-z]{3}", sentence)
print(temp)
rows = 5
cols = 10
matrix = [[0 for y in range(cols)] for x in range(rows)]
matrix[0][1] = 6
print(matrix)
