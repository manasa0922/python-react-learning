score = [10, 20, 30, 40]
print(score)

# modify
score[1] = 15
print(score)

#append
score.append(45)
print(score)

# add at specific position
score.insert(3,25)
print(score)

#remove
score.remove(40)
print(score)

#remove last item
score.pop()
print(score)
 
#length of list 
print(len(score))