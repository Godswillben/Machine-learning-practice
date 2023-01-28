# Dictionary
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
    'a':[1, 2,3],
    'b':'hello',
    'x': True
    },
    {
    'a':[4, 5, 6],
    'b':'hello',
    'x': True
    }
]

print(my_list[0]['a'][2])

print(dictionary['a'][1])

user = {
    'basket':[1,2,3],
    'greet': 'hello',
    'age':20
}

user2 = dict(name='JohnJohn')
print(user2)

# methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age':20
}

print('age' in user.keys())
print('hello' in user.values())
user.clear()
user.copy()
user2 = user.copy()
print(user.items())
# pop
print(user.pop('age'))
print(user.popitem('age'))
# update
print(user.update({'ages':55}))
print(user)
