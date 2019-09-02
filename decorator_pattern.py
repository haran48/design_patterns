import time


def decorator_function(input_function):
    def wrapper_function():
        t1 = time.time()
        input_function()
        t2 = time.time()
        print("the difference is", t2 - t1)
    return wrapper_function()


@decorator_function
def simple_function():
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [n * 2 for n in list_data if n % 2 == 0]
    print("The even numbers from the list are ", even_numbers)