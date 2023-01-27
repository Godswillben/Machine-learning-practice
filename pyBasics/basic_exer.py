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
