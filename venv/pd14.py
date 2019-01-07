def pathfinder(x, y):
    if x == a and y == b:
        global total
        total += 1
    if x < a:
        pathfinder(x + 1, y)
    if y < b:
        pathfinder(x, y + 1)

with open("pd14.txt", "r") as file:
    for each in file:
        each = each.rstrip()
        total = 0
        i, j, a, b = int(each[2]), int(each[4]), int(each[7]), int(each[9])
        pathfinder(i, j)
        print(total)