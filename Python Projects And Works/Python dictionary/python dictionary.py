mydict = {
    "name" : "Arjav",
    "class" : 9,
    "age" : 14
}
print(mydict["name"])

# get key to acces the items in the dixtionary

mydict = {
    "name" : "Arjav",
    "class" : 9,
    "age" : 14
}

x = mydict.keys()

print(x)

mydict["school"] = "cia"

print(x)

y = mydict.values()

print(y)


mydict["residence"] = "Dewas"

print(y)

z = mydict.items()

print(z)

if "name" in mydict:
    print("yes")
