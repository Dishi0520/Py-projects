students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stab"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"],student["house"],student["patronus"], sep =", ")