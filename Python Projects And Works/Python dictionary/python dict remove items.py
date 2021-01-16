#python dictionary remove the items
#pop method - removes the item with the specified key
tinydict = {
    "company" : "Maruti",
    "Car" : "Baleno",
    "Model" : "vxi",
    "year" : 2018
}

print(tinydict)

tinydict.pop("Model")

print(tinydict)

# the popitem method removes the last item [in the versions above 3.7] and in the versions before 3.7 it removes any random item

x = tinydict.popitem()
print(x, "is removed from the dictionary")
print(tinydict)

# del keyword removes the item specified - del dict[key]
# it can also delete the full dictionary if the tem is not specified - del dict

mydict = {
    "Country" : "India",
    "State" : "MP",
    "City" : "Dewas",
    "Pincode" : 455001
}
print(mydict)

del mydict["Pincode"]
print(mydict)

# the clear method empties the dictionary but not deletes it so this will not cause any error

note = {
    "Name" : "Bill Gates",
    "Company" : "Microsoft"
}
print(note)

note.clear()

print(note)
