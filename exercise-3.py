import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Define a regular expression pattern to extract name, age, occupation, and location
pattern = r"Name: (\w+\s\w+); Age: (\d+); Occupation: (\w+); Location: (\w+\s?\w*)"

# Use re.search to find the first match in the text
match = re.search(pattern, text)

# Extract information using capturing groups
if match:
    name = match.group(1)
    age = match.group(2)
    occupation = match.group(3)
    location = match.group(4)

    # Print extracted information
    print("Name:", name)
    print("Age:", age)
    print("Occupation:", occupation)
    print("Location:", location)
else:
    print("No match found.")
