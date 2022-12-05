import os
import re
dir = os.path.dirname(os.path.realpath(__file__))
def parse_file():
    with open(f"{dir}/input.txt") as file:
        stacks_input, lines_input = file.read().split("\n\n")
        stacks = [[] for _ in range(9)]
        stacks_input = stacks_input.splitlines()[:-1]
        stacks_input.reverse()
        for line in stacks_input:
            for i in range(8, -1, -1):
                if line[i*4+1] != " ":
                    stacks[i].append(line[i*4+1])
        com = list(map(int, re.findall(r'(\d+)', lines_input)))
    return stacks, com

def part_one():
    stacks, com = parse_file()
    for i in range(0, len(com), 3):
        for _ in range(com[i]):
            stacks[com[i+2]-1].append(stacks[com[i+1]-1].pop())
    return stacks

def part_two():
    stacks, com = parse_file()
    for i in range(0, len(com), 3):
        stacks[com[i+2]-1] += stacks[com[i+1]-1][-com[i]:]
        del stacks[com[i+1]-1][-com[i]:]
    return stacks

def results(stacks):
    result = ""
    for i in range(len(stacks)):
        result += stacks[i].pop()
    return result
        
print(results(part_one()))
print(results(part_two()))