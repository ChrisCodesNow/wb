'''
Approach :
Runtime: O()
Space Complexity: O()
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = []
        while self.stack:
            temp.append(self.stack.pop())

        self.stack.append(x)
        while temp:
            self.stack.append(temp.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack == []


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

    queue = MyQueue()        
    queue.push(1)
    queue.push(2)  
    t.run(queue.peek() == 1)
    t.run(queue.pop() == 1)
    t.run(queue.empty() == False)