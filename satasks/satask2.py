class MyHashTable:
    def __init__(self, max_length=0):
        self.max_length = max_length or 100
        self.storage = []
        for _ in range(self.max_length):
            self.storage.append([])
        self.len = 0

    @classmethod
    def _hash(cls, key_str: str, hash_len):
        hash_value = 17
        for char in key_str:
            hash_value = (hash_value * 31 + ord(char)) % hash_len

        return hash_value

    def _find_item_by_key(self, my_key, ):
        index = MyHashTable._hash(my_key, self.max_length)
        result = self.storage[index]
        for inner_index, (item_key, item_value) in enumerate(result):
            if item_key == my_key:
                return index, inner_index, item_key, item_value
        return index, None, None, None

    def get_by_key(self, my_key):
        _, __, item_key, item_value = self._find_item_by_key(my_key)
        if item_key:
            return item_value
        raise KeyError(f"Key '{my_key}' dot exists in table")

    def save_value_by_key(self, my_key, new_value):
        self.len += 1
        self.rehash_and_storage_extend()
        index, inner_index, item_key, _ = self._find_item_by_key(my_key)
        if item_key:
            self.storage[index][inner_index][1] = new_value
            return None
        self.storage[index].append([my_key, new_value])
        return None

    def delete_item_by_key(self, my_key):
        index, inner_index, item_key, _ = self._find_item_by_key(my_key)
        if item_key:
            self.storage[index].pop(inner_index)
            self.len -= 1
            return None
        raise KeyError(f"Key '{my_key}' dot exists in table")

    def items(self):
        res = []
        for nested_lists in self.storage:
            for item in nested_lists:
                res.append(item)
        return res

    def table_update(self, other_table):
        for item_key, item_value in other_table.items():
            self.save_value_by_key(item_key, item_value)

    def rehash_and_storage_extend(self):
        if self.len == self.max_length:
            self.max_length *= 2
            new_table = MyHashTable(self.max_length)
            for item_key, item_value in self.items():
                new_table.save_value_by_key(item_key, item_value)
            self.storage = new_table.storage
            del new_table

    def __contains__(self, item):
        _, __, item_key, __ = self._find_item_by_key(item)
        if item_key:
            return True
        return False

    def __len__(self):
        return self.len

    def __getitem__(self, item_key):
        _, __, item_key, item_value = self._find_item_by_key(item_key)
        if item_key:
            return item_value
        raise KeyError

    def __setitem__(self, item_key, new_value):
        self.save_value_by_key(item_key, new_value)


my_table = MyHashTable(10)
my_table["key"] = "new value"
for num in range(1, 7):
    if num == 3:
        continue
    my_table.save_value_by_key(f"key{num}", f"value{num}")

assert ("key1" in my_table) is True
assert ("key3" in my_table) is False
assert len(my_table) == 6

for num in range(7, 27):
    my_table.save_value_by_key(f"key{num}", f"value{num}")
assert len(my_table) == 26
assert my_table["key"] == "new value"
