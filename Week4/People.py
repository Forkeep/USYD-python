people = [
    ('Alice', 32),  # one tuple
    ('Bob', 51),  # another tuple
    ('Carol', 15),
    ('Dylan', 5),
    ('Erin', 25),
    ('Frank', 48)
]  # `people` is a list of tuples

# Finish this program, so that it loops through the list of tuples, and
# prints "Youngest person: Dylan, 5 years old."

i = 0
min_age = 0
while i < len(people):
    if people[i][1] < people[min_age][1]:
        min_age = i
    i += 1
print(people[min_age])