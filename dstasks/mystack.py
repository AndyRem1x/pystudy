class MyStack:
    def __init__(self):
        self._items = []

    def empty(self):
        return not self._items

    def peek(self):
        return self._items[len(self._items) - 1] if not self.empty() else None

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if not self.empty() else None

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation
