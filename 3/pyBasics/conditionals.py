is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you is old for driver lincense')
elif is_old: 
    print('you is not have licence')
else:
    print('you are not of age')

# Ternary operator
is_friend = False
can_message = "message allowed" if is_friend else "allowed to message"
print(can_message)

for item in (1,2,3,4):
    print(item)
    print(item)


i=0
while i < 50:
    print(i)
    i  += 1
    break
else:
    print('err')

# function
def say_hello():
    print('hellooooo')

say_hello()

# default parameters
def sayy_hello(name='dart vader'):
    print(f'hello, {name}')

#kew word arguments
say_hello(name="meememn")
