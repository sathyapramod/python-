bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])

# Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Changing, adding, and removing elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'splender')
print(motorcycles)

# removing an Item Using the del Statement
del motorcycles[0]
print(motorcycles)

# removing an Item by Value
motorcycles.remove('suzuki')
print(motorcycles)

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
#print(cars)
print(len(cars))