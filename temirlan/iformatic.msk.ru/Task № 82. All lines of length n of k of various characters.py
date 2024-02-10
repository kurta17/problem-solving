n,k = map(int, input().split())


def print_num(n,k,line):
    if len(line) == n:
        print("".join(map(str, line)))
        return 
    
    for i in range(k):
        line.append(i)
        print_num(n,k,line)
        line.pop()

print_num(n,k,[])