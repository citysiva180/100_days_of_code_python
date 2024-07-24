# Given a limited range array of size n containing elements between 1 and n-1 with one element repeating,
# find the duplicate number in it without using any extra space.

# Input:  { 1, 2, 3, 4, 4 }
# Output: The duplicate element is 4

from collections import Counter


def get_duplicate_values(input_array):
    output = Counter(input_array)
    for key, values in output.items():
        if values > 1:
            return key


input_list = [1, 2, 3, 4, 4]
output_values = get_duplicate_values(input_list)
print(output_values)

# GPT Solution where it completely uses 0(1) time and
# space complexity!
# Floyd's Tortoise and Hare algorithm

def find_duplicate(nums):
    # Phase 1: Finding the intersection point
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Finding the start of the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Example usage
array = [3, 1, 3, 4, 2]
duplicate = find_duplicate(array)
print(duplicate)  # Output: 3
