counter = 0

while counter <= 3:
    print(counter)
    counter += 1
print('Final value for counter: ', counter)


one = 0

while one <= 99:
    one += 1
    print(one)
    
normal = 0

while normal <= 5:
    normal += 1
    print(normal)


while True:
    if counter > 3:
        print("The loop runs")
        break
    else:
        print(counter)
        counter += 1


# for loops

myCars = ['Toyota', 'Tesla', 'Ford', 'BMW', 'Jeep', 'Kia', 'Honda']

for car in myCars:
    print(car)

for index in range(0, len(myCars)):
    print(index, ' : ' + myCars[index])

for item in myCars:
    items += item + ' '
    print(items)