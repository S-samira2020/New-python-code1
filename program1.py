#4.1
'''pizzas = ['dominos', 'pizza hut', 'off beat']
for pizza in pizzas:
    print()
    print(pizza)
    print('i like peporoni pizza')
print()
print('i really love pizza')
'''

# 4.2
'''
animals  = ['tiger', 'lion', 'tortouis']
for name in animals:
    print(name)
    print('a dog is a great pet')
print()
print('any of these animals would make a great pet\n')
'''

# range of function
for numbers in range(1,10):
    print(numbers)

# list of numbers using range function
print()
numbers = list(range(1,10))
print(numbers)

# even numbers using range()
print()
even_numbers = list(range(2,11,2))
print(even_numbers)

# odd numbers using range ()
print()
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

# square
squares = []
for numbers in range(1,10):
    square = numbers**2
    squares.append(square)
print(squares)
#squares = [value**2 for value in range(1,11)]
#print(squares)
# 4.3
for numbers in range(1,21):
    print(numbers)
print()
# 4.4
numbers = list(range(1,10000000))
print(numbers)
print()
# 4.5
numbers = list(range(1,10000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()
# 4.6
for numbers in range(1,21,2):
    print(numbers)
print()
# 4.7
for numbers in range(3,31,3):
    print(numbers)
print()
# 4.8
cubes = []
for numbers in range(1,11):
    cube = numbers ** 3
    cubes.append(cube)
for cube in cubes:
    print(cube)
print()
# 4.9
cubes = [numbers ** 3 for numbers in range(1,11)]
print(cubes)
# slicing a list
actors = ['shilpa', 'ranvir', 'shahir', 'karan', 'adha', 'santosh']
print(actors[0:3])
print()
print(actors[1:4])
print()
print(actors[:4])
print()
print(actors[2:])
print()
print(actors[-3:])
print()
for actor in actors[:3]:
    print(actor)
print()
for actor in actors[-3:]:
    print(actor)
print()

#copying a list
my_food = ['rice', 'chicken', 'vegetable']
my_ffood = my_food[0:]
print('My favourite food is here: ')
print(my_food)
print()
print('my friend favourite food: ')
print(my_ffood)
print()
my_food.append('drink')
my_ffood.append('ice cream')
print('my favorite food is: ')
print(my_food)
print()
print('my friends favourite food is: ')
print(my_ffood)
print()
# 4.10
list = ['pencil', 'eraser', 'pen', 'khata', 'notebook', 'books', 'bag']

print(list[0:3]) # show 1st 3 items
print()

print(list[2:5]) # show middle 3 items
print()

print(list[4:]) # show last 3 items
print()
# 4.11
my_pizza = ['pizza hut', 'pizza burg', 'dominos', 'pizza burger']
my_fpizza = my_pizza[:]

print('here are my pizza list: ')
print(my_pizza)
print()

print('here are my friends pizza list: ')
print(my_fpizza)
print()

my_pizza.append('pizza bug')
my_fpizza.append('pizza king')

print('here are the new different list of my pizza: ')
print(my_pizza)
print()

print('here are the new different list of friend pizza: ')
print(my_fpizza)
print()

print('new list: ')
for pizza in my_pizza:
    print(pizza)
print()

for pizza in my_fpizza:
    print(pizza)
print()
