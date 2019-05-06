class UnionFind:
    # Create n subsets of 1 element
    def __init__(self, n):
        self.parent = [i for i in range(n)]


    # Find root node of subset
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])


    # Connect two subsets of parent of x and parent of y
    def join(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        self.parent[root_x] = root_y
        
    
    # Get copy of parent 
    def get_parent(self):
        return self.parent[:]


    # Connect each susbset parent to all its direct children
    # O(n)
    def compress(self):
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)