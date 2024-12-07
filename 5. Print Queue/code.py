# Read the input file content
file_path = "./5. Print Queue///input.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# Split the rules and updates based on the input structure
ordering_rules = []
updates = []
is_reading_rules = True

for line in lines:
    line = line.strip()
    if not line:
        is_reading_rules = False
        continue
    if is_reading_rules:
        ordering_rules.append(line)
    else:
        updates.append(line)

# Parse the ordering rules into a dictionary
from collections import defaultdict

dependency_graph = defaultdict(list)
for rule in ordering_rules:
    x, y = map(int, rule.split('|'))
    dependency_graph[x].append(y)

# Function to check if an update is in the correct order
def is_update_correct(order, dependencies):
    positions = {page: i for i, page in enumerate(order)}
    for x, dependents in dependencies.items():
        if x not in positions:
            continue
        for y in dependents:
            if y in positions and positions[x] >= positions[y]:
                return False
    return True

# Check each update and find the middle page numbers for correctly ordered ones
correct_updates = []
middle_pages = []

for update in updates:
    pages = list(map(int, update.split(',')))
    if is_update_correct(pages, dependency_graph):
        correct_updates.append(pages)
        middle_index = len(pages) // 2
        middle_pages.append(pages[middle_index])

# Sum up the middle page numbers
result = sum(middle_pages)
print(result)

# ------------------------------------------------------------------

# Function to sort pages based on the dependency graph (topological sorting)
def sort_update_by_dependencies(order, dependencies):
    # Create a graph and in-degree count for the pages in the update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x in order:
        if x in dependencies:
            for y in dependencies[x]:
                if y in order:
                    graph[x].append(y)
                    in_degree[y] += 1

    # Add all pages in the update to ensure isolated nodes are included
    for page in order:
        if page not in in_degree:
            in_degree[page] = 0

    # Perform topological sort using Kahn's algorithm
    sorted_order = []
    queue = [node for node in order if in_degree[node] == 0]
    while queue:
        node = queue.pop(0)
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

# Process incorrectly ordered updates
incorrect_updates = []
sorted_middle_pages = []

for update in updates:
    pages = list(map(int, update.split(',')))
    if not is_update_correct(pages, dependency_graph):
        incorrect_updates.append(pages)
        sorted_pages = sort_update_by_dependencies(pages, dependency_graph)
        middle_index = len(sorted_pages) // 2
        sorted_middle_pages.append(sorted_pages[middle_index])

# Sum the middle page numbers of corrected updates
sorted_result = sum(sorted_middle_pages)
print(sorted_result)