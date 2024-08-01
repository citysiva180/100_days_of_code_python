# Find maximum length subarray having a given sum
# Given an integer array, find the maximum length subarray having a given sum.

# creating a hashmap
nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8

# Practicing hashmap in Python!


def max_sum_array(input_list, target_sum):

    sum_map = {}  # this is the hashmap they are talking about
    max_length = 0
    cumulative_sum = 0
    start_index = -1

    for index, number in enumerate(input_list):
        # This is just a counter, but its just summing the list of elements in a list
        cumulative_sum += number

        if cumulative_sum == target_sum:
            max_length = index + 1
            start_index = 0

        if (cumulative_sum - target_sum) in sum_map:

            current_length = index - sum_map[cumulative_sum - target_sum]

            if current_length > max_length:
                max_length = current_length
                start_index = sum_map[cumulative_sum - target_sum] + 1

        # Adding code for getting the sub-array

        if cumulative_sum not in sum_map:
            sum_map[cumulative_sum] = 1

    if max_length > 0:
        # how will this work?
        max_subarray = input_list[start_index:start_index+max_length] 
    else:
        max_subarray = []

    return max_length, max_subarray


max_length, max_subarray = max_sum_array(nums, target)
print("max_len : ", max_length)
print("max_subarray : ", max_subarray)
