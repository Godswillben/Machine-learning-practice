for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)


# iterables
# iterable - list, dictionary, tuple, set, string
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for k, v in user.items():
    print(k, v)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# range
range()

for _ in range(2):
    print(list(range(10)))

# enumerate
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')
