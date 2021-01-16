"""
# python  if else
a = 34
b = 45
c = 34

if a >= b:
    print("a is greater tha b")
elif b > c:
    print("a b is greater than c")
else:
    print("hii")


# else statement without elif
if a>= b:
    print("a is greater than b")
else:
    print("a is equal to c")

#short hand if else,

print("yes a is 34 ") if a == 34 else print("no 34 is not 34")

# short hand if else with 3 conditions
print("b = 54") if b == 54 else print("b == 45") if b == 55 else print("b is not 54")


# logical operator 'and' in if else statement
#if both the statements are true

if b == 45 and c == 34:
    print("yes b = 45 and c = 34")
else:
    pass

# Logical operator 'or' in if else
# if one of the given given statements is true

if b == 54 or c == 34:
    print("yes both/one of the both conditions is true")
else:
    pass
"""
x = 10
y = 20
z = 30

if x > 50:
    print("x is above 5")
    if y > 15:
        print("y is above 15")
        if x = 10:
            print("yes x = 10")
            if y == 20:
                print(yes y = 20)
                if z == 30:
                    print("yes z = 30")
        else:
            pass
             
    else:
        print("y is not abaove 15")
else:
    print("no x is not above 50")
    if y > 15:
        print("y is above 15")
    else:
        print("y is not above 15")
