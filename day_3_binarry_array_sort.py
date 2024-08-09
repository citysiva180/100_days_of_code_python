# Sorting Binary Array with Constant time and Space!
# Sort binary array in linear time
# Given a binary array, sort it in linear time and constant space. The output should print all zeros, followed by all ones.
input = [1, 0, 1, 0, 1, 0, 0, 1]


def binary_array_sort(binary_array):

    zero_count = 0
    ones_count = 0

    for elements in binary_array:
        if elements == 0:
            zero_count += 1
        else:
            ones_count += 1

    binary_array.clear()
    for _ in range(zero_count):
        binary_array.append(0)
    for _ in range(ones_count):
        binary_array.append(1)

    return binary_array


output = binary_array_sort(input)
print(output)

# In my solution Iam using the same data structure and appending all 1 at the end
# here is another solution where the value is shifted


def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# Example usage
binary_array = [1, 0, 1, 0, 1, 0, 0, 1]
sorted_array = sort_binary_array(binary_array)
print(sorted_array)
