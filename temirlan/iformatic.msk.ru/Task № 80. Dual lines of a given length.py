n = int(input())
k = 2
def print_num(n,line):
    if len(line) == n:
        print("".join(map(str, line)))
        return 
    
    for i in range(k):
        line.append(i)
        print_num(n,line)
        line.pop()

print_num(n, [])
