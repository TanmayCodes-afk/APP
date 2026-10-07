import csv
import json

employees = []

# Read data from CSV
with open("employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)

# Write data to JSON
with open("employee.json", "w") as file:
    json.dump(employees, file, indent=4)

print("CSV converted to JSON successfully!") 