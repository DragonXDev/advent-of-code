import math
import itertools

with open(r"C:\Users\Amaar Chughtai\Desktop\AOSGit\data.txt", "r") as f:
    new_arr = f.read().splitlines()
    instructions = new_arr[0]
    paths = {}
    for i in new_arr[1:]:
        if i!="":
            paths[i.split(" ")[0]]=(i.split(" ")[2].split(",")[0][1:],i.split(" ")[3][:-1])
        

def findPath(currPos):
    p = 0
    total = 0
    counter = 0
    final = []
    while True:
        if instructions[p]=="L":
            currPos=paths[currPos][0]
        elif instructions[p]=="R":
            currPos=paths[currPos][1]
        total+=1
        if currPos[-1]=="Z":
            counter+=1
            final.append(total)
        if counter==2:
            break
        p+=1
        if p==len(instructions):
            p=0
    return final

digits = []
for i in paths:
    if i[-1]=="A":
        x = findPath(i)
        digits.append(x[1]-x[0])

print(math.lcm(*digits))