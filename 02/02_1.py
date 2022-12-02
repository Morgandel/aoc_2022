strat = {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2}
lines = [(strat[p1], strat[p2]) for p1, _, p2 in open("input.txt").read().splitlines()]
total = 0
for p1, p2 in lines:
    total += p2
    if p1 == p2:
        total += 3
    if (p2-p1)%3 == 1:
        total += 6
print(total+len(lines))