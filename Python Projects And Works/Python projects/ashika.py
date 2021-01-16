score = 0
print("this si a test f")
b = input("what is your name   ")
# Q1
a = input("Ok ,Q1 == what do cows eat mainly  ")
if a == "grass" or a == "green grass" or a == "Grass":
    score+=1
    print(",yes you are correct", b)
else:
    print("no , the correct answer is grass or green grass")
# Q 2
c = input("what is your favorite food [ this q does not have marks]  ")
print("yes your favorite food is", c)
#q3
d = input("what is [2 + 2] X 4   ")
if d == "16":
    score+=1
    print("yes,you are correct", b)
else:
    print("no you are not correct")
print("your total score is ", score)
