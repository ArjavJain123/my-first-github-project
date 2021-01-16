"""
# python loops
print("python has two major loops:\n1.)while loop\n2.)for loop")
print("\n\n\n\while loop is the loop, in which the command in the loop repeats till the condition becomes true")
"""
i = 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

while i == 6:
    i += 1
    print(i)
    if i == 5:
        i += 2
        print(i)
    else:
        continue

"""
a = "bananas"
lists = {"a" , "s"}
while a == "bananas":
    print(a)
"""

#for loop in string
a = "bananas"
for x in "bananas":
    print(x)
# for loop in list
a = list(("a" , "b", "c", "d", "e", "f" ))
for z in a:
    print(z)

# for loop in set

b = {"aa", "bb", "cc"}
print(type(b))
print(type(b))
for k in b:
    print(k)

# for loop in dictionary

p = {
    "key" : "value",
    "one" : 1,
    "two" : 2,
    "three" : 3
}
for x,y in p.items():
    print(x, y)

#for loop in tuples

q = ("x", "y", "z")
print(type(q))

for r in q:
    print(r)
