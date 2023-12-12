from mystack import MyStack
from myqueue import MyQueue


class MyExtendedStack(MyStack):
    def __init__(self):
        super().__init__()
        self.temp = MyStack()
        self.temp_item = None

    def get_from_stack(self, element):
        for _ in range(self.size()):
            self.temp_item = self.pop()
            if element == self.temp_item:
                break
            self.temp.push(self.temp_item)
        for _ in range(self.temp.size()):
            self.push(self.temp.pop())
        if not self.temp_item:
            raise ValueError("Element in stack is not found.")
        result = self.temp_item
        self.temp_item = None
        return result


class MyExtendedQueue(MyQueue):
    def __init__(self):
        super().__init__()
        self.temp = MyQueue()
        self.temp_item = None

    def get_from_queue(self, element):
        for _ in range(self.size()):
            self.temp_item = self.dequeue()
            if element == self.temp_item:
                continue
            self.temp.enqueue(self.temp_item)
        for _ in range(self.temp.size()):
            self.enqueue(self.temp.dequeue())
        if not self.temp_item:
            raise ValueError("Element in queue is not found.")
        result = self.temp_item
        self.temp_item = None
        return result


if __name__ == "__main__":
    stack_1 = MyExtendedStack()
    for number in range(1, 7):
        stack_1.push(f"{number}")
    print(stack_1)
    stack_1.get_from_stack("2")
    print(stack_1)
    stack_1.get_from_stack("6")
    print(stack_1)
    queue_1 = MyExtendedQueue()
    for number in range(1, 7):
        queue_1.enqueue(f"{number}")
    print(queue_1)
    queue_1.get_from_queue("5")
    print(queue_1)
    queue_1.get_from_queue("2")
    print(queue_1)
