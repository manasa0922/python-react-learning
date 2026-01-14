# file create and write
file  = open("students.txt", "w")
file.write("Manasa,Manasa, 90,80, 90\n")
file.write("Kavya,MSc, 80,90, 100\n")
file.close()

#append dat ato existing file
file  = open("students.txt", "a")
file.write("Megha,MSc, 80,90, 100\n")
file.close()

#Print data
file = open("students.txt", "r")
data = file.read()
print(data)
file.close()
