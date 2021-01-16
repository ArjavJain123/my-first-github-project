# nested idctionary means a dictionary the contains multiple dictionaries
A = {
    "name" : "a",
    "year" : 2000
}
B = {
    "name" : "b",
    "year" : 2001
}
C = {
    "name" : "c",
    "year" : 2002
}
D  = {
    "name" : "d",
    "year" : 2003
}
nesteddict = {
    "dict1" : A,
    "dict2" : B,
    "dict3" : C,
    "dict4" : D
}
for x,y in nesteddict.items():
    print(x,y)
