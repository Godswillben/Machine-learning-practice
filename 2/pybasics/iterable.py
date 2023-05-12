for item in (1,2,3,4,5):
    for x in ["a", "b", "c"]:
        print(1, 'c')

for _ in range(2):
    print(list(range(10)))

# iterables
for i,char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')

# While loops
i=0
while i < 50:
    print(i)
    i += 1
    break
else:
    print('done with all the work')

while True:
    response = input('say something!: ')
    if (response == 'bye'):
        break

# continue, pass, break
my_list = [1,2,3]
for item in my_list:
    # thinking about it
    pass

i=0

while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

