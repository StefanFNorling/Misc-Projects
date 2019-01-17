file = open("pd19.txt", "r")
tests = int(file.readline())

inandout = []
for i in range(0,tests,1):
    temp = file.readline().split()
    temp2 = []
    for item in temp:
        temp2.append(int(item))
    inandout.append(temp2)
#print(inandout)
peoplein = 0
inmin = inandout[0][0]
outmax = 0

for item in inandout:
    if item[0] < inmin:
        inmin = item[0]
    if item[1] > outmax:
        outmax = item[1]
#print(inmin, outmax)

final = 0
for i in range(inmin, outmax):
    count = 0
    for item in inandout:
        if item[0] <= i and item[1] >= i:
            count += 1
    if count > final:
        final = count
print(final)