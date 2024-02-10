import sys
input = sys.stdin.readline
from collections import defaultdict

t= int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mydict = defaultdict(int)
    ind = n - 1
    while True:
        if mydict[a[ind]] == 0:
            mydict[a[ind]] += 1
            ind -=1
        else:
            break
    print(n - len(mydict.keys()))