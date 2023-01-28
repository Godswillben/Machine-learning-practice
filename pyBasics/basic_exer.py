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
