n = int(input())
w = list(map(int, input().split()))

def min_diff(i,first,second):
    if i == n:
        return abs(first - second)
    return min(min_diff(i+1,first + w[i],second),min_diff(i+1,first,second + w[i]))

print(min_diff(0, 0, 0))