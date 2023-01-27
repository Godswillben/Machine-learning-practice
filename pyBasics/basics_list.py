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
