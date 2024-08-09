# in this code snippet library,
# we will be discussing on the common code encounters where
# we feel stuck or need an api to be implemented to do some operations
# by using these code snippets and technique we should be able to
# cross through the bottle neck situation through any technical interview


# in this section we will be dealing with
# Collections and itertools
# Alternatives to nested loops
# While loops
# List operations on subtraction, finding duplicates and other list operations
# Such as merging, removing and adding elements and mapping list with lambda functions etc
# functools
# python ranking method
# List comprehension for


# import code snippets and libraries

from functools import reduce
import functools

# ------------------------------------------------------------------


def my_decorator(func):
    # This actually helps to preserve the doc string and the other details of the function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")


say_hello()
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: This function says hello.

# ------------------------------------------------------------------
# the functools.cache helps in caching the code for faster run


@functools.cache  # Super useful decorator. Using this we should be able to reduce the space complexity of
def factorial(n):   # O(n) algorithms to some extend
    return n * factorial(n-1) if n else 1


# Usage
print(factorial(10))  # Computes and caches results
print(factorial(5))   # Retrieves result from cache
print(factorial(12))  # Computes only necessary calls
# -------------------------------------------------------------------

# Functools.Partial - Not finding a lot of use case for daily use.
# helps you to simplify function to pass some parameter


def example_function(a, b, c, d):
    return a + b + c + d


# Create a new function where a and b are fixed
new_function = functools.partial(example_function, 1, 2)

print(new_function(3, 4))  # Output: 10

# -------------------------------------------------------------------

# LRU cache which is Last Reused Cache
# The LRU cache helps in caching the code so it could re-use the last cache it built
# you can parameterize it by setting max size on this!


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Usage
print(fibonacci(50))

# -------------------------------------------------------------------

# Example: Calculate the factorial of a number
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120

result = reduce(lambda x, y: x+y, numbers)
print(result)

# -------------------------------------------------------------------


@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


# Usage
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1 > p2)  # True, because 30 > 25
print(p1 <= p2)  # False, because 30 is not less than or equal to 25
print(p1 == p2)  # False, because 30 is not equal to 25


print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

# -----------------------------------------------------------------

# important iterables
# enumerate
# map
# zip
# reduce


# Example for Map In Python

# List of temperatures in Celsius
celsius_temps = [0, 20, 30, 40]

# Function to convert Celsius to Fahrenheit


def to_fahrenheit(c):
    return (c * 9/5) + 32


# Use map to apply the function
fahrenheit_temps = list(map(to_fahrenheit, celsius_temps))

print(fahrenheit_temps)  # Output: [32.0, 68.0, 86.0, 104.0]

# with map we are able to apply some operations on the list
# ------------------------------------------------------------
# Zip helps in zipping 2 lists together

countries = ['France', 'Germany', 'Italy']
capitals = ['Paris', 'Berlin', 'Rome']

country_capital_dict = dict(zip(countries, capitals))

print(country_capital_dict)
# Output: {'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome'}

# Remember - zip returns a dictionary!!
# ------------------------------------------------------------


def enumerate_generator(iterable):
    for index, value in enumerate(iterable):  # Enumerate generates
        yield index, value


gen = enumerate_generator(['apple', 'banana', 'cherry'])

for index, word in gen:
    print(index, word)

# Output:
# 0 apple
# 1 banana
# 2 cherry

# Enuemerate helps you to create a hashmap automatically! Hashmaps are
# super useful to identify records on index basis

# remember Enumerate pauses the function while
# return terminates the function. Using Enumerate
# might help in higher performance as the function is turned on
# and off again and again

output = enumerate(['apple', 'banana', 'cherry'])

# to create a iterable you could use the enumerate function

# ------------------------------------------------------------
