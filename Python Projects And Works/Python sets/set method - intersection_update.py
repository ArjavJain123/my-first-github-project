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
