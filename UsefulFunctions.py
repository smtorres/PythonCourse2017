### SOME USEFUL FUNCTIONS TO KEEP IN MIND


# Enumerate:
# Syntax: enumerate(list)
# Application:

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

my_list2 = list(enumerate(my_list))
print my_list2

new_list = []
for c, value in enumerate(my_list, 1):
	new_list.append([c,value])


# Map:
# Syntax: map(function_to_apply, list_of_inputs)
# Application: square each element of the following list

items = [1, 2, 3, 4, 5]
mylist = []
for i in items:
	mylist.append(i**2)
mylist


squared = list(map(lambda x: x**2, items))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Filter:
# Syntax: map(condition_to_apply, list_of_inputs)
# Application:filter elements in a list that are less than zero
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Reduce
# Syntax: filter(function_to_apply, list_of_inputs)
# Application: get the product of the numbers in a list
# Check the import!

product = 1
mylist = [1, 2, 3, 4]
for num in mylist:
    product = product * num

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
product = reduce((lambda x, y: x**2 + y**2), [1, 2, 3, 4])



