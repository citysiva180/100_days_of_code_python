# Given an integer array, find the maximum product of two integers in it.

# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.

array_1 = [-10, -3, 5, 6, -2]

max_num = 0

list_of_list = []
for initial_value in array_1:
    for iterated_value in array_1:
        if iterated_value != initial_value:
            product = initial_value * iterated_value
            if product > max_num:
                max_num = product
                list_of_list.append([initial_value, iterated_value])
            elif product == max_num:
                list_of_list.append([initial_value, iterated_value])


print(list_of_list)


def max_product_of_two_integers(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")

    # Initialize the largest and smallest pairs
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    # Traverse the array to find the largest and smallest pairs
    for num in arr:
        # Update the largest pair
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Update the smallest pair
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # The maximum product is the maximum of the product of the two largest
    # and the product of the two smallest
    product1 = max1 * max2
    product2 = min1 * min2

    result_pairs = []
    max_product = max(product1, product2)

    if product1 == max_product:
        result_pairs.append((max1, max2))
    if product2 == max_product:
        result_pairs.append((min1, min2))

    return max_product, result_pairs


# Example usage
arr = [-10, -3, 5, 6, -2]
max_product, pairs = max_product_of_two_integers(arr)
print(f"Maximum product is {max_product} from the pairs {pairs}")
