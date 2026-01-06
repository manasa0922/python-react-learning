s1 = int(input("enter the marks "))
s2 = int(input("enter the marks"))
s3 = int(input("enter the marks"))

total = s1+ s2 + s3
avg = total/3
print("total marks is ", total)
print("average marks is ", avg)

if s1 > s2:
    print("s1 marks is greater than s2")
else:
    print("s2 marks is greater than s1")

marks = 90
attendance = 79
if (marks>=40 and attendance >=75):
   print("eligible")
else:
    print("Not an Eligible") 
