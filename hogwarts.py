"""
students = ["Hermione", "Harry", "Ron"]

# List base line
print(students[0])
print(students[1])
print(students[2])

#Iterating
for student in students:
    print(student)

# Using len and range
for i in range(len(students)):
    print(i + 1, students[i], sep = ".- ")

# Using dict
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
}
#for student in students: # just to print the values, but not the keys
#    print(students[student])
for student in students: # print the keys and values separated by commas
    print(student, students[student], sep=", ")
"""
# And now a list with more than two values
students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print(student["name"], student["patronus"], sep = ", ")
