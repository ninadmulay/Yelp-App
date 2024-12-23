from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.map = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, new_val):
        if new_val not in self.map:
            return False
        node = self.map[new_val]
        # Remove and add to make it most recent
        self._removeNode(node)
        self._addNode(node)
        return True
        

    def _addNode(self, new_node):
        temp = self.tail.prev
        temp.next = new_node
        new_node.prev = temp
        new_node.next = self.tail
        self.tail.prev = new_node

    def _removeNode(self, new_node):
        new_node.prev.next = new_node.next
        new_node.next.prev = new_node.prev
        new_node.prev = None
        new_node.next = None
    
    def add(self, new_val):
        if new_val in self.map:
            node = self.map[new_val]
            self._removeNode(node)
            self._addNode(node)
        else:
            node = Node(new_val)
            self._addNode(node)
            self.map[new_val] = node
            if len(self.map) > self.size:
                nodeToRemove = self.head.next
                del self.map[nodeToRemove.val]
                self._removeNode(nodeToRemove)
        return True
    
if __name__ == "__main__":
    obj = LRUCache(2)
    obj.add(1)
    obj.add(2)
    obj.get(1)
    obj.add(3)
    obj.get(2)
    obj.add(4)
    obj.get(1)
    obj.get(3)
    obj.get(4)
    