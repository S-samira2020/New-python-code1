# Touple

'''dimension = (200, 50)
print(dimension[0])
print(dimension[1])
print()

# using for loop [ Touple ]

for names in dimension:
    print(names)
print()
'''

dimensions = (200, 50)
print('Original dimensions: ')
for dimension in dimensions:
    print(dimension)
print()

dimensions = (400, 100)
print('modified dimensions: ')
for dimension in dimensions:
    print(dimension)
print()

# 4.13
foods = ('drink', 'ice-cream', 'faluda', 'custard', 'sweets')
print('original menu: ')
for food  in foods:
    print(food)
print()

food = ('drink', 'faluda', 'custard', 'sweets', 'pastries')
print('one item modified menu:  ')
for food in foods:
    print(food)
print()

foods = ('drink', 'ice-cream', 'faluda', 'pastries', 'zera pani')
print('modified menu: ')
for food in foods:
    print(food)
print()

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


'''r_topping = ' mushrooms '

if r_topping  != ' cauliflower ':
    print("Hold the cauliflower!")
'''



#   checking wheather a value is not in list

b_users = [' carolina', ' andrew', ' david']
user = ' marie'

if user  not in b_users:
    print()
    print(user.title() + " , you can post a response if you wish.")


# 5.1

car  = 'subaru'
print(" Is car == 'subaru'? I pretic true.")
print(car == 'subaru')
print()
print("Is car == 'audi'? i predic false.")
print(car == 'audi')
print()


# 5.2

name  = 'samira'
print("no-1")
print(name  == 'samira')
print()
print("no-2")
print(name  == 'rifat')
print()
name  = 'sakiba'
print("no-3")
print(name == 'rifat')
print()
print("no-4")
print(name  == 'sakiba')
print()
name  = 'belayet'
print("no-5")
print(name == 'belayet')
print()
print("no-6")
print(name == 'rafee')
print()
name  = 'rafee'
print("no-7")
print(name  == 'rafee')
print()
print("no-8")
print(name  == 'rifat')
print()
name  = 'rifat'
print("no-9")
print(name  == 'rifat')
print()
print("no-10")
print(name == 'rafee')
print()


# 5.2

names  = ['samira', 'sakiba', 'babu']
for name in names:
    if name  == 'babu':
        print(name)

car  = 'Audi'
car == 'audi'   # it will be false coz value assigned upper case and comparison is lower case

car  = 'Audi'
car.lower() == 'audi'



