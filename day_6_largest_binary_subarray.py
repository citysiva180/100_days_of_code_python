# Find the largest subarray having an equal number of 0’s and 1’s
# Given a binary array containing 0’s and 1’s, find the largest subarray with equal numbers of 0’s and 1’s


def find_largest_subarray_with_equal_0s_1s(arr):
    # Step 1: Replace 0 with -1
    transformed_arr = [-1 if x == 0 else 1 for x in arr]
    
    # Step 2: Use a hashmap to store the first occurrence of each prefix sum
    prefix_sum_map = {}
    prefix_sum = 0
    max_len = 0
    end_index = -1

    for i in range(len(transformed_arr)):
        prefix_sum += transformed_arr[i]

        if prefix_sum == 0:
            max_len = i + 1
            end_index = i

        if prefix_sum in prefix_sum_map:
            # Check if the current prefix sum has been seen before
            if max_len < i - prefix_sum_map[prefix_sum]:
                max_len = i - prefix_sum_map[prefix_sum]
                end_index = i
        else:
            # Store the first occurrence of the prefix sum
            prefix_sum_map[prefix_sum] = i

    # Step 3: Get the starting index of the subarray
    start_index = end_index - max_len + 1

    return arr[start_index:end_index + 1], max_len

# Example usage
arr = [1, 0, 0, 1, 0, 1, 1]
result, length = find_largest_subarray_with_equal_0s_1s(arr)
print(f"Largest subarray with equal number of 0's and 1's: {result}")
print(f"Length of the largest subarray: {length}")
