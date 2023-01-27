amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[2])

# List slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix
matrix = [
    [1, 5, 1],
    [0, 1, 0],
    [1, 0, 1],
]

print(matrix[0][1])

basket = [1, 2, 3, 4, 5]

# list methods

# adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)

# insert
basket.insert(5, 100)
new_list = basket
print(basket)
print(new_list)

# adding
basket.extend([5, 100])
new_list = basket
print(basket)
print(new_list)

# removing
basket.pop()
basket.pop(0)
basket.remove(3)
basket.clear()
print(basket)
