student = {
    "name" : "Manasa",
    "age"  : 23,
    "grade" : 'A'
}

print(student)
print(student["age"])

print("--------")

#modify 
student["age"] = 24
print(student)
print("--------")

# add new key value
student["class"] = "MCA"
print(student)
print("--------")

#removing items
student.pop("age")
print(student)
print("--------")

#Looping Through Dictionary
for value in student.values():
    print(value)
print("--------")

#Looping through dictionary(keys)
for key in student.keys():
    print(key)
print("--------")


students = [
    {"name": "Ravi", "marks": 80},
    {"name": "Anu", "marks": 90},
    {"name": "John", "marks": 75}
]

print(students)

print("--------")
#Dictionaries with list

Students = [
    {"name" : "Manasa", "class" : "1st Mca", "Marks" :[90, 80, 87], "Percentage": 79},
    {"name" : "Kavya" , "class" : "2nd Mca", "Marks" :[90, 90, 87], "Percentage" : 80}
]
print(Students)
for s in Students:
    print("Name:", s["name"])
    print("Total Mraks:", sum(s["Marks"]))     #can calculate and store in varible also
    print("Percentage: ", s["Percentage"])
