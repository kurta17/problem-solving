class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}  
        
    def insert(self, value, new_value):
        new_node = Node(new_value)
        node = self.nodes[value]  
        
        new_node.next = node.next
        new_node.prev = node
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.nodes[new_value] = new_node  

    def erase(self, value):
        node = self.nodes[value]  
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del self.nodes[value]  

n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = LinkedList()

for i in a:
    new_node = Node(i)
    if l.head is None:
        l.head = new_node
        l.tail = new_node
    else:
        l.tail.next = new_node
        new_node.prev = l.tail
        l.tail = new_node
    l.nodes[i] = new_node  

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l.insert(query[1], query[2])
    else:
        l.erase(query[1])

node = l.head
while node is not None:
    print(node.value, end=' ')
    node = node.next