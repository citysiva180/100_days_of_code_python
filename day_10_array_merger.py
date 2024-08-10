# Merge two arrays by satisfying given constraints
# Given two sorted arrays X[] and Y[] of size m and n
# each where m >= n and X[] has exactly n vacant cells,
# merge elements of Y[] in their correct position in
# array X[], i.e., merge (X, Y) by keeping the sorted order.
x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
y = [1, 8, 9, 10, 15]

# replace all the zeroes with the sorted values!


def replace_the_zeroes(x, y):
    # find the index of 0
    # try to replace the index of zeroes with smaller array values
    y = sorted(y, reverse=True)

    len_of_y = len(y)-1
    for items in range(len(x)):
        if x[items] == 0:
            x[items] = y[len_of_y]
            len_of_y -= 1

    print(sorted(x))


replace_the_zeroes(x, y)

# my solution explained
# in my solution, I am reversing the smaller array..
# and replacing values of zeroes with the elements in smaller array on index
# we could have simply gone for pop and merge but replacing elements in array
# In my solution, I am using the sorted of x which even though I had replaced all the
# zeroes with my values in y
# trust in self!
