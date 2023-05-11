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


