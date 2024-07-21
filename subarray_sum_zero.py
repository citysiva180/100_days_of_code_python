# Given an integer array, check if it contains a subarray having zero-sum.

# My Solution : Completely built by me...

import itertools


def check_sub_array_zero(input_list: list) -> list:
    """ Function that gives sub-arrays which has 0 in them

    Returns:
        list: input is a large python list and output is multiple lists! 
    """

    output_list = []

    def slice_the_list_from_front(input_list, ending_index):
        front_list = input_list[:ending_index]
        if sum(front_list) == 0:
            if len(front_list) != 0:
                return front_list

    def slice_the_list_from_back(input_list, starting_index):
        back_list = input_list[starting_index:]
        if sum(back_list) == 0:
            if len(back_list) != 0:
                return back_list

    while input_list:

        for index in range(len(input_list)):

            reverse_index = len(input_list) - (index+1)
            list_1 = slice_the_list_from_front(input_list, reverse_index)
            list_2 = slice_the_list_from_back(input_list, index)
            if type(list_1) != type(None):
                output_list.append(list_1)
            if type(list_2) != type(None):
                output_list.append(list_2)

        input_list.pop(0)

    output_list.sort()
    new_list = list(output_list for output_list,
                    _ in itertools.groupby(output_list))

    return new_list


test_input_list = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
result_list = check_sub_array_zero(test_input_list)
print(result_list)


# Chat gpt solution which uses hashmap to do this!

def check_sub_array_zero_gpt(input_list: list) -> list:
    """ Function that finds all sub-arrays which sum up to 0.

    Args:
        input_list (list): The input list of integers.

    Returns:
        list: List of sub-arrays that sum to zero.
    """
    # Dictionary to store cumulative sum and its corresponding indices
    sum_map = {}
    cumulative_sum = 0
    result = []

    # Initialize sum_map with a key for cumulative_sum of 0 at index -1
    sum_map[0] = [-1]

    # Traverse the input list and compute cumulative sum
    for index, value in enumerate(input_list):
        cumulative_sum += value

        # If cumulative sum is found in sum_map, there exist sub-arrays with zero sum
        if cumulative_sum in sum_map:
            start_indices = sum_map[cumulative_sum]
            for start_index in start_indices:
                result.append(input_list[start_index + 1:index + 1])
            sum_map[cumulative_sum].append(index)
        else:
            sum_map[cumulative_sum] = [index]

    return result


# Example usage
test_input_list = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
print(check_sub_array_zero_gpt(test_input_list))
