class MyQueue:
    def __init__(self):
        self._items = []

    def empty(self):
        return not self._items

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        if self.size() < 1:
            return None
        return self._items.pop() if not self.empty() else None

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation
