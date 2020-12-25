def pathing(file,right,down):
    with open(file, "r") as x:
        gridtrees = x.read().split("\n")
    gridtrees.pop()
    trees = 0
    patternlength=len(gridtrees[0])-1 #indices count
    rows = len(gridtrees)-1 #indices count
    x = 0 #xcoord
    y = 0 #ycoord
    while 1:
        if gridtrees[y][x] == "#":
            trees+=1
        x+=right
        y+=down
        if x>patternlength:
            x -= (patternlength+1)
        if y>rows:
            break
    print(trees)
pathing("day3.txt",3,1)

pathing("day3.txt",1,1)
pathing("day3.txt",3,1)
pathing("day3.txt",5,1)
pathing("day3.txt",7,1)
pathing("day3.txt",1,2)
