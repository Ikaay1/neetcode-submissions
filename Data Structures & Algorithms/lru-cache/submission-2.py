class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

#key -> node (holds value)
class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.head = self.tail = None
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        node = self.keys[key]
        self.remove(node)
        self.append(node)

        return node.val
        
    def append(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        else:
            self.tail = node
            self.head = node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.key, temp.val)
            temp = temp.next
        
        print("-----------")

    def remove(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            self.remove(node)
        elif self.size == self.capacity:
            del self.keys[self.head.key]
            self.remove(self.head)
        else:
            self.size += 1

        new_node = Node(key, value)
        self.append(new_node)
        self.keys[key] = new_node
        self.print_list()

        
