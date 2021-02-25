#  read file
input = open("sol.txt", "r")

data = input.readline()
print(type(data))
print(data)

data_array = data.split()

time = data_array[0]
print(time + ' ' + 'seconds')

intersection = data_array[1]
print(intersection + ' ' + 'intersections')

streets = data_array[2]
print(streets + ' ' + 'streets')

cars = data_array[3]
print(cars + ' ' + 'cars')

points = data_array[4]
print(points + ' ' + 'points for completing')

# print(data_array)
# length = len(data)


