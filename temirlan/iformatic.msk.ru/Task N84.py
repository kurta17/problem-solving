n, k = map(int, input().split())

def print_num(n, k, line, ones):
    if len(line) == n:
        if ones == k:
            print(''.join(map(str, line)))
        return

    for i in range(k):  
        if i == 1:
            ones += 1
        line.append(i)
        print_num(n, k, line, ones)
        line.pop()
        if i == 1:
            ones -= 1 

print_num(n, k, [], 0)