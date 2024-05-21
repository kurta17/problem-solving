from math import ceil, log2

class RMQSegmentTree:
    def __init__(self, a):
        self.N = 2 ** int(ceil(log2(len(a))))
        self.neutral_value = float('inf')
        self.s = [None] * (self.N - 1) + list(a) + [self.neutral_value] * (self.N - len(a))
        for i in range(self.N - 2, -1, -1):
            self.refresh_s(i)

    def refresh_s(self, i):
        self.s[i] = min(self.s[2 * i + 1], self.s[2 * i + 2])

    def rmq_i(self, l, r, i, li, ri):
        if r <= li or ri <= l:
            return self.neutral_value
        if l <= li and ri <= r:
            return self.s[i]
        middle = li + (ri - li) // 2
        return min(self.rmq_i(l, r, 2 * i + 1, li, middle),
                   self.rmq_i(l, r, 2 * i + 2, middle, ri))

    def update(self, i, v):
        i += self.N - 1
        self.s[i] = v
        while i > 0:
            i = (i - 1) // 2
            self.refresh_s(i)

    def rmq(self, l, r):
        return self.rmq_i(l, r, 0, 0, self.N)


n,m = map(int, input().split())
a = list(map(int, input().split()))
tree = RMQSegmentTree(a)
for _ in range(m):
    command, i, v = map(str, input().split())
    if command == "+":
        tree.update(int(i), int(v))
    else:
        print(tree.rmq(int(i), int(v)))
