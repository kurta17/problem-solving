import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_back(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def push_mid(self, data):
        if self.count == 0:
            self.push_back(data)
        else:
            new_node = Node(data)
            mid_node = self.get_mid_node()
            new_node.next = mid_node.next
            new_node.prev = mid_node
            mid_node.next.prev = new_node
            mid_node.next = new_node
            self.count += 1

    def get_mid_node(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def pop_front(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.count -= 1
            return data

    def len(self):
        return self.count


n = int(input())
d = [Deque() for _ in range(n)]

while True:
    a = input()
    if a[0] == '#':
        break
    elif a[0] == '+':
        parts = a.split()
        b = int(parts[1])
        c = int(parts[2])
        d[b].push_back(c)
    elif a[0] == '-':
        parts = a.split()
        b = int(parts[1])
        print(d[b].pop_front())
    elif a[0] == '?':
        parts = a.split()
        b = int(parts[1])
        print(d[b].len())
    elif a[0] == '!':
        parts = a.split()
        b = int(parts[1])
        c = int(parts[2])
        d[b].push_mid(c)
        