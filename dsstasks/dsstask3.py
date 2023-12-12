from node import Node


class MyQueue:

    def __init__(self):
        self._head = None

    def empty(self):
        return self._head is None

    def enqueue(self, item):
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node

    def dequeue(self):
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
        representation = "<Queue: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_queue = MyQueue()
    for num in range(1, 11):
        new_queue.enqueue(f"{num}")
    print(new_queue)
    assert new_queue.size() == 10
    assert new_queue.dequeue() == "1"
    assert new_queue.size() == 9
    assert new_queue.dequeue() == "2"
    print(new_queue)
    new_queue.enqueue("1")
    new_queue.enqueue("2")
    new_queue.enqueue("new_item")
    print(new_queue)
