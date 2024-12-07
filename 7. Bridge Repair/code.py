from itertools import product

# Parse the input file
file_path = './7. Bridge Repair/input.txt'
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Function to evaluate expressions left-to-right
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    return result

# Initialize the total calibration result
total_calibration_result = 0

# Process each equation
for line in lines:
    # Parse the test value and numbers
    test_value, numbers = line.split(":")
    test_value = int(test_value.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Generate all possible operator combinations
    operator_combinations = product('+-*', repeat=len(numbers) - 1)
    
    # Check if any combination matches the test value
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            total_calibration_result += test_value
            break

print(total_calibration_result)

# ------------------------------------------------------------------

from functools import lru_cache

# Optimized function to evaluate combinations with memoization
def evaluate_with_memoization(numbers, target):
    n = len(numbers)
    
    @lru_cache(None)
    def dfs(index, current_value):
        # If we've processed all numbers, check if the value matches the target
        if index == n:
            return current_value == target
        
        result = False
        # Try all operators with the next number
        next_num = numbers[index]
        # Addition
        result |= dfs(index + 1, current_value + next_num)
        # Multiplication
        result |= dfs(index + 1, current_value * next_num)
        # Concatenation
        concatenated_value = int(str(current_value) + str(next_num))
        result |= dfs(index + 1, concatenated_value)
        
        return result

    # Start DFS from the first number
    return dfs(1, numbers[0])

# Reinitialize total calibration result
optimized_total_calibration_result = 0

# Process each line with optimized approach
for line in lines:
    # Parse the test value and numbers
    test_value, numbers = line.split(":")
    test_value = int(test_value.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Check if the target value can be achieved
    if evaluate_with_memoization(tuple(numbers), test_value):
        optimized_total_calibration_result += test_value

print(optimized_total_calibration_result)