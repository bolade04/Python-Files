# This program reads in a csv file with data on vehicles


# Here is where you import needed modules for our program
import csv
import copy

# Defining the vehicle dictionary.
myVehicle = {'vin':'<empty>', 'make':'<empty>', 'model':'<empty>', 'year':0,
'range':0, 'topSpeed':0, 'zeroSity':0.0, 'mileage':0}

for key, value in myVehicle:
    print('{} : {}'.format(key, value))

myInventoryList = []
with open('Data_Files\car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {"," .join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make : {row[1]}, model: {row[2]}, year: r{ow[3]}, ')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle['vin'] = row[0]
            currentVehicle['make'] = row[1]
            currentVehicle['model'] = row[2]
            currentVehicle['year'] = row[3]
            currentVehicle['range'] = row[4]
            currentVehicle['topSpeed'] = row[5]
            currentVehicle['zeroSixty'] = row[6]
            currentVehicle['mileage'] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Proccessed {lineCount} lines.')


currentVehicle = copy.deepcopy(myVehicle)
for key, value in currentVehicle.items():
    print(f'{key} : {value}')

print('-----')

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print('{} : {}'.format(key, value))
    print('-----')