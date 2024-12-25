students = []

with open('names.csv') as file:
    for line in file:
        name, age = line.rstrip().split(",")
        # students.append({'name': name, 'age':age})
        students.append({name, age})

print(students[0])