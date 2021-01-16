score =0
a = input("what is your name  ")
print("ok", a ,"""
this is a meanings test of 10 marks
each q will have 1 marks -- total 10 questions
""")
#q1
b = input("\nQuestion1.) excited:\na.) nearby \nb.) hold\nc.) eager\n Answer:  ")
if b =="eager" or b == "c":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is c - eager")          
#q2
c = input("\nQuestion2.) surrounded:\na.) nearby \nb.) hold\nc.) eager\n Answer:  ")
if c =="nearby" or c == "a":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is a--nearby")
#q3
d = input("\nQuestion3.) breeze:\na.) gaze\nb.)surround\nc.)gentle wind\n Answer:  ")
if d =="gentle" or d == "c":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is c - gentle wind")
#q4
e = input("\nQuestion4 examine:\na.)happy\nb.)study\nc.)exam\nAnswer:  ")
if e =="study" or e == "b":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is c -study")
#q5
f = input("\nQuestion5.) afraid:\na.)scared\nshy\nstop\nAnswer:  ")
if f =="scared" or f == "a":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is a--scared")
#q6
g = input("\nQuestion6.) shocked:\na.)surprised and sad \nb.)sad\nc.)shock\n Answer:  ")
if g =="surprised and sad" or g == "a":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is a--surprised and sad")
#q7
h = input("\nQuestion7.) pretend:\na.)hide \nb.)act like someone\nc.)clean\n Answer:  ")
if h =="act like someone" or h == "b":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is b--act like someone")
#q8
x = input("\nquestion8.) wipe:\na.)to clean\nb.)hold\nc.)dirt\n Answer:  ")
if x =="to clean" or x == "a":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is a--to clean")
#q9
y = input("\nQuestion9.) marmalade:\na.)james \nb.)jam\nc.)jame\n Answer:  ")
if y =="jam" or y == "b":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is b--jam")
#q10
z = input("\nQuestion10.) plenty:\na.)many\nb.) hold\nc.) eager\n Answer:  ")
if z =="a" or z == "many":
          score+=1
          print("yes", a, "you are correct")
else:
          print("no the correct answer is a--many")
print(a, "you got", score, "/10")

