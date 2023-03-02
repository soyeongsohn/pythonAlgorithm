import sys

class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return -1
        return self.queue[0]
    
    def back(self):
        if self.is_empty():
            return -1
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return 1 if len(self.queue) == 0 else 0
    
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    queue = Queue()

    for _ in range(N):
        comm = sys.stdin.readline().rstrip()
        if comm == "empty":
            print(queue.is_empty())
        elif comm == "size":
            print(queue.size())
        elif comm == "pop":
            print(queue.pop())
        elif comm == "front":
            print(queue.front())
        elif comm == "back":
            print(queue.back())
        else:
            queue.push(comm.split()[-1])