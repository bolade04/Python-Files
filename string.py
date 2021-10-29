# The string data type
myStr = 'This is a String'
print(myStr, '\n', type(myStr))
print(myStr + '...', "it's of data type", type(myStr))

# String concatenation
str1, str2 = 'water', 'fall'
str3 = str1 + str2
print(str3)

# Input string
name = input('What is your name? ')
print(name)

# Format output string
color = input('What is your favorite color? ')
animal = input('What is your favorite animal? ')
print('{}, you like a {} {}!' .format(name, color, animal))
print(f'{name}, you like a {color} {animal}.')

# Exceptions
# print(name + 3)
print(name + ' ' + str(3))