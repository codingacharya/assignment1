# List of student scores

scores = [85, 42, 78, 90, 56, 33, 67, 95, 48, 72]

total = 0
passed = 0
failed = 0

highest = scores[0]
lowest = scores[0]

print("Student Score Report")
print("-" * 25)

for score in scores:

    # Calculate total
    total += score

    # Find highest score
    if score > highest:
        highest = score

    # Find lowest score
    if score < lowest:
        lowest = score

    # Pass/Fail Count
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Grade Assignment
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Score:", score, "| Grade:", grade)

# Average Score
average = total / len(scores)

print("\nSummary Report")
print("-" * 25)
print("Average Score:", average)
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Highest Score:", highest)
print("Lowest Score:", lowest)