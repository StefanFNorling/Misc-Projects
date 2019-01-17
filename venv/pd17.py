tests = [[7,1,3,2,6,4],[9,1,8,2,7,3,6,4,5]]
for x in tests:
    minimum = x[0]
    final = 0
    for i in range(1,len(x),1):
        if x[i] < minimum:
            minimum = x[i]
        elif x[i] - minimum > final:
            final = x[i] - minimum
    print(final)