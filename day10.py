from functools import lru_cache
def adapt(file):
    with open(file,"r") as x:
        adapters=[]
        for i in x:
            adapters.append(int(i.strip()))
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters.sort()
    onev=0
    twov=0
    threev=0
    for index, num in enumerate(adapters):
        if index == len(adapters)-1:
            break
        volt=adapters[index+1]-num
        if volt == 1:
            onev+=1
        elif volt == 3:
            threev+=1
        else:
            twov+=1
    print(onev*threev)
adapt("day10.txt")

#part two credited to u/thecircleisround on the advent of code reddit

adapters = [x for x in set(map(int, open("day10.txt")))]
maxvolt = max(adapters)+3
adapters.append(maxvolt)
adapters.insert(0,0)

@lru_cache(maxsize=3)
def possibilities(item):
    x = [z for z in range(item - 3,item) if z in adapters]
    if item == 0:
        return 1
    return sum(possibilities(i) for i in x)
print(possibilities(maxvolt))
