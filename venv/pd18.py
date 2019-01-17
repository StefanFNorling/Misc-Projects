file = open("pd18.txt", "r")
cases = int(file.readline())
for i in range(0,cases,1):
    numsoldiers = int(file.readline())
    dwalked = file.readline().split()
    ascending = []
    final = []
    for j in range(len(dwalked)):
        ascending.append(j+1)
        dwalked[j] = int(dwalked[j])
    #print(dwalked)
    #print(ascending)
    lendw = len(dwalked)
    for x in range(lendw-1, 0, -1):
        final.append(ascending[x]-dwalked[x])
        for y in range(ascending[x]-dwalked[x]-1, lendw, 1):
            ascending[y] = ascending[y]+1
        #print(ascending)
    for x in range(1, lendw):
        if x not in final:
            final.append(x)
            break
    final.reverse()
    print(final)