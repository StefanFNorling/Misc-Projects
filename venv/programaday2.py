file = open("programaday2.txt", "r")

besttlpath = ["", 0]
besttrpath = ["", 0]
bestblpath = ["", 0]
bestbrpath = ["", 0]

def tlpath(x, y, currpath, currval):
    if x == middlex and y == middley:
        global besttlpath
        if currval > besttlpath[1]:
            besttlpath = [currpath, currval]
    elif x <= middlex and y <= middley:
        tlpath(x + 1, y, currpath + "d ", currval + graph[x + 1][y])
        tlpath(x, y + 1, currpath + "r ", currval + graph[x][y + 1])

def trpath(x, y, currpath, currval):
    if x == middlex and y == middley:
        global besttrpath
        if currval > besttrpath[1]:
            besttrpath = [currpath, currval]
    elif x <= middlex and y >= middley:
        trpath(x + 1, y, currpath + "d ", currval + graph[x + 1][y])
        trpath(x, y - 1, currpath + "l ", currval + graph[x][y - 1])

def blpath(x, y, currpath, currval):
    if x == middlex and y == middley:
        global bestblpath
        if currval > bestblpath[1]:
            bestblpath = [currpath, currval]
    elif x >= middlex and y <= middley:
        blpath(x - 1, y, currpath + "u ", currval + graph[x - 1][y])
        blpath(x, y + 1, currpath + "r ", currval + graph[x][y + 1])

def brpath(x, y, currpath, currval):
    if x == middlex and y == middley:
        global bestbrpath
        if currval > bestbrpath[1]:
            bestbrpath = [currpath, currval]
    elif x >= middlex and y >= middley:
        brpath(x - 1, y, currpath + "u ", currval + graph[x - 1][y])
        brpath(x, y - 1, currpath + "l ", currval + graph[x][y - 1])

numgraphs = int(file.readline())
for each in range(numgraphs):
    info = file.readline().split(";")
    rows = len(info)
    middlex = rows // 2
    graph = []
    i = 0
    while i < rows:
        graph.append(list(map(int, info[i].split(","))))
        i += 1
    cols = len(graph[0])
    middley = cols // 2
    tlpath(0, 0, "", graph[0][0])
    trpath(0, cols - 1, "", graph[0][cols - 1])
    blpath(rows - 1, 0, "", graph[rows - 1][0])
    brpath(rows - 1, cols - 1, "", graph[rows - 1][cols - 1])
    best = max(besttlpath[1], besttrpath[1], bestblpath[1], bestbrpath[1])
    j = 0
    while j < rows:
        print(graph[j])
        j += 1
    if best == besttlpath[1]:
        print("The best path is taken from the top-left and is", besttlpath[0]+"with value", besttlpath[1])
    elif best == besttrpath[1]:
        print("The best path is taken from the top-right and is", besttrpath[0]+"with value", besttrpath[1])
    elif best == bestblpath[1]:
        print("The best path is taken from the bottom-left and is", bestblpath[0]+"with value", bestblpath[1])
    elif best == bestbrpath[1]:
        print("The best path is taken from the bottom-right and is", bestbrpath[0]+"with value", bestbrpath[1])