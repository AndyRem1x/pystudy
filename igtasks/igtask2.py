class CustomRange:

    def __init__(self, start, stop, step):
        if step == 0:
            raise ValueError()
        self.index = 0
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        result = self.start + self.step * self.index
        if self.step > 0 and result >= self.stop:
            raise StopIteration
        if self.step < 0 and self.stop >= result:
            raise StopIteration
        self.index += 1
        return result

    def __str__(self):
        return (f"custom_range({self.start}, {self.stop}" f'{f", {self.step}" if not self.step == 1 else ""})')


def in_range(value, *args):
    start = 0
    stop = value
    step = 1
    if len(args) == 1:
        start, stop = value, args[0]
    if len(args) == 2:
        start, stop, step = value, args[0], args[1]
    return CustomRange(start, stop, step)


print(in_range(10))
print(in_range(1, 10))
print(in_range(1, 11, 2))
print(in_range(10, 1, -2))
print(*in_range(10))
print(*in_range(1, 10))
print(*in_range(1, 11, 2))
print(*in_range(10, 1, -2))

assert [*in_range(4)] == [*range(4)]
assert [*in_range(1, 7)] == [*range(1, 7)]
assert [*in_range(1, 9, 3)] == [*range(1, 9, 3)]
assert [*in_range(9, 1, -3)] == [*range(9, 1, -3)]
