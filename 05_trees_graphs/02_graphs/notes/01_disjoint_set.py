class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]


    def find(self, a):
        '''
        Get root node/parent node of a
        '''
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


    def join(self, b, a):
        '''
        Make root of a parent of root of b
        '''
        parent_a = self.find(a)
        parent_b = self.find(b)
        self.parent[parent_b] = parent_a


    def are_connected(self, a, b):
        return self.find(a) == self.find(b)



if __name__ == '__main__':
    # Test
    class Test:
        count = 0
        def run(self, result):
            self.count += 1
            if result:
                print(f"Passed test {self.count}")
            else:
                print(f"Failed test {self.count}")

    t = Test()
    n = 10
    ds = DisjointSet(n)

    ds.join(2, 1)
    ds.join(4, 3)
    ds.join(8, 4)
    ds.join(9, 3)
    ds.join(6, 5)
    ds.join(5, 2)

    a, b = 0, 7
    t.run(ds.are_connected(a, b) == False)

    a, b = 8, 9
    t.run(ds.are_connected(a, b) == True)