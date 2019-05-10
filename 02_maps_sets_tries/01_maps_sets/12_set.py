'''
Approach 1:
    Hash with chaining
Runtime: O(1), on average
Space Complexity: O(n)
'''
from typing import List
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.S = [[] for _ in range(10000)]
        

    def add(self, key: int) -> None:
        idx = self.my_hash(key)
        if self.find(key, idx) == -1:
            self.S[idx].append(key)


    def remove(self, key: int) -> None:
        idx = self.my_hash(key)
        j = self.find(key, idx)
        if j != -1:
            self.S[idx].pop(j)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self.my_hash(key)
        j = self.find(key, idx)
        return j != -1


    def my_hash(self, key):
        return key % 9977


    def find(self, key, idx):
        for j, k in enumerate(self.S[idx]):
            if key == k:
                return j

        return -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


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


hashSet = MyHashSet()
hashSet.add(1)         
hashSet.add(2)         
t.run(hashSet.contains(1) == True)
t.run(hashSet.contains(3) == False)
hashSet.add(2)        
t.run(hashSet.contains(2) == True)
hashSet.remove(2)          
t.run(hashSet.contains(2) == False)
