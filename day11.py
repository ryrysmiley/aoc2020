
def cfilled(str):
    if str=="#":
        return 1
    return 0

def cempty(str):
    if str!="#":
        return 1
    return 0


with open("day11.txt","r") as x:
    rows = x.read().split("\n")
newrow = []

while 1:
    newrow = []
    for ind1, row in enumerate(rows):
        symbols=""
        for ind2, seat in enumerate(row):
            if seat==".":
                symbols+="."
            elif seat=="L":
                if ind1==0:
                    if ind2==0:
                        if cempty(rows[ind1][ind2+1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2+1])==3:
                            symbols+="#"
                        else:
                            symbols+="L"
                    elif ind2==len(row)-1:
                        if cempty(rows[ind1][ind2-1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2-1])==3:
                            symbols+="#"
                        else:
                            symbols+="L"
                    else:
                        if cempty(rows[ind1][ind2+1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2+1])+cempty(rows[ind1+1][ind2-1])+cempty(rows[ind1][ind2-1])==5:
                            symbols+="#"
                        else:
                            symbols+="L"

                elif ind1==len(rows)-1:
                    if ind2==0:
                        if cempty(rows[ind1][ind2+1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2+1])==3:
                            symbols+="#"
                        else:
                            symbols+="L"
                    elif ind2==len(row)-1:
                        if cempty(rows[ind1][ind2-1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2-1])==3:
                            symbols+="#"
                        else:
                            symbols+="L"
                    else:
                        if cempty(rows[ind1][ind2-1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2-1])+cempty(rows[ind1][ind2+1])+cempty(rows[ind1-1][ind2+1])==5:
                            symbols+="#"
                        else:
                            symbols+="L"

                else:
                    if ind2==0:
                        if cempty(rows[ind1][ind2+1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2+1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2+1])==5:
                            symbols+="#"
                        else:
                            symbols+="L"
                    elif ind2==len(row)-1:
                        if cempty(rows[ind1][ind2-1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2-1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2-1])==5:
                            symbols+="#"
                        else:
                            symbols+="L"
                    else:
                        if cempty(rows[ind1][ind2-1])+cempty(rows[ind1-1][ind2])+cempty(rows[ind1-1][ind2-1])+cempty(rows[ind1+1][ind2])+cempty(rows[ind1+1][ind2-1])+cempty(rows[ind1+1][ind2+1])+cempty(rows[ind1-1][ind2+1])+cempty(rows[ind1][ind2+1])==8:
                            symbols+="#"
                        else:
                            symbols+="L"
            else: #filled seat
                if ind1==0:
                    if ind2==0:
                        symbols+="#"
                    elif ind2==len(row)-1:
                        symbols+="#"
                    else:
                        if cfilled(rows[ind1][ind2+1])+cfilled(rows[ind1+1][ind2])+cfilled(rows[ind1+1][ind2+1])+cfilled(rows[ind1+1][ind2-1])+cfilled(rows[ind1][ind2-1])>=4:
                            symbols+="L"
                        else:
                            symbols+="#"

                elif ind1==len(rows)-1:
                    if ind2==0:
                        symbols+="#"
                    elif ind2==len(row)-1:
                        symbols+="#"
                    else:
                        if cfilled(rows[ind1][ind2-1])+cfilled(rows[ind1-1][ind2])+cfilled(rows[ind1-1][ind2-1])+cfilled(rows[ind1][ind2+1])+cfilled(rows[ind1-1][ind2+1])>=4:
                            symbols+="L"
                        else:
                            symbols+="#"

                else:
                    if ind2==0:
                        if cfilled(rows[ind1][ind2+1])+cfilled(rows[ind1+1][ind2])+cfilled(rows[ind1+1][ind2+1])+cfilled(rows[ind1-1][ind2])+cfilled(rows[ind1-1][ind2+1])>=4:
                            symbols+="L"
                        else:
                            symbols+="#"
                    elif ind2==len(row)-1:
                        if cfilled(rows[ind1][ind2-1])+cfilled(rows[ind1-1][ind2])+cfilled(rows[ind1-1][ind2-1])+cfilled(rows[ind1+1][ind2])+cfilled(rows[ind1+1][ind2-1])>=4:
                            symbols+="L"
                        else:
                            symbols+="#"
                    else:
                        if cfilled(rows[ind1][ind2-1])+cfilled(rows[ind1-1][ind2])+cfilled(rows[ind1-1][ind2-1])+cfilled(rows[ind1+1][ind2])+cfilled(rows[ind1+1][ind2-1])+cfilled(rows[ind1+1][ind2+1])+cfilled(rows[ind1-1][ind2+1])+cfilled(rows[ind1][ind2+1])>=4:
                            symbols+="L"
                        else:
                            symbols+="#"
        newrow.append(symbols)
    if newrow == row:
        print(newrow)
        break
    rows = newrow