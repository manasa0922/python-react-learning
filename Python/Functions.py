#function without parameter and return value

def greet():
    print("Hello, welcome!!")

greet()

#function with parameter

def say_hello(name, Class):
    print("My Name is:", name , "Class is :", Class)
say_hello("Manasa", "1st MCA")

#function with return value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)


#Calculate Total Marks
def calculate(marks):
    return sum(marks) 

marks = [90, 80, 78, 78]
total = calculate(marks)
print(total)

#calcualte the average

#Calculate Total Marks
def calculate(marks):
    return sum(marks) / len(marks) 

marks = [90, 80, 78, 78]
total = calculate(marks)
print(total)

#T ask 2 
# Create a function:
# Input: average
# Output: grade (A/B/C/Fail)

def avgGrade(marks):
    return sum(marks)/len(marks)
marks = [90, 80, 89, 70]
avg = avgGrade(marks)
print(avg)

if(avg > 80):
    print("Grade A")
elif(avg>60):
    print("Grade B")
elif(avg>45):
    print("Grade C")
else: 
    print("Fail")
