import os
dir = os.path.dirname(os.path.realpath(__file__))
lines = open(f"{dir}/input.txt").read().splitlines()
total = 0
for i in range(0,len(lines),3):
    both = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
    for item in both:
        subs = ord("a") if item.islower() else ord("A")-26
        total += ord(item)-subs+1
print(total)