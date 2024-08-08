
# Given an array containing only 0’s, 1’s, and 2’s,
# sort it in linear time and using constant space.


# my solution!
from collections import Counter


def sort_012_list(arr):
    new_list = []
    output = Counter(arr)
    for key, value in output.items():
        for items in range(value):
            new_list.append(key)
    return (new_list)


arr = [0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0]
sort_012_list(arr)

# GPT Solution!
# understanding - Instead of using APIs to create a new array with values,
# we could actually shift the values inside the list to get the relevant array


def sort_012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


# Example usage
arr = [0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0]
sorted_arr = sort_012(arr)
print(sorted_arr)
