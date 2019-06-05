'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Q =  deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        old_size = len(self.Q)
        self.Q.append(x)
        for _ in range(old_size):
            self.Q.append(self.Q.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.Q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.Q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.Q:
            return False
        else:
            return True
        



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

    stack = MyStack()
    stack.push(1)
    stack.push(2)  
    t.run(stack.top() == 2)
    t.run(stack.pop() == 2)
    t.run(stack.empty() == False)