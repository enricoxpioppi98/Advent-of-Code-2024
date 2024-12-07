# Function to determine if a report is safe
def is_safe_report(report):
    # Calculate differences between adjacent levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are between 1 and 3 (inclusive) or -1 and -3 (inclusive)
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

# Read the input data
file_path = "./2. Red-Nosed Reports/input.txt"
with open(file_path, "r") as file:
    reports = file.readlines()

# Parse reports and count the number of safe ones
safe_count = 0
for report in reports:
    levels = list(map(int, report.split()))
    if is_safe_report(levels):
        safe_count += 1

print(safe_count)

# ------------------------------------------------------------------

# Function to determine if a report is safe with or without the Problem Dampener
def is_safe_with_dampener(report):
    # Check if the report is already safe
    if is_safe_report(report):
        return True

    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True

    return False

# Count the number of safe reports considering the Problem Dampener
safe_count_with_dampener = 0
for report in reports:
    levels = list(map(int, report.split()))
    if is_safe_with_dampener(levels):
        safe_count_with_dampener += 1

print(safe_count_with_dampener)
