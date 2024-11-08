#1 Create a dictionary
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "A",
    "Eve": "B"
}
for key, value in grades.items():
    print(key + ": " + str(value))

#2 Accessing Values
student = {
    "name": "Alice",
    "age": 16,
    "grade": "A"
}

print(student.get("name"))
print(student.get("age"))

#3 Updating Values
student["grade"] = "A+"
for key, value in student.items():
    print(key + ": " + str(value))

#4 Adding New Key-Value Pairs
movies = {
    "Wizard of Oz": "1939",
    "Clueless": "1995",
    "The Devil Wears Prada": "2006"
}
newmovie = input("What is your favorite movie?\n>")
release = input("What year was it released?\n>")
movies[newmovie] = release

for key, value in movies.items():
    print(key + ": " + str(value))

