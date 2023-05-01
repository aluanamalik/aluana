from functools import reduce

lst = [1, 2, 3]


def multiply(numbers):
    return reduce((lambda x, y: x * y), numbers)


result = multiply(lst)
print(result)
