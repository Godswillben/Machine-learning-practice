is_old = False
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive!')
# elif is_licenced:
#     print('you can drive now!')
else:
    print('you are not of age!')

print('okoko')

# Truthy and falsy
password = '123'
username = 'johnny'

# Truthy and Falsy
if password and username:
    print('you are a user with the correct credentials')
else:
    print('you are not of age!')
    print('okoko')

# Ternary Operator

# condition_if_true if condition else condition_if_false
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# Short Circuiting
is_Friend = False
is_User = True

if is_Friend and is_User:
    print('best friends forever')
