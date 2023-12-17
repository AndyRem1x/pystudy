from node import Node


class MyExtendedUnsortedList:
    def __init__(self):
        self._head = None

    def empty(self):
        return self._head is None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self._head)
        self._head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.empty():
            self._head = new_node
            return
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError("Element in the list is not found.")

    def pop(self, index=None):
        if self.empty():
            raise IndexError("Pop from empty list.")
        index = (self.size() - 1) if index is None else index
        if self.size() <= index:
            raise IndexError("Pop index out of range.")
        if index == 0:
            value = self._head.get_data()
            self._head = self._head.get_next()
            return value
        current = self._head
        previous = self._head
        count = 1
        while current is not None and count != (index + 1):
            count += 1
            previous = current
            current = current.get_next()
        value = current.get_data()
        previous.set_next(current.get_next())
        return value

    def insert(self, index, item):
        if self.empty() or index == 0:
            self.add(item)
            return
        if self.size() < index:
            raise IndexError("Pop index out of range.")
        new_node = Node(item)
        current = self._head
        previous = self._head
        count = 1
        while current is not None and count != (index + 1):
            count += 1
            previous = current
            current = current.get_next()
        previous.set_next(new_node)
        new_node.set_next(current)

    def slice(self, start, stop):
        sliced_list = MyExtendedUnsortedList()
        if self.empty():
            raise IndexError("List is empty.")
        if self.size() <= start:
            raise IndexError("Start index out of range.")
        if stop <= start:
            raise IndexError("The stop index must be greater than the start index.")
        current = self._head
        index = 1
        while current is not None and index <= start:
            index += 1
            current = current.get_next()
        while current is not None and index <= stop:
            index += 1
            sliced_list.append(current.get_data())
            current = current.get_next()
        return sliced_list

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    new_list = MyExtendedUnsortedList()
    for num in range(2, 11):
        new_list.append(f"{num}")
    print(new_list)
    new_list.add("1")
    print(new_list)
    assert new_list.index("1") == 0
    assert new_list.index("5") == 4
    assert new_list.index("10") == 9
    assert new_list.pop() == "10"
    assert new_list.pop(0) == "1"
    assert new_list.pop(7) == "9"
    assert new_list.pop(3) == "5"
    print(new_list)
    new_list.insert(0, "1")
    new_list.insert(4, "5")
    new_list.insert(8, "9")
    new_list.insert(9, "10")
    print(new_list)
    assert new_list.slice(0, 3).size() == 3
    assert new_list.slice(2, 3).size() == 1
    assert new_list.slice(3, 7).size() == 4
    assert new_list.slice(5, 11).size() == 5
    print(new_list)
