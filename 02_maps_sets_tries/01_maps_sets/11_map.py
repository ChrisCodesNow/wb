'''
Approach 1:
    Map with chaining

Runtime: O(1), average
Space Complexity: O(n)
'''
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = [[] for _ in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hash(key)
        j = self.find(key, idx)

        if j == -1:
            self.add_key_val(key, value, idx)
        else:
            self.update_value(value, idx, j)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hash(key)
        j = self.find(key, idx)

        if j == -1:
            return -1
        else:
            return self.M[idx][j][1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hash(key)
        j = self.find(key, idx)
        if j != -1:
            self.M[idx].pop(j)


    def hash(self, key):
        return key % 9973


    # Find key in hashed slot
    def find(self, key, idx):
        for j, pair in enumerate(self.M[idx]):
            if key == pair[0]:
                return j

        return -1


    def add_key_val(self, key, value, idx):
        self.M[idx].append([key, value])


    def update_value(self, val, idx, j):
        self.M[idx][j][1] = val


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


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



    hashMap = MyHashMap()
    hashMap.put(1, 1)       
    hashMap.put(2, 2)         
    t.run(hashMap.get(1) == 1)
    t.run(hashMap.get(3) == -1)
    hashMap.put(2, 1);          # update the existing value
    t.run(hashMap.get(2) == 1) 
    hashMap.remove(2);          # remove the mapping for 2
    t.run(hashMap.get(2) == -1) 