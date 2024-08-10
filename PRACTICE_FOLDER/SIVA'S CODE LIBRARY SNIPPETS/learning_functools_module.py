
import functools
from functools import reduce

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


# Explanation
# __eq__ Method:         You must still define the __eq__ method, which checks if two Person objects are equal based on age.
# One Comparison Method: You only need to define one of the other comparison methods, such as __lt__.
# Automatic Generation:  @functools.total_ordering automatically generates the other comparison methods (__le__, __gt__, __ge__) based on the methods you define.
