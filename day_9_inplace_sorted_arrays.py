# In-place merge two sorted arrays
# Given two sorted arrays, X[] and Y[] of size m and n each,
# merge elements of X[] with elements of array Y[] by maintaining
# the sorted order, i.e., fill X[] with the first m smallest
# elements and fill Y[] with remaining elements.

x = [1, 4, 7, 8, 10]
y = [2, 3, 9]

output = x + y
new_output = sorted(output)

x = new_output[:len(x)]
y = new_output[len(x):]

print(x)
print(y)

# GPT Solution


def merge(X, Y):
    m, n = len(X), len(Y)

    # Traverse X[] from the end and Y[] from the start
    for i in range(m-1, -1, -1):
        # Compare the largest in X[] with the smallest in Y[]
        if X[i] > Y[0]:
            # Swap if the element in X[] is greater
            X[i], Y[0] = Y[0], X[i]
            # Re-sort Y[] to ensure it's still sorted after the swap
            Y.sort()

    # Sort X[] again to ensure it's in correct order
    X.sort()


# Example usage:
X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]

merge(X, Y)
print("X:", X)  # X should have the first m smallest elements
print("Y:", Y)  # Y should have the remaining elements
