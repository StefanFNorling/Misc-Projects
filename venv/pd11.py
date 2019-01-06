def hor(row, col):
    i = 0
    while i < 8:
        if occupied[row][i] == 1 and i != col:
            #print("hey",row, col, row, i)
            return False
        i += 1
    return True

def vert(row, col):
    i = 0
    while i < 8:
        if occupied[i][col] == 1 and i != row:
            #print("woah",row, col, i, col)
            return False
        i += 1
    return True

def rdiag(row, col):
    i = 0
    small = min(row, col)
    x = row - small
    y = col - small
    while x < 8 and y < 8:
        if occupied[x][y] == 1 and (x != row and y != col):
            #print("aye", row, col, x, y)
            return False
        x += 1
        y += 1
    return True

def ldiag(row, col):
    i = 0
    small = min(row, col)
    x = row + small
    y = col - small
    while x >= 0 and y < 8:
        if occupied[x][y] == 1 and (x != row and y != col):
            #print("spook", row, col, x, y)
            return False
        x -= 1
        y += 1
    return True

with open("pd11.txt", "r") as file:
    for each in file:
        each = each.rstrip()
        parts = each.split(', ')
        finparts = []
        for part in parts:
            part = part[2:-2]
            temp = part.split(",")
            part = [0,0]
            part[0] = int(temp[0]) - 1
            part[1] = int(temp[1]) - 1
            finparts.append(part)
        occupied = []
        i = 0
        while i < 8:
            occupied.append([0,0,0,0,0,0,0,0])
            i += 1
        #print(occupied)
        for queen in finparts:
            #print(queen[0], queen[1])
            occupied[queen[0]][queen[1]] = 1
        #print(occupied)
        for queen in finparts:
            a = queen[0]
            b = queen[1]
            good = hor(a,b) and vert(a,b) and rdiag(a,b) and ldiag(a,b)
            if not good:
                print('"(' + str(a + 1) + ',' + str(b + 1) + ')"')
                break
        if good:
            print("true")
