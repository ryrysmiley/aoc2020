def sum2(entry):
    x = open(entry, "r")
    listnum = x.read().split("\n")
    x.close()
    listnum.pop()
    for num1 in listnum:
        for num2 in listnum:
            if (int(num1) + int(num2) == 2020):
                print(num1, num2)
                print(int(num1)*int(num2))
                return

def sum3(entry):
    x = open(entry, "r")
    listnum = x.read().split("\n")
    x.close()
    listnum.pop()
    for num1 in listnum:
        for num2 in listnum:
            for num3 in listnum:
                if (int(num1)+int(num2)+int(num3) == 2020):
                    print(num1, num2, num3)
                    print(int(num1)*int(num2)*int(num3))
                    return

sum2("day1.txt")
sum3("day1.txt")