i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print('done with all the work')

#when to use while: when you don't know end of iteration
while True:
    response = input('say something: ')
    if (response == "bye"):
        break

