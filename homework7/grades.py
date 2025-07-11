filename = "grades.csv"
mode = "r"

grades = []

with open(filename, mode) as f:
    for line in f:
        grades.append(line.strip("\n").split(","))
print(grades)
