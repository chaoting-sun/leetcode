# a doubly linked list -> record the least recently used key
# a hashmap -> record the key-Node({key, val}) pairs

class Node:
    # a node for a doubly linked list
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = {}
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_key_in_dict(self, key):
        del self.pairs[key]

    def update_key_in_dict(self, key, node):
        self.pairs[key] = node

    def remove_key_in_dll(self, key):
        node = self.pairs[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        value = node.value
        del self.pairs[key]
        return value
    
    def add_key_in_dll(self, key, value):
        node = Node(key, value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.pairs[key] = node
        return node

    def get(self, key: int) -> int:
        if key in self.pairs:
            value = self.remove_key_in_dll(key)
            self.add_key_in_dll(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            self.remove_key_in_dll(key)
        elif len(self.pairs) == self.capacity:
            self.remove_key_in_dll(self.head.next.key)

        node = self.add_key_in_dll(key, value)
        self.update_key_in_dict(key, node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)