# Stefan Norling
# sfn2mc

input = open("nodes_and_edges", "r")
vertices = input.readline.split()
nodesandedges = {}

for vertice in vertices:
    nodesandedges[vertice] = []

tempdata = input.readline()
numNodes = tempdata.split()[0]
numEdges = tempdata.split()[1]

i = 0
while i < numNodes:
    