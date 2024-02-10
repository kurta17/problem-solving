a, b = map(int, input().split())

def max_div(a, b):
    if b == 0:
        return a
    else:
        #print(b, a % b)
        return max_div(b, a % b)

print(max_div(a, b))