x=True
y=False
z=True
print((x and y) or (x and z))
print((x or not y)and(not x or z))
print(x or y and z)
print(not(x or y) and z)
print(x or y or x and not z and not y)
print(not x or not y or z and x and not y)
