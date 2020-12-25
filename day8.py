def gameconsole(file):
    with open(file, "r") as x:
        instruct = x.read().split("\n")
    accelerator = 0
    line = 0
    while 1:
        if instruct[line][0] == "c":
            return accelerator
        elif instruct[line][0:3]=="nop":
            instruct[line]= "c" + instruct[line]
            line+=1
        elif instruct[line][0:3]=="acc":
            accelerator+=int(instruct[line][4:])
            instruct[line]= "c" + instruct[line]
            line+=1
        else:
            instruct[line]= "c" + instruct[line]
            line += int(instruct[line][5:])
    return 0
print(gameconsole("day8.txt"))


def gameconsolefinish(file):
    x = open(file,"r")
    instruct = x.read().split("\n")
    for index, i in enumerate(instruct):
        with open(file,"r") as x:
            instruct1 = x.read().split("\n")
        newinstruct = []
        newinstruct = instruct1
        if i[0:3] == "nop":
            newinstruct[index] = "jmp" + newinstruct[index][3:]
            x = testrun(newinstruct)
            if x!=0:
                break
        elif i[0:3] == "jmp":
            newinstruct[index] = "nop" + newinstruct[index][3:]
            x = testrun(newinstruct)
            if x!=0:
                break
        else:
            continue
    return x
def testrun(listentry):
    line=0
    accelerator=0
    while 1:
        if len(listentry[line]) == 0:
            break
        if listentry[line][0] == "c":
            return 0
        elif listentry[line][0:3]=="nop":
            listentry[line]= "c" + listentry[line]
            line+=1
        elif listentry[line][0:3]=="acc":
            accelerator+=int(listentry[line][4:])
            listentry[line]= "c" + listentry[line]
            line+=1
        else:
            listentry[line]= "c" + listentry[line]
            line += int(listentry[line][5:])
    return accelerator
print(gameconsolefinish("day8.txt"))