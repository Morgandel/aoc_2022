import os
dir = os.path.dirname(os.path.realpath(__file__))
lines = [line.split(",") for line in open(f"{dir}/input.txt").read().splitlines()]
cpt=0
for line in lines:
    min1, max1 = map(int,line[0].split("-"))
    min2, max2 = map(int,line[1].split("-"))
    if min1 <= min2 and max1 >=max2 or min1 >= min2 and max1 <=max2:
        cpt+=1
print(cpt)