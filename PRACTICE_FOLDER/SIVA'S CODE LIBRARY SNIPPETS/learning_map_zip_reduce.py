from functools import reduce
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

# --------------------------------------------------------------

# Remember you can use the reduce function only from functools module 


# Example: Calculate the factorial of a number
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120

result = reduce(lambda x, y: x+y, numbers)
print(result)
