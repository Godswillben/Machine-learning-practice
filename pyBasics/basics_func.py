picture= []

def show_tree():
    for image in picture:
        for pixel in  image:
            if (pixel):
                print('*', end = "")
            else:
                print(" ", end="")
        print('')
show_tree()

def say_hello():
    print("Helloooooo")

say_hello()

# paramerers and arguments
#parameters
def say_hell0(name, emoji):
    print(f'helloooooo {name} {emoji}')
# arguments
say_hell0("Andrei", ":)")
# postional arguments
say_hell0("Benny", ":)")
# keyword arguments
say_hell0(emoji=":(", name="philip")

# default Parameters
def say_hello2(name="Darth vader", emoji=":()"):
    print(f"hello {name} {emoji}")

# return parameter
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10, 20)
print(total)

# doc string
def test(a):
    '''
    Info: this function test and prints param a
    '''
    print(a)

print(test())

# clean code
def is_even(num):
    return num % 2 == 0

print(is_even(50))

# *args **kwargs
# *args
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))
# *kwargs
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs


# Scope - what variables do I have access to?\
if True:
    x = 10

def some_func():
    total = 100
    print(x)

# scope and dependecy injection
total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total))))

# scope non local
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()

# functional programming: pure functions
# function shoule take input and always return same output
# function not affect anything outside it's scope
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# map, filter, zip, and reduce functions
# map
my_list = [1,2, 3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list)

# filter
def only_odd(item):
    """
    returns true if odd else false
    """
    return item % 2 != 0
print(list(filter(only_odd, my_list)))

# zip
your_list = [10, 20, 30]
thier_list = (5,4, 3)
print(list(zip(my_list, your_list, thier_list)))
print(my_list)

# reduce
from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))
print(my_list)

# comprehensions
# list, set, and dictionary comprehensions
# list comprehensions
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0,100) if num % 2==0]

print(my_list4)

# set and dictionary comprehensions
my_list = {char for char in 'hello'} # set
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}

my_dict = {num:num*2 for num in [1, 2,3]}

print(my_dict)

