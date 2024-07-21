# Original Solution


list_1 = [2, 7, 11, 15]
target = 9
list_2 = [3, 2, 4]
target_2 = 6

# using hashmap for solutions


def two_sum(num_list, target):
    previous_map = {}

    for i, n in enumerate(num_list):
        diff = target - n
        if diff in previous_map:
            return [previous_map[diff], i]
        previous_map[n] = i
    return


two_sum(list_2, target_2)

# Below solutions is a O(N) solutions and its not preferred


def sum_of_pairs_index(num_list, target):

    for items in num_list:
        print(items)
        for index in range(len(num_list)):
            print(index)
            if num_list[index] != items:
                check = items + num_list[index]
                if check == target:
                    print("code entered here...")
                    print([num_list[index], items])


sum_of_pairs_index(list_2, target_2)
