# loop Through sets
Numbers = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4
}
#To print all the keys one by one
for y in Numbers:
    print(y)

# to print all the values one by one , there are two methods
#first usibg .values()
for x in Numbers.values():
    print(x)
# or by using print(Numbers[z])
for z in Numbers:
    print(Numbers[z])

# print all the keys and values together
for a,b in Numbers.items():
    print(a, b)
