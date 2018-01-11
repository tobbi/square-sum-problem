import argparse
import math

parser = argparse.ArgumentParser(description='Find the hamiltonian path through a list of numbers from 1 to n, two adjacent numbers adding up to a square number')
parser.add_argument('n', help="Max number", type=int)
args = parser.parse_args()
num_nodes = args.n

# Find hamiltonian path:
# Source: https://www.python.org/doc/essays/graphs/

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Returns true if the square root of this number is an integer
def is_sqrt(num):
    return (math.sqrt(num)).is_integer()

# Creates all the keys for the list
def make_list(max_value):
    res_array = {}
    for i in range(1, max_value + 1):
        res_array[i] = []
    return res_array

available_nodes = make_list(num_nodes)

# Fill the values of the list with those numbers that form a square number
for num_one in available_nodes.keys():
    for num_two in available_nodes.keys():
        if is_sqrt(num_one + num_two):
            available_nodes.get(num_one).append(num_two)

print("Available Hamiltonian paths for list from 1 to %s:" % num_nodes)
print("(the edge of two numbers forming a square number)")

found = False
for num_one in available_nodes.keys():
    for num_two in available_nodes.keys():
        all_paths = find_all_paths(available_nodes, num_one, num_two)
        for path in all_paths:
            if len(path) == num_nodes:
                found = True
                print(path)

if found == False:
    print("No paths found")