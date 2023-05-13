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
