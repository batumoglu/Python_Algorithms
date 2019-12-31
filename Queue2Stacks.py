class Queue2Stacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

if __name__ == '__main__':
    q = Queue2Stacks()

    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        print(q.dequeue())