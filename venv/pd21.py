in1 = input("Enter string 1: ")
in2 = input("Enter string 2: ")

if len(in1) != len(in2):
    print("Not the same pattern")
    exit(0)

ht = {}
i = 0
for char in in1:
    if char not in ht:
        ht[char] = in2[i]
    else:
        if ht[char] != in2[i]:
            print("Not the same pattern")
            exit(0)
    i += 1

print("The strings have the same pattern")

a = 1
al = [1,2,3]
b = 2
bl = ["a","b"]
c = 3
cl = [1,"yo"]

dic = {}
dic[a] = al
dic[b] = bl
dic[c] = cl

print(dic[c])