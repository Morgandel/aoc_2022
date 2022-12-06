import os
dir = os.path.dirname(os.path.realpath(__file__))
line = open(f"{dir}/input.txt").read()
def find_index(size):
    for i in range(len(line)-size):
        if len(set(line[i:i+size]))==size:
            return(i+size)

print(find_index(4))
print(find_index(14))