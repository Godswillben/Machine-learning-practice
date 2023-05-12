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
def say_hello(name, emoji):
    print(f'hellooo {name} {emoji}')

# arguments
say_hello('Andrei', ":)`")
say_hello('Dan', ":)`")
say_hello('Emily', ":)`")
