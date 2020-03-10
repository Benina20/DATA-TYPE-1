cars= [56,78,34,21,56,34,125,45,89,75,12,56]
print(type(cars))
#the data type of the numbers represented
cars.sort()
print(cars)
#sorting the numbers in ascending order
print(cars[:1])
#to find the smallest number
print(max(cars))
#to print the largest number
print(sum(cars))
#to print the sum of all the numbers
cars = list(dict.fromkeys(cars))
#tho remove duplicates from the list
print(cars)
#to print out the list without duplicates
