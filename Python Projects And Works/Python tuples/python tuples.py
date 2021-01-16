# title -- python tuples
a = (23 , "arjav" , "style" , 34 ,45 ,45)
print(a)
print(type(a))
print(a[0:3])
# as tuples are immutable , to change the values we need to change to list and then change
b = list(a)
b[3] = "jain"
a = tuple(b)
print(a)
# in
if 23 in a:
    print("yes 23 is there in this tuple")
# joining two tuples
x = [23, "hii" , 96 , "sst" , "etc."]
y = [1,]
z = x + y
print(z)


