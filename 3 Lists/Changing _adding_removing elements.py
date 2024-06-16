#Changin elements
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='dukati'
print(motorcycles)

#appending (Adding elemtns to the lists)
motorcycles.append('kawazaki')
print(motorcycles)

#dynamicaly adding
bikes=[]
bikes.append('honda')
bikes.append('harly davidson')
bikes.append('bmw')
print(bikes)

#adding elements to a specific index
motorcycles.insert(0,'dukati')
print(motorcycles)

#deleting elements
del motorcycles[0]
print(motorcycles)

#using an element which taken out of the list
popped_motorcycle=motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

print(f'last motorcycle I owned was a {popped_motorcycle.title()}')


