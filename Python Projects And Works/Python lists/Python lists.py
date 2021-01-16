# python lists
a = ['arjav' , 'is' , ' the best' , 123 , 34 , 423]
print(a)
'''
#replaces an item by indexing
a[0] = "Arjav"
print(a)
'''
'''
# in funstion in python list
print("yes arjav is in the list") if 'arjav' in a else print("arjav is not in the list")
'''
'''
# append , extend [add or remove] and instert and remove
a.append("in the world") # append is to add an object in the list
print(a)
'''
'''
# insert is to add an object to a specific place or index
b = ["arjav"," is ","a","boy"]
print(b)
b.insert(3, "good")
print(b)
'''
'''
#remove item
c = ["maths" , "arjav" , "chemistry" , "social" , "eco" , "physics" , "123"]
print("c=", (c))
c.pop(1) # removing using pop() it removes specific index or last index if not specified
print(c)
del c[5] # del only deletes the specific index or the whole list
print(c)
'''
'''#empting a list
d = [23 , 23 , 56 , 567 , 8667]
print(d)
d.clear()
print(d)
'''
'''#copy a list
x = [34,45,67,23,34,45,54]
y = x.copy()#copeid using copy() function
print(x)
print(y)
z = list(x)#using copy method
print(z)
'''
'''
#joing two lists
list1 = [34,45,23,67,78]
list2 = [1,2,3,4,5,6,7,8,9,]
list1.append(list2)
print(list1)
'''
'''
#but the append method is not joing them as a whole list
#using extend
l1 = [23 , 24]
l2 = [25,26]
l1.extend(l2)
print(l1)
'''
a = input('hi')

