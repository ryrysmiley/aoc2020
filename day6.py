def customsform(file):
    with open(file, "r") as x:
        peopleform = x.read().split("\n") 
    indivform = set()
    sum = 0
    for element in peopleform:
        if len(element) == 0:
                sum+=len(indivform)
                indivform.clear()
                continue
        for letter in element:
            indivform.add(letter)
    print(sum)
customsform("day6.txt")

def customsformall(file):
    pass


customsformall("day6.txt")
    