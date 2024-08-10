# Problem statement
# You are given a string 'str' of length 'N'.
# Your task is to reverse the original string word by word.
# There can be multiple spaces between two words and there can be leading or trailing spaces but in the output reversed string you need to put a single space between two words, and your reversed string should not contain leading or trailing spaces.
# Example:
# If the given input string is "Welcome to Coding Ninjas", then you should return "Ninjas Coding to Welcome" as the reversed string has only a single space between two words and there is no leading or trailing space.


def reverse_string_in_sentence(input_string: str) -> str:
    split_string = input_string.split(" ")
    removed_white_spacing = [x for x in split_string if x != ""]
    split_string_stripped = [x.strip() for x in removed_white_spacing]

    index = len(split_string_stripped)-1
    reversed_string = ""

    while index >= 0:
        reversed_string += split_string_stripped[index] + " "
        index -= 1

    return reversed_string

    # print(split_string_rev)
    # stripped_list_rev = [x.strip() for x in split_string_rev]
    # joined_string = " ".join(stripped_list_rev)
    # return joined_string


input_string = "Welcome to Coding Ninjas"
output = reverse_string_in_sentence(input_string)
print(output)
