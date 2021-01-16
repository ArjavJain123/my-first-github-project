#python sets
"""set1 = {"watermelon", "banana", "cherry", "kiwi", 234, 45454}
print(set1)
print(type(set1))
print("banana" in set1)
if "cherry" and "banana" in set1:
    print("yes  , they are in the set 1")
else:
    print("no")
for x in set1:
    print(x*10)
set1.add("apple")
set1.add("banana")
set1.update(["apple", "guava", 123, 3646784])
print(set1)
#pytthon sests
print("pythoon sets are unindexed")
set1 = {"a", "b", "c", 7454875, 54325}
print(set1)
#remove removes only one item, and if the item doesn,t exist this will raise an error
set1.remove("a")
print(set1)
set1.update("a")
print(set1, ".set1 is added with a.")
del set1
print("set 1 doesnt exist now")
set2 = {"a", "arjav", 37478347, 4378578}
set2.clear()
#set1 is cleared
print(set2)
set2.add("apple")
set3 = {"arjav", "jain", 45643}
print(set3)
# discard will also remove only one item , but if the item does'nt exist it does'nt raise ny error
set3.discard("arjav") 
print(set3)
#pop will remove the last item but the set is unorded we will not know which item is removed!1
set4 = {"a", "b", 456874, 76457864}
print("set4 =", set4)
a = set4.pop()
print(a, "is removed from the set")
print(set4)
#joing two sets
print("1. joining two sets using union method")
b = {"aj", 44654}
c = {"arj", 4572}
d = b.union(c)
print(d)
"""
"""
#differnces of sets this will print the items that are only in the set x but not in the set y
x = {1, 2, 3, 4, 5, 6, 7, 8}
y = {1, 2, 3, 4, 5, 9, 10, 20,}
print("x is", x)
print("y is", y)
z = x.difference(y)
print("the differennce of x and y be ", z)
w = y.difference(x)
print("similarly the difference in y and x is", w)
"""
"""
# joing using [|] (unoin)
a1 = {"ak", 123, 456, 789, 3452}
a2 = {"aj", 124, 356, 789, 3451}
c1 = a1|a2
print(c1)
"""
"""
a1 = {"ak", 123, 456, 789, 3452}
a2 = {"aj", 124, 356, 789, 3451}
print("a1 is", a1)
print("a2 is", a2)
print(a1|a2)
"""
"""
#now difference_update removes the item that exist in the both the sets
print("now difference_update removes the item that exist in the both the sets and updates the set that is give in the starting")
x = {1, 2, 3, 4, 5, 6, 7, 8}
y = {1, 2, 3, 4, 5, 9, 10, 20,}
print("x is", x)
print("y is", y)
x.difference_update(y)
print("the x set is updated and the items in the both sets in common are removed from the set \nx =", x)
print(y)
"""
"""
# 'intrersection' of the sets returns a new set that have the items in both the sets in common
w1 = {"hibiscus", "rose", "lotus", "tulip", "sunflower"}
w2 = {"sunflower", "jasmine", "rose",}
print(w1)
print(w2)
y1 = w1.intersection(w2)
print(y1)
"""
"""
# intersection_update removes the item that is not present in all the sets compared
zw = {"hibiscus", "rose", "lotus", "tulip", "sunflower"}
yw = {"sunflower", "jasmine", "rose",}
xw = {"tree", "palm", "flower", "sunflower", "tulip"}

zw.intersection_update(xw, yw)

print(zw)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

"""
"""
# set isdisjoint method returns true if the sets doesn,t have something in common else it will print false
abc = {"apple", "banana", "mango"}
ab = {"papaya", "orange", "pineapple"}
xyz = abc.isdisjoint(ab)

print(xyz)

ace = {"python", "javascript", "html"}
dia = {"python", "django", "AI"}

clu = ace.isdisjoint(dia)

print(clu)
"""
# set method - issubset , if all the contents of the set specified is present in the set(s) in the brackets , it returns true , else it returns false
company = {"apple", "microsoft", "mi"}
brands = {"apple", "microsoft", "android", "mi"}

at = company.issubset(brands)

print(at)

fruits = {"banana", "orange", "mango", "guava"}
all = {"banana", "orange", "potato", "onion", "guava"}

iss = fruits.issubset(all)

print(iss)
