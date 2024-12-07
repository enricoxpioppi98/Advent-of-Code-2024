# Load the input map
file_path = "./6. Guard Gallivant/input.txt"
with open(file_path, 'r') as file:
    lab_map = [line.strip() for line in file.readlines()]

# Directions: up, right, down, left
directions = ['^', '>', 'v', '<']
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # row, col changes

# Locate the guard's starting position and direction
rows, cols = len(lab_map), len(lab_map[0])
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in directions:
            guard_position = (r, c)
            guard_direction = directions.index(lab_map[r][c])
            break

# Initialize visited positions
visited_positions = set()
visited_positions.add(guard_position)

# Simulation function
def move_guard(position, direction):
    row, col = position
    dr, dc = deltas[direction]
    return (row + dr, col + dc)

def is_within_bounds(position):
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

# Simulate the guard's movement
while True:
    # Compute the next position based on the current direction
    next_position = move_guard(guard_position, guard_direction)
    
    if is_within_bounds(next_position) and lab_map[next_position[0]][next_position[1]] == '#':
        # Obstacle in front, turn right
        guard_direction = (guard_direction + 1) % 4
    else:
        # Move forward if possible
        guard_position = next_position
        if not is_within_bounds(guard_position):
            break
        visited_positions.add(guard_position)

# Count the distinct visited positions
distinct_positions_count = len(visited_positions)
print(distinct_positions_count)

# ------------------------------------------------------------------

from collections import defaultdict

# Helper function to detect a loop
def simulate_guard_with_obstruction(lab_map, obstruction_pos):
    guard_position = None
    guard_direction = None
    # Reload the guard's starting position and direction
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in directions:
                guard_position = (r, c)
                guard_direction = directions.index(lab_map[r][c])
                break

    visited_states = set()
    current_path = set()
    
    while True:
        # State is defined as (position, direction)
        state = (guard_position, guard_direction)
        
        # Detect loop
        if state in visited_states:
            return True  # Guard is in a loop
        visited_states.add(state)
        current_path.add(guard_position)
        
        # Compute next position
        next_position = move_guard(guard_position, guard_direction)
        
        if next_position == obstruction_pos or (
            is_within_bounds(next_position) and lab_map[next_position[0]][next_position[1]] == '#'
        ):
            # Obstacle encountered: turn right
            guard_direction = (guard_direction + 1) % 4
        else:
            # Move forward
            guard_position = next_position
            if not is_within_bounds(guard_position):
                return False  # Guard exits the map

# Find all possible obstruction positions
possible_positions = set()
guard_path = set()

# Simulate the guard's initial movement and record the path
guard_position = None
guard_direction = None

# Reload the guard's starting position and direction
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in directions:
            guard_position = (r, c)
            guard_direction = directions.index(lab_map[r][c])
            break

visited_states = set()

while True:
    state = (guard_position, guard_direction)
    if state in visited_states:
        break
    visited_states.add(state)
    guard_path.add(guard_position)

    next_position = move_guard(guard_position, guard_direction)

    if is_within_bounds(next_position) and lab_map[next_position[0]][next_position[1]] == '#':
        # Obstacle encountered: turn right
        guard_direction = (guard_direction + 1) % 4
    else:
        # Move forward
        guard_position = next_position
        if not is_within_bounds(guard_position):
            break

# Test each position in the guard's path as a possible obstruction
for pos in guard_path:
    if pos != (guard_position):  # Exclude starting position
        if simulate_guard_with_obstruction(lab_map, pos):
            possible_positions.add(pos)

# Count the number of valid obstruction positions
print(len(possible_positions))
