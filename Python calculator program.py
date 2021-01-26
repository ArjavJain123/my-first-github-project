def add():
    try:
        add1 = input("enter the first number to add\n")
        print("you have entered ", add1)
        add2 = input("enter the second number to add\n")
        print("you have entered ", add2)
    except:
        print("please enter numberes only")
        add()
    try:
        addr = (int(add1) + int(add2))
        print("\n\n\nyour answer is ", addr, "\n\n")
    except:
        print("\n\n\nplease enter numbers only\n\n\n")
        home()
    print("Thanks for using tihs calculator , will you try once again!")
    print(home())
def sub():
        sub1 = input("enter the first number to subtract\n")
        print("you have entered ", sub1)
        sub2 = input("enter the number to be subtracted\n")
        print("\nyou have entered ", sub2)
        try:
            subr = int(sub1) - int(sub2)
            print("\n\nyour answer is ", subr, "\n\n")
        except:
            print("\n\n\nplease enter numbers only")
        print("Thanks for using tihs calculator , will you try once again!")
        home()
def multiplication():
    mul1 = input("enter the first numnber to be multiplied\n")
    print("you have entered ", mul1)
    mul2 = input("plese enter the second number\n")
    print("you have entered ", mul2)
    try:
        mulr = int(mul1) * int(mul2)
        print("\n\nyour answer is ", mulr, "\n\n")
    except:
        print("\n\nplease enter numbers only")
    print("Thanks for using tihs calculator , will you try once again!")
    home()
def division():
    div1 = input("please enter the dividend\n")
    print("you have enetered ", div1)
    div2 = input("please enter the divisor\n")
    print("you have entered ", div2)
    try:
        divr = int(div1) / int(div2)
        print("\n\nyour answer is ", divr, "\n\n")
    except:
        print("please enter numbers only")
    print("Thanks for using tihs calculator , will you try once again!")
    home()
def floor():
    print("this is floor division , here you wil only get the qoutient")
    floor1 = input("please enter the divisor\n")
    print("you have entered ", floor1)
    floor2 = input("plase enter the dividend\n")
    print("you have entered ", floor2)
    try:
        floorr = float(floor1) // float(floor2)
        print("your answer is ", floorr)
    except:
        print("please enter numbers only")
     home()
def square():
    try:
        square1 = input("type the number to be squared\n")
        result = float(square1)**2
        print("The square of ", square1, "is ", result, "\n\n\n")
    except:
        print("please enter numbers only")
    print("Thanks for using tihs calculator , will you try once again!")
    home()
def sqrt():
    try:
        sqrt1 = input("enter the number to be under-rooted\n")
        sqrtr = float(sqrt1)**0.5
        print("The square root of ", sqrt1, "is ", sqrtr, "\n\n\n")
    except:
        print("please enter numbers only")
    print("Thanks for using tihs calculator , will you try once again!")
    home()
def home():
    print("this is my python caclculator\nplease choose any one of these options--\n[a] addition\n[b] subtraction\n[c]multiplication\n[d]division\n[e]floor division\n[f] square of a number\n[g] square root of a number\n[h]exit\n\n\n")
    b = input("please select anyone of these options\n")
    if b == 'a' or b == 'A':
        print(add())
    elif b == 'b' or b == 'B':
        sub()
    elif b == 'c' or b == 'C':
        multiplication()
    elif b == 'd' or b == 'D':
        division()
    elif b == 'e' or b == 'E':
        floor()
    elif b == 'f' or b == 'F':
        square()
    elif b == 'g' or b == 'G':
        sqrt()
    elif b == 'h' or b == 'H':
        exit()
    else:
        print("please select anyone one of this options")
        home()
print(home())


    
        
