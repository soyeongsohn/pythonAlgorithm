import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return -1
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    stack = Stack()
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        command = sys.stdin.readline().rstrip()
        if command == "top":
            print(stack.top())
        elif command == "pop":
            print(stack.pop())
        elif command == "empty":
            print(1 if stack.is_empty() else 0)
        elif command == "size":
            print(stack.size())
        else: # push
            stack.push(command.split()[-1])