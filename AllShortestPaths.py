# Stefan Norling
# sfn2mc
# Based on my algorithms homework question which I misinterpreted
# Finds all minimum length spanning trees

input = open("nodes_and_edges.txt", "r")
vertices = input.readline().split()
nodesedges = []

for vertice in vertices:
    nodesedges.append([int(vertice), []])

numNodes = len(vertices)

i = 0
while i < numNodes:
    tempdata = input.readline().split()
    source = int(tempdata[0])
    numNeighbors = len(tempdata)
    j = 1
    while j < numNeighbors:
        nodesedges[source][1].append(tempdata[j])
        j += 1
    i += 1

print(nodesedges)

