from mystack import MyStack


def print_revert_sequence(iterable):
    new_stack = MyStack()
    for element in iterable:
        new_stack.push(element)
    for _ in range(new_stack.size()):
        print(new_stack.pop(), end=", ")
    print("\b\b")


if __name__ == "__main__":
    print_revert_sequence("stack")
    print_revert_sequence(list(range(10)))
    print_revert_sequence(list(range(10, 0, -2)))
    print_revert_sequence(enumerate(range(3), 12))
