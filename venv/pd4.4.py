file = open("pd4.txt", "r")

def square(x, y):
    if matrix[x][y] == 1:
        if not x - 1 < 0:
            if not y - 1 < 0:
                


numofms = int(file.readline())
i = 0
while i < numofms:
    matrix = []
    valuematrix = []
    line = file.readline()
    rows = line.split(",")
    numrows = len(rows)
    numcols = len(rows[0])
    j = 0
    while j < numrows:
        matrix.append([])
        valuematrix.append([])
        for char in rows[j]:
            matrix[j].append(int(char))
            valuematrix[j].append(0)
        j += 1
    i = 0
    while i < numrows:
        j = 0
        while j < numcols:
            square(i, j)