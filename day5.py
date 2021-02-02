#solution and math found on advent of code reddit u/KingCravenGamer

with open("day5.txt","r") as x:
    codes = x.read().split()

def rowcolumn(seatcode):
    highest=0
    for i in seatcode:
        row=[i for i in range(128)]
        column=[i for i in range(8)]
        for let in i:
            if let == "F":
                row = row[:len(row)//2]
            if let == "B":
                row = row[len(row)//2:]
            if let == "L":
                column = column[:len(column)//2]
            if let == "R":
                column = column[len(column)//2:]
        id = (row[0]*8)+column[0]
        if id > highest:
            highest = id
    print(highest)
rowcolumn(codes)

def rowcolumnown(seatcode):
    seats = [[0 for i in range(8)] for i in range(128)]
    for i in seatcode:
        row=[i for i in range(128)]
        column=[i for i in range(8)]
        for let in i:
            if let == "F":
                row = row[:len(row)//2]
            if let == "B":
                row = row[len(row)//2:]
            if let == "L":
                column = column[:len(column)//2]
            if let == "R":
                column = column[len(column)//2:]
        seats[row[0]][column[0]] = -1
    print(seats)
    
    for count, row in enumerate(seats):
        for column, seat in enumerate(row):
            if seat == 0:
                if count != 0:
                    if column != 0 and column !=7:
                        if seats[count][column-1]==-1 and seats[count][column+1]==-1:
                            print(count*8+column)
                            print(count,column)
                            return
rowcolumnown(codes)