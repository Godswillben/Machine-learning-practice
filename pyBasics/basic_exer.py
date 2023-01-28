# python basics part one: excersice
birth_year = input('what year were you born?')

age = 2019 - int(birth_year)

print(f'your age is: {age}')

# python basics part one: excersice
username = input('what is your username?')
password = input('what is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} characters long')

# teneray and coditions
is_magician = False
is_expert = True

# chek if magician AND expert: you are master magician
if is_expert and is_magician:
    print("you are master magician")

# check if magician but not expert:"at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")

# counter
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for item in my_list:
    counter = counter + item
print(counter)

# GUI
picture = [
    [0, 0, 0, 1, 0,0, 0],
    [0, 0, 1, 1, 1,0, 0],
    [0, 1, 1, 1, 1,1, 0],
    [1, 1, 1, 1, 1,1, 1],
    [0, 0, 0, 1, 0,0, 0],
    [0, 0, 0, 1, 0,0, 0],
]

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(" ", end='')

    print('')

# Exercise: check for duplicate
some_list = ["a", "b", "c", "b", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
        
print(duplicates)

# highest even
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))


# duplicates using comprehensions

some_list = ['a', 'b', 'c', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)
