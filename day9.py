def numrule(file):
    with open(file,"r") as x:
        numlist = x.read().split("\n")
    start=0
    end=25
    lenlist=len(numlist)+1
    while end!=lenlist:
        checker = False
        for ind1, i1 in enumerate(numlist[start:end]):
            for ind2, i2 in enumerate(numlist[start:end]):
                if ind1 == ind2:
                    continue
                if (int(i1) + int(i2)) == int(numlist[end]):
                    checker = True
                    break
        if checker == False:
            return int(numlist[end])
        start+=1
        end+=1

print(numrule("day9.txt"))

def con_numbers(file,val):
    answernums = []
    with open(file,"r") as x:
        numlist = x.read().split("\n")
    for ind1, i1 in enumerate(numlist):
        for i2 in numlist[ind1:]:
            answernums.append(int(i2))
            if sum(answernums)==val:
                print(answernums)
                return min(answernums)+max(answernums)
            elif sum(answernums)>val:
                answernums=[]
                break
        

print(con_numbers("day9.txt",numrule("day9.txt")))