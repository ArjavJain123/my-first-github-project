#differnces of sets this will print the items that are only in the set x but not in the set y
x = {1, 2, 3, 4, 5, 6, 7, 8}
y = {1, 2, 3, 4, 5, 9, 10, 20,}
print("x is", x)
print("y is", y)
z = x.difference(y)
print("the differennce of x and y be ", z)
w = y.difference(x)
print("similarly the difference in y and x is", w)
