def find_person(people, name, age):
    i = 0

    while i < len(people):
        ppl = people[i]
        if ppl[0] == name and ppl[1] == age:
            return (i, (people[i]))
        i += 1

    return (-1, None)


people = [
    ('Alice', 32),  # one tuple
    ('Bob', 1),  # another tuple
    ('Carol', 15)
]  # `people` is a list of tuples

a = find_person(people, 'Alice', 32)  # (0, ('Alice', 32))
b = find_person(people, 'Carol', 15)  # (1, ('Bob', 51))
print(a)
print(b)