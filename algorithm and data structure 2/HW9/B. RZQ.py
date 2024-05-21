class RZQSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = 1 if data[i] == 0 else 0
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, index, delta):
        index += self.n
        a[index - self.n] += delta  # update the original array element
        if a[index - self.n] == 0:
            self.tree[index] = 1
        else:
            self.tree[index] = 0
        i = index
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def query(self, l, r):
        l += self.n
        r += self.n
        zeros_count = 0
        while l < r:
            if l % 2:
                zeros_count += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                zeros_count += self.tree[r]
            l //= 2
            r //= 2
        return zeros_count


n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = RZQSegmentTree(a)
for _ in range(m):
    command, i, v = map(str, input().split())
    if command == "+":
        tree.update(int(i), int(v))
    else:
        print(tree.query(int(i), int(v)))
        
