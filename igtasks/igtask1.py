class CustomEnumerate:

    def __init__(self, iterable, start=0):
        self.index = 0
        self.start = start
        self.iterable = iterable or []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.iterable):
            raise StopIteration
        result = (self.index + self.start, self.iterable[self.index])
        self.index += 1
        return result


def with_index(iterable, start):
    return CustomEnumerate(iterable, start)


test_list = [1, 3, 5, 7, 9, 10]
custom_enumerate_arr = []
enumerate_arr = []

for index, item in with_index(test_list, 2):
    custom_enumerate_arr.append((index, item))

for index, item in enumerate(test_list, 2):
    enumerate_arr.append((index, item))

assert custom_enumerate_arr == enumerate_arr
