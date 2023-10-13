def oops():
    raise IndexError


def outer_1():
    try:
        oops()
    except IndexError:
        return "IndexError was catched."


def another_oops():
    raise KeyError


def outer_2():
    try:
        another_oops()
    except KeyError:
        return "KeyError was catched"


print(outer_1())
print(outer_2())
