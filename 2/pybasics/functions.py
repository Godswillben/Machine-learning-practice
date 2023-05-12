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
