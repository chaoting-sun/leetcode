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
        self.pairs = {} # 
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key):
        node = self.pairs[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        value = node.value
        del self.pairs[key]
        return value
    
    def add(self, key, value):
        node = Node(key, value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.pairs[key] = node

    def get(self, key: int) -> int:
        # if the key exists, remove the key in dll, and add the key at the tail
        # if not, return -1
        if key in self.pairs:
            value = self.remove(key)
            self.add(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key exists, remove the key in dll, and add the key at the tail
        # if not, add the key at the tail
        if key in self.pairs:
            self.remove(key)
            self.add(key, value)
        else:
            if len(self.pairs) == self.capacity:
                self.remove(self.head.next.key)
            self.add(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)