def show_tree(picture):
    for image in picture:
        for pixel in image:
            if(pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')

show_tree([0,1,0,1])

# parameters and arguments

# Parameters
def say_hello(name, emoji):
    print(f'hellooo {name} {emoji}')

# arguments || positional arguments
say_hello('Andrei', ":)`")
say_hello('Dan', ":)`")
say_hello('Emily', ":)`")

# keyword arguments
say_hello(emoji=":)`", name='bibi')

# Default parameters
def say_hello_default(name="Darth vader", emoji=":)"):
    print(f'helllooo {name} {emoji}')

say_hello_default()
say_hello_default("melly")

# Doc string
def test(a):
    # ways to documents what a function does
    # or funtion of a function (get it ;)
    '''
    Info: this function tests and prints a 
    '''
    print(a)

print(test.__doc__)

# Clean code
def is_even(num):
    return num % 2 == 0

print(is_even(50))

# *args **kwargs
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Andy', 1,2,3,4,5, num1=10, num2=5))

# Scope - what variables do I have access to? \
if True:
    x = 10

def some_func():
    total = 100
    
print(x)

# scope and it's rules
a=1

def parent():
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

#1 - start with local
#2 - Parent local?
#3 - Global
#4 - built in python functions.

# Non local
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)
    
    inner()
    print("outer:", x)

outer()

# pure functions
wizard = {
    'name': 'Merlin',
    'power': 50
}

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# map, filter, zip, and reduce
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))
