'''
Approach 1:
    Get:
        Get key's val.
        Make key, val most recent.

    Put:
        Either update or insert.
        Remove LRU when at cap.
        Make key, val most recent.


Runtime: O(1)
Space Complexity: O(1)
'''

from collections import deque

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Q = deque()
        self.keys = dict()

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.Q.remove(node)
            self.Q.append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.update(key, value)
        else:
            self.insert(key, value)

    
    def update(self, key, val):
        node = self.keys[key]
        self.Q.remove(node)

        node.val = val
        self.Q.append(node)


    def insert(self, key, val):
        if len(self.Q) >= self.capacity:
            delete_node = self.Q.popleft()
            del self.keys[delete_node.key]
        
        node = Node(key, val)
        self.Q.append(node)
        self.keys[key] = node
        

# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
if __name__ == '__main__':
    t = Test()

        
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    t.run((cache.get(1)) == 1)          # returns 1
    cache.put(3, 3)                     # evicts key 2
    t.run((cache.get(2)) == -1)         # returns -1 (not found)
    cache.put(4, 4)                     # evicts key 1
    t.run((cache.get(1)) == -1)         # returns -1 (not found)
    t.run((cache.get(3)) == 3)          # returns 3
    t.run((cache.get(4)) == 4)          # returns 4