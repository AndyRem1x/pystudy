class CustomIterable:
    def __init__(self, init_object):
        self.index = 0
        self._iterable = init_object

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._iterable):
            raise StopIteration
        result = self._iterable[self.index]
        self.index += 1
        return result

    def __getitem__(self, index):
        return self._iterable[index]

    def __len__(self):
        return len(self._iterable)


test_object = "test_string"
char_list1 = []
char_list2 = []
char_list3 = []

my_iterable_object = CustomIterable(test_object)

for element in my_iterable_object:
    char_list1.append(element)

for _, value in enumerate(my_iterable_object):
    char_list2.append(value)

for i in range(0, len(my_iterable_object)):
    char_list3.append(my_iterable_object[i])

assert list(my_iterable_object) == char_list1
assert list(my_iterable_object) == char_list2
assert list(my_iterable_object) == char_list3
