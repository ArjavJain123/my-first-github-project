# set method - issubset , if all the contents of the set specified is present in the set(s) in the brackets , it returns true , else it returns false
company = {"apple", "microsoft", "mi"}
brands = {"apple", "microsoft", "android", "mi"}

at = company.issubset(brands)

print(at)

fruits = {"banana", "orange", "mango", "guava"}
al = {"banana", "orange", "potato", "onion", "guava"}

iss = fruits.issubset(al)

print(iss)
