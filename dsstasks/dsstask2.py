from node import Node


class MyStack:
    def __init__(self):
        self._head = None

    def empty(self):
        return self._head is None

    def peek(self):
        if self.empty():
            return None
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        return current.get_data()

    def push(self, item):
        new_node = Node(item)
        if self.empty():
            self._head = new_node
            return None
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)
        return None

    def pop(self):
        if self.empty():
            return None
        current = self._head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<Stack: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_stack = MyStack()
    for num in range(1, 11):
        new_stack.push(f"{num}")
    print(new_stack)
    assert new_stack.peek() == "10"
    assert new_stack.size() == 10
    assert new_stack.pop() == "10"
    assert new_stack.size() == 9
    assert new_stack.peek() == "9"
    assert new_stack.pop() == "9"
    assert new_stack.peek() == "8"
    assert new_stack.pop() == "8"
    assert new_stack.peek() == "7"
    print(new_stack)
    new_stack.push("9")
    new_stack.push("8")
    new_stack.push("new_item")
    print(new_stack)
