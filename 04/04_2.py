import os
dir = os.path.dirname(os.path.realpath(__file__))
lines = [line.split(",") for line in open(f"{dir}/input.txt").read().splitlines()]
cpt=0
for line in lines:
    assign1 = list(map(int, line[0].split("-")))
    assign2 = list(map(int, line[1].split("-")))
    assign1[1] += 1
    assign2[1] += 1
    if len(set(range(*assign1)) & set(range(*assign2))) > 0:
        cpt+=1
print(cpt)