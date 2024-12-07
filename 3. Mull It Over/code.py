import re

# Load the file content
file_path = "./3. Mull It Over/input.txt"

with open(file_path, "r") as file:
    content = file.read()

# Regex pattern to find valid mul(x,y) instructions
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, content)

# Compute the sum of all valid multiplications
total_sum = sum(int(x) * int(y) for x, y in matches)
print("Part One Total Sum:", total_sum)

# ------------------------------------------------------------------

# Regex patterns for the instructions
mul_pattern = r"mul\((\d+),(\d+)\)"
control_pattern = r"(do\(\)|don't\(\))"

# Find all instructions (both mul and control)
instructions = re.findall(rf"{mul_pattern}|{control_pattern}", content)

# Track the current state (enabled/disabled for mul)
enabled = True
total_sum_part_two = 0

# Process instructions in order
for instr in instructions:
    if instr[2] == "do()":
        enabled = True
    elif instr[2] == "don't()":
        enabled = False
    elif instr[0] and instr[1]:  # Valid mul(x, y)
        if enabled:
            total_sum_part_two += int(instr[0]) * int(instr[1])

print("Part Two Total Sum:", total_sum_part_two)