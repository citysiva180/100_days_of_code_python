# Given an array arr[] of integers, find out the difference between any two elements
# such that larger element appears after the smaller number in arr[].
# Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
# If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)

def larger_and_small_diff(input_list):

    # identify the largest and smallest elements in the list
    # identify the index position of these elements and compare to
    # see if the largest index greater than smallest index..
    min_output = 0
    max_output = max(input_list)
    enumerated_dict = {value: index for index, value in enumerate(input_list)}

    for elements in input_list:
        if elements < max_output and enumerated_dict[elements] < enumerated_dict[max_output] and min_output == 0:
            min_output = elements
            return max_output-elements


input_list = [7, 9, 5, 6, 3, 2]
output = larger_and_small_diff(input_list)
input_list_2 = [2, 3, 10, 6, 4, 8, 1]
output = larger_and_small_diff(input_list_2)
