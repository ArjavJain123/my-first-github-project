### python functions
##
##def myfunc():
##    a = input("what is 1 + 2")
##    print("this is correct ") if a == 3 else print("no the correct answer is 3")
##    exit
##myfunc()
##
###function

# function arguments
##def my(arg):
##    print(arg + "is a good boy")
##my("arjav ")
# no. of arguments
##def argfun(*arg):
##    print(arg[1] + " is good")
##argfun("ashika" , "arjav")


def choice():
    a = input("Who is best - Arjav (a) or Ashika (b)  ")
    if a == 'a':
        print("no ashika  is best")
    elif a == 'b':
        print("yes ashika is the best")
    else:
        choice()
choice()
    
