def merge_sort(array):
    array_len = len(array)
    if array_len > 1:
        mid = array_len // 2
        left_half = [array[index] for index in range(0, mid)]
        right_half = [array[index] for index in range(mid, array_len)]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array


assert merge_sort([79, 90, -71, -54, 85, -55, 32, -5, -11, -60]) == [
    -71,
    -60,
    -55,
    -54,
    -11,
    -5,
    32,
    79,
    85,
    90,
]
assert merge_sort([-17, -81, 44, 92, -54, -2, 96, -1, -96, 75]) == [
    -96,
    -81,
    -54,
    -17,
    -2,
    -1,
    44,
    75,
    92,
    96,
]
assert merge_sort([-70, 31, 48, 21, 11, 38, 1, 35, 94]) == [
    -70,
    1,
    11,
    21,
    31,
    35,
    38,
    48,
    94,
]
