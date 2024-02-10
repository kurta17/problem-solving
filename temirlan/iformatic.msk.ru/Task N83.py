n,k = map(int, input().split())


def print_num(n,k,line):
    if len(line) == n:
        print("".join(map(str, line)))
        return 
    
    for i in reversed(range(k)):
        if i < 10:
            line.append(str(i))
        else:  
            line.append(chr(ord('a') + i - 10))
        print_num(n,k,line)
        line.pop()

print_num(n,k,[])