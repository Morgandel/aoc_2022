import os
dir = os.path.dirname(os.path.realpath(__file__))
lines = [(line[:(len(line)//2)],line[(len(line)//2):]) for line in open(f"{dir}/input.txt").read().splitlines()]
total = 0
for comp1, comp2 in lines:
    both = set(comp1) & set(comp2)
    for item in both:
        subs = ord("a") if item.islower() else ord("A")-26
        total += ord(item)-subs+1
print(total)