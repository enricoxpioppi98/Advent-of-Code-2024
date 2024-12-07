# Load the input file content
file_path = "./1. Historian Hysteria//input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

# Parse the two columns into separate lists
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Calculate the total distance by pairing and summing absolute differences
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print("Total Distance:", total_distance)

# ------------------------------------------------------------------

from collections import Counter

# Reload the file content and initialize lists
file_path = "./1. Historian Hysteria//input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Count occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculate the similarity score based on occurrences
similarity_score = sum(num * right_counts[num] for num in left_list)
print(f"Similarity Score: {similarity_score}")