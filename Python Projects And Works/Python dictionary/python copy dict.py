# copy two dictionary
print("method 1 --- by using the built-in function ---- copy()")
A = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

B = A.copy()

print(A)

print(B)


print("method 2 -- by using dict() function")

C = dict(A)

print(C)
