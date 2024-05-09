class Deque:
    def __init__(self):
        self.front = []
        self.back = []

    def pop_back(self):
        if not self.back and self.front:
            self.back = self.front[::-1]
            self.front = []
        return self.back.pop() if self.back else "Error!"

    def pop_front(self):
        if not self.front and self.back:
            self.front = self.back[::-1]
            self.back = []
        return self.front.pop() if self.front else "Error!"
     
    def push_back(self, x):
        self.back.append(x)

    def push_front(self, x):
        self.front.append(x)

    def len(self):
        return len(self.front) + len(self.back)


deque = Deque()
import deque

while True:
    operation = list(map(int, input().split()))
    if operation[0] == -1:
        break
    elif operation[0] == 0:
        deque.push_back(operation[1])
    elif operation[0] == 1:
        deque.push_front(operation[1])
    elif operation[0] == 2:
        print(deque.len())
    elif operation[0] == 3:
        result = deque.pop_back()
        print(result if result != "Error!" else "Error!")
    elif operation[0] == 4:
        result = deque.pop_front()
        print(result if result != "Error!" else "Error!")