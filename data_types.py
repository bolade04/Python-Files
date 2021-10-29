# The numeric data types

print("2 + 2 =", 2+2)
print('4 - 2 =', 4-2)
print('2 * 2 =', 2*2)
print('4 / 2 =', 4/2)
print('4 % 2 =', 4%4)
print('4 / 2 =', int(4/2))

# Data and their typs
myVar = 1
print(myVar, 'is of data type', str(type(myVar)))
myVar = 3.14
print(myVar, "is of data type", str(type(myVar)))
myVar = 5j
print(myVar, 'is of data type', type(myVar))
myVar = True
print(myVar, 'is of data type', type(myVar))

# Assignment operators
myVar = 1
print(myVar)
myVar += 1
print(myVar)
myVar = myVar * 2
print(myVar)
myVar *= 2
print(myVar)
myVar -= 1
print(myVar)