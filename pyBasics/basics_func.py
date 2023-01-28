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
