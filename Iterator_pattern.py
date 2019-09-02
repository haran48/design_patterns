#Iterables and Iterators
list_data = [1, 2, 3, 4, 5, 6, 7, 8]

# the __next__() method is called automatically
for element in list_data:
    print(element)

# explicitly calling the __next__() function
iter_check = list_data.__iter__()
print(iter_check)
val = iter_check.__next__()
print(val)
val = iter_check.__next__()
print(val)
val = iter_check.__next__()
print(val)

# List Comprehension
elements = [n for n in list_data]
print(elements)

# List Comprehensions including conditions
even_numbers = [n for n in list_data if n % 2 == 0]
print(even_numbers)

# List Transformations
even_numbers = [n * 2 for n in list_data if n % 2 == 0]
print(even_numbers)
