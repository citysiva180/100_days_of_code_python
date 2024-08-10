from collections import OrderedDict, namedtuple, deque, ChainMap, Counter
# Collections Module!! :-)

# collections module has the following data structures for your usage


# namedtuple()
# A Named Tuple is a data structure in which you could customize
# your preference of data which is added to the tuple

# here is an example for the same


# Define a namedtuple called 'Person' with fields 'name', 'age', and 'city'
from collections import OrderedDict
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance of the namedtuple
person1 = Person(name='Alice', age=30, city='New York')

# Access the fields by name
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person1.city)  # Output: New York

# ---------------------------------------------------------------
# deque()


# Initialize a deque
d = deque([1, 2, 3, 4])

# Append elements
d.append(5)
d.appendleft(0)

# Pop elements
d.pop()        # Removes 5
d.popleft()    # Removes 0

# Rotate the deque
d.rotate(1)    # Moves all elements one step to the right

print(d)  # Output: deque([4, 1, 2, 3])
# ---------------------------------------------------------------
# Chainmap()

# The significance of ChainMap lies in its ability to
# manage multiple dictionaries as a single unit without merging them.
# This is particularly useful when you want to maintain the original
# dictionaries separately and access them collectively, with a

# specific order of precedence.


# Two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Combine them with ChainMap
combined = ChainMap(dict1, dict2)

print(combined['a'])  # Output: 1 (from dict1)
print(combined['b'])  # Output: 2 (from dict1, has priority)
print(combined['c'])  # Output: 4 (from dict2)

# Why Use ChainMap?
# Dynamic View: Changes in the underlying dictionaries are immediately
# reflected in the ChainMap.
# No Data Duplication: Unlike merging, ChainMap does not create a
# new dictionary, conserving memory.
# Flexible Precedence: You can easily reorder or add/remove dictionaries
# in the chain without altering the original data.
# ChainMap is ideal when you need to work with multiple dictionaries in
# a context where the precedence of keys is crucial, without actually merging the data.

# ---------------------------------------------------------------

# Counter()
# the counter returns a dictionary with the elements of a list in key

list_1 = [1, 2, 6, 4, 8, 5, 2, 1, 4, 5, 9, 7, 8, 4, 5, 6, 9, 2, 3, 6, 4, 1, 4]
output = Counter(list_1)
print(output)
# ---------------------------------------------------------------
# OrderedDict()
car_list = OrderedDict()

car_list['model'] = "S-Class"
car_list['brand'] = "mercedes"
car_list['year'] = 2024
car_list['color'] = 'gold'

print(car_list)

car_list.move_to_end('model')

print(car_list)

# The OrderedDict class in the collections module comes with several methods that allow you to interact with and manipulate the ordered dictionary. Here's a list of all the built-in functions (methods) available for an OrderedDict:

# 1. OrderedDict() Constructor
# Creates a new, empty OrderedDict.
# Can also take an iterable of key-value pairs or another dictionary to create an OrderedDict.
# 2. OrderedDict.clear()
# Removes all items from the OrderedDict, leaving it empty.
# 3. OrderedDict.copy()
# Returns a shallow copy of the OrderedDict.
# 4. OrderedDict.fromkeys(iterable, value=None)
# Creates a new OrderedDict with keys from the provided iterable and values set to value.
# This is a class method, so it's used as OrderedDict.fromkeys(...).
# 5. OrderedDict.get(key, default=None)
# Returns the value for key if key is in the dictionary, else default.
# 6. OrderedDict.items()
# Returns a new view of the dictionary's items (key-value pairs).
# 7. OrderedDict.keys()
# Returns a new view of the dictionary's keys.
# 8. OrderedDict.pop(key, default=None)
# Removes and returns the value for key if key is in the dictionary. If not, returns default if provided, otherwise raises a KeyError.
# 9. OrderedDict.popitem(last=True)
# Removes and returns the last (key, value) pair as a tuple if last is True (default), or the first pair if last is False.
# Raises KeyError if the OrderedDict is empty.
# 10. OrderedDict.setdefault(key, default=None)
# If key is in the dictionary, returns its value.
# If not, inserts key with a value of default and returns default.
# 11. OrderedDict.update([other])
# Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
# Existing keys are overwritten.
# 12. OrderedDict.values()
# Returns a new view of the dictionary's values.
# 13. OrderedDict.move_to_end(key, last=True)
# Moves an existing key to either the end (last=True) or the beginning (last=False) of the OrderedDict.
# 14. OrderedDict.__reversed__()
# Returns an iterator that yields the keys in reverse order.
# 15. OrderedDict.__eq__(other)
# Returns True if the OrderedDict is equal to other (i.e., they contain the same items in the same order).
# 16. OrderedDict.__delitem__(key)
# Removes the item with the given key from the dictionary. Equivalent to del ordered_dict[key].
# 17. OrderedDict.__getitem__(key)
# Returns the value associated with key. Equivalent to ordered_dict[key].
# 18. OrderedDict.__iter__()
# Returns an iterator over the keys of the dictionary.
# 19. OrderedDict.__len__()
# Returns the number of items in the OrderedDict. Equivalent to len(ordered_dict).
# 20. OrderedDict.__setitem__(key, value)
# Sets key to value in the dictionary. Equivalent to ordered_dict[key] = value.
# ------------------------------------------------------------------------
# defaultdict()
# ------------------------------------------------------------------------
# UserDict()
# ------------------------------------------------------------------------
# UserList()
# ------------------------------------------------------------------------
# UserString()
# ------------------------------------------------------------------------
