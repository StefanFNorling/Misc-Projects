#file = open("pd4.txt", "r")
with open("pd4.txt", "r") as file:
#numofms = int(file.readline())
#a = 0
#while a < numofms:
    for each in file:
        matrix = []
        line = each.rstrip()
        rows = line.split(",")
        numrows = len(rows)
        numcols = len(rows[0])
        largest = 0
        dim = 0
        j = 0
        while j < numrows:
            matrix.append([])
            for char in rows[j]:
                matrix[j].append(int(char))
            j += 1
        i = 0
        while i < numrows:
            j = 0
            while j < numcols:
                if matrix[i][j] == 1:
                    #print(i, j)
                    if 1 > largest:
                        largest = 1
                    issquare = True
                    dim = 2
                    while issquare:
                        try:
                            x = 0
                            while x < dim:
                                if matrix[i + x][j + dim - 1] == 0 or matrix[i + dim - 1][j + x] == 0:
                                    issquare = False
                                    #print("blah")
                                    break
                                x += 1
                            if not issquare:
                                break
                            else:
                                if dim > largest:
                                    #print(i, j, dim)
                                    largest = dim
                                    #print(largest)
                                dim += 1
                        except IndexError:
                            break
                j += 1
            i += 1
        print("The area of the largest square submatrix is", largest ** 2)
        #a += 1