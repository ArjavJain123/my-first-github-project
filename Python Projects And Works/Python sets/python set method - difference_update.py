#now difference_update removes the item that exist in the both the sets
print("now difference_update removes the item that exist in the both the sets and updates the set that is give in the starting")
x = {1, 2, 3, 4, 5, 6, 7, 8}
y = {1, 2, 3, 4, 5, 9, 10, 20,}
print("x is", x)
print("y is", y)
x.difference_update(y)
print("the x set is updated and the items in the both sets in common are removed from the set \nx =", x)
print(y)
