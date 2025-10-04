def count_words(string):
    count = len(string.split())
    return count
def count_chars(string):
    char_count = {}
    for char in string.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
def sort_dicts(dict_in):
    dict_list = []
    for char, count in dict_in.items():
        dict_list.append({"char": char, "num":count})
    return sorted(dict_list, key=sort_on, reverse=True)
def sort_on(items):
    return items["num"]
# Alternative
def get_chars_dict(text):
    # Declare empty dict
    char_dict = {}
    # loop through characters in the input string
    for char in text:
        # Set the current character to lowercase
        lowered = char.lower()
        # check if the lowercase letter is already in the dict
        if lowered in char_dict:
            # If it is, add 1 to the value @ key = current character
            char_dict[lowered] += 1
        # Else, add a new entry with value 1 for its first count
        else:
            char_dict[lowered] = 1
    # return the dict
    return char_dict

# Alternative for sorted list
def sort_on_2(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on_2)
    return sorted_list
