# Open the input file
file = open("Age.py", "r")

# Read all lines
lines = file.readlines()

# Count number of lines
print("Number of rows:", len(lines))

# Extract two lines
line1 = lines[0]
line2 = lines[1]

file.close()

# Create a new file and write the two lines
new_file = open("output.txt", "w")

new_file.write(line1)
new_file.write(line2)

new_file.close()

print("Two lines copied to output.txt")


with open("output.txt", "r") as file:
    content = file.read()
    print(content)