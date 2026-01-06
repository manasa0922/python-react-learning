for i in range(3+1):
    print(i)

marks = [90, 89, 76, 89]
total = 0
for m  in marks:
    total = total + m
avg = total/len(marks)

print("toal marks:", total)
print("average mmarks is: ", avg)


t = 0
for s in range(4):
    score = int(input("enter the marks:"))
    t = t + score
print("total is: ", t)



#break 
for i in range(5):
    if i == 3:
        break
    print(i)
print("-----")

#continue
for i in range(5):
    if i == 2:
        continue
    print(i)


