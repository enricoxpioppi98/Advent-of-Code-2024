# Read the input data
file_path = "./4. Ceres Search//input.txt"
with open(file_path, "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Dimensions of the grid
rows, cols = len(grid), len(grid[0])

# The target word to search for
word = "XMAS"
word_length = len(word)

# Function to count occurrences of the word in the grid
def count_word_in_grid(grid, word):
    def check_direction(x, y, dx, dy):
        """Check for the word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    # All eight possible directions
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1),  # up-left
    ]

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1
    return count

# Count all occurrences of the word "XMAS"
total_count = count_word_in_grid(grid, word)
print(total_count)

# ------------------------------------------------------------------

# Refined function to count X-MAS patterns with MAS sequences forward and backward
def count_xmas_patterns_with_reversals(grid):
    count = 0

    # Iterate through all possible centers of the X
    for x in range(1, rows - 1):  # Skip the first and last rows
        for y in range(1, cols - 1):  # Skip the first and last columns
            # Check for X-MAS pattern with MAS in forward or reversed order
            if (
                (grid[x - 1][y - 1] == "M" and grid[x][y] == "A" and grid[x + 1][y + 1] == "S") or
                (grid[x - 1][y - 1] == "S" and grid[x][y] == "A" and grid[x + 1][y + 1] == "M")
            ) and (
                (grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S") or
                (grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M")
            ):
                count += 1

    return count

# Count X-MAS patterns with the clarified rules
final_xmas_count = count_xmas_patterns_with_reversals(grid)
print(final_xmas_count)