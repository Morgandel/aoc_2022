import os

TOTAL_ONE = 0

class Directories:
    def __init__(self, name, parent):
        self.name = name
        self.size = []
        self.parent = parent
        self.next_dir = {}
        self.total = 0
    
    def get_total_size(self):
        global TOTAL_ONE
        current_folder = sum(self.size)
        for dir in self.next_dir.values():
            current_folder += dir.get_total_size()
        if current_folder <= 100000:
            TOTAL_ONE += current_folder
        self.total = current_folder
        return current_folder

    def get_minimum_needed(self, total_used):
        result = 99999999999999999999999999999
        if total_used - self.total <= 40000000:
            result = min(result, self.total)
        for dir in self.next_dir.values():
            result = min(result, dir.get_minimum_needed(total_used))
        return result

def generate_graph():
    python_dir = os.path.dirname(os.path.realpath(__file__))
    lines = open(f"{python_dir}/input.txt").read().split("\n")
    for line in lines:
        command = line.split()
        match command:
            case ["$", "cd", "/"]:
                current_dir = Directories("/", None)
                root = current_dir
            case ["$", "cd", ".."]:
                current_dir = current_dir.parent
            case ["$", "cd", name]:
                current_dir = current_dir.next_dir[name]
            case ["dir", name]:
                next_dir = Directories(name, current_dir)
                current_dir.next_dir[name] = next_dir
            case [size, name]:
                if size.isdigit():
                    current_dir.size.append(int(size))
    return root

root = generate_graph()
root.get_total_size()
print(TOTAL_ONE)
print(root.get_minimum_needed(root.total))