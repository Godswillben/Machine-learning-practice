# Ternary Operator

# condition_if_true if condtion else condition_if_false
is_friend = False
can_message = "message allowed" if is_friend else "allowed to message"

print(can_message)

# Short Circuiting
is_friend = False
is_user = True

if is_friend and is_user:   # if first check results in true it jumps to conditonal body.
    print('best friends forever')

# is vs ==
print( True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([1,2,3,] == [1,2,3])


print( True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3,] is [1,2,3])
