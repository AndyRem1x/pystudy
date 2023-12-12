def binary_search(value, sorted_list):
    list_len = len(sorted_list)
    if list_len == 0 or list_len == 1 and value != sorted_list[0]:
        return False
    mid_index = round(list_len / 2)
    if value == sorted_list[mid_index]:
        return True
    if value < sorted_list[mid_index] and mid_index > 0:
        return binary_search(value, sorted_list[0:mid_index])
    if value > sorted_list[mid_index]:
        return binary_search(value, sorted_list[mid_index:])
    return False


assert binary_search(5, [1, 6, 8, 10, 14, 66]) is False
assert binary_search(5, [1, 6, 8, 10, 14, 66, 85]) is False
assert binary_search(8, [1, 6, 8, 10, 14, 66]) is True
assert binary_search(8, [1, 6, 8, 10, 14, 66, 85]) is True
assert binary_search(1, [1, 6, 8, 10, 14, 66]) is True
assert binary_search(85, [1, 6, 8, 10, 14, 66, 85]) is True
assert binary_search(10, [1, 6, 8, 10, 14, 66]) is True
assert binary_search(14, [1, 6, 8, 10, 14, 66, 85]) is True
