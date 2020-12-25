def passcheck(file):
    with open(file, "r") as x:
        passports = x.read().split("\n")
    valid = 0
    passportdict={}
    for pp in passports:
        elements = pp.strip().split(" ")
        for i in elements:
            if i == "":
                if len(passportdict) == 7:
                    valid+=1
                passportdict={}
                break
            field = i.split(":")
            if field[0] != "cid":
               passportdict[field[0]]=field[1]
    print(valid)

passcheck("day4.txt")

def passcheckstrict(file):
    with open(file, "r") as x:
        passports = x.read().split("\n")
    valid = 0
    passportdict={}
    for pp in passports:
        elements = pp.strip().split(" ")
        for i in elements:
            if i == "":
                if len(passportdict) == 7:
                    a=heightcheck(passportdict["hgt"])
                    b=haircheck(passportdict["hcl"])
                    c=eyecolor(passportdict["ecl"])
                    d=passid(passportdict["pid"])
                    e=byr(passportdict["byr"])
                    f=iyr(passportdict["iyr"])
                    g=eyr(passportdict["eyr"])
                    if a and b and c and d and e and f and g:
                        valid+=1
                passportdict={}
                break
            field = i.split(":")
            if field[0] != "cid":
               passportdict[field[0]]=field[1]
    print(valid)

def heightcheck(entry):
    if "cm" in entry:
        num = int(entry[:-2])
        if num >= 150 and num <= 193:
            return True
    elif "in" in entry:
        num = int(entry[:-2])
        if num >= 59 and num <= 76:
            return True
    return False

def haircheck(entry):
    if len(entry) != 7 or entry[0] != "#":
        return False
    entry1 = entry[1:]
    for i in entry1:
        if i not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
            return False
    return True

def eyecolor(entry):
    if entry in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return True
    return False

def passid(entry):
    if len(entry) != 9:
        return False
    for i in entry:
        if i not in ["0","1","2","3","4","5","6","7","8","9"]:
            return False
    return True

def byr(entry):
    if int(entry) >= 1920 and int(entry) <= 2002:
        return True
    return False

def iyr(entry):
    if int(entry) >= 2010 and int(entry) <= 2020:
        return True
    return False

def eyr(entry):
    if int(entry) >= 2020 and int(entry) <= 2030:
        return True
    return False

passcheckstrict("day4.txt")