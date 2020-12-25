def passwords(entry):
    with open(entry, "r") as x:
        counter = 0
        for i in x:
            currentpass = i.split(" ")
            rangeval = currentpass[0].split("-")

            low = (rangeval[0])
            high = (rangeval[1])

            letter = currentpass[1][0]
            charcount = currentpass[2].count(letter)
            if charcount <= int(high) and charcount >= int(low):
                counter+=1
    print(counter)

def passwordsstrict(entry):
    with open(entry, "r") as x:
        counter = 0
        for i in x:
            currentpass = i.split(" ")
            rangeval = currentpass[0].split("-")
            
            pos1 = int((rangeval[0]))
            pos2 = int((rangeval[1]))

            letter = currentpass[1][0]
            if currentpass[2][pos1-1] == letter or currentpass[2][pos2-1] == letter:
                if currentpass[2][pos1-1]!=currentpass[2][pos2-1]:
                    counter+=1
    print(counter)

passwords("day2.txt")
passwordsstrict("day2.txt")