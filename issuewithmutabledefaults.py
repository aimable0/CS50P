def append_to_list(value, my_list=None):  # Mutable default: `my_list`
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# Usage
print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (unexpected!)
print(append_to_list(5))  # Output: [1, 2, 3] (unexpected!)

my_list = [1, 4, 6]
print(append_to_list(0, my_list))