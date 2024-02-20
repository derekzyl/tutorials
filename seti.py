name = {"kia", "volvo","toyota" }
name2 = {"tesla", "nissan","toyota" }
name.add("ford")

c = name.union(name2)
d = name.intersection(name2)
e = name.difference(name2)
e = name - name2

print(e)