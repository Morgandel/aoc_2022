strat = {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2}
lines = [(strat[p1], strat[p2]) for p1, _, p2 in open("input.txt").read().splitlines()]
total = 0
for p1, p2 in lines:
    if p2 == 0:
        total += (p1+2)%3
    elif p2 == 1:
        total += p1 + 3
    else:
        total += (p1+1)%3 + 6
        
print(total+len(lines))