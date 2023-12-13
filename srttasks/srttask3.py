import random
import time


def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = current_value
    return array


def quick_sort(array, partition_limit=1):
    quick_sort_helper(array, 0, len(array) - 1, partition_limit)
    return array


def quick_sort_helper(array, first, last, partition_limit=10):
    if len(array) <= partition_limit:
        insertion_sort(array)
    if first < last:
        split_point = partition(array, first, last)
        if split_point - first <= partition_limit:
            insertion_sort(array[first:split_point])
        else:
            quick_sort_helper(array, first, split_point - 1, partition_limit)

        if last - split_point <= partition_limit:
            insertion_sort(array[split_point + 1:last + 1])
        else:
            quick_sort_helper(array, split_point + 1, last, partition_limit)


def partition(array, first, last):
    pivot_value = array[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark += 1
        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp
    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp
    return right_mark


test_list = [random.randint(-99, 100) for _ in range(100000)]
start = time.time()
quick_sort(test_list, partition_limit=10)
time1 = time.time() - start

test_list = [random.randint(-99, 100) for _ in range(100000)]
start = time.time()
quick_sort(test_list)
time2 = time.time() - start
print(
    "Quick sort for list of 100000 elements ",
    "with partition limit 10 faster then ",
    f"quick sort without it on {round((time1 - time2)*1000)} ms",
    sep="\n",
)
