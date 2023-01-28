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

# insert
basket = ['a', 'b', 'c', 'd', 'e']
basket.index('c')
print(basket in ('d'))
print('x' in basket)
print(basket.count('d'))

# sort 
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
print(basket)
# sorted method
print(sorted(basket)) # returns a sorted list
# copy
new_basket = basket.copy()
print(new_basket)
# reverse
basket.sort() # optional
basket.reverse()
print(basket)
# range
print(list(range(101)))
# join
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])

print(new_sentence)

# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9,]
print(a)
print(b)
print(c)
print(other)
print(d)
