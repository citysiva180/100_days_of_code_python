# While loops and the technique to break the infinity scenario!

sample_list = range(10)

# important points
# while loop needs an empty variable to be declared before it could go forward
# while loop also needs an incrementor to keep it up


count = 0

# for the while loop, the condition for breaking infinity is given in the loop syntax itself
while count < len(range(10)):
    print(count)
    count += 1

# Reverse while loop
# remember if your count variable is not determined to have the max value
another_count = len(range(10))-1
# then your reverse loop will go infinitely! ensure to break your reverse loop properly!

while another_count >= 0:
    print(another_count)
    another_count -= 1
