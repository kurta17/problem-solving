n = int(input())

def print_num(n, line):
    if len(line) == n:
        print(''.join(map(str, line)))
        return

    for i in range(1, n+1):
        if i not in line:
            line.append(i)
            print_num(n, line)
            line.pop()

print_num(n, [])