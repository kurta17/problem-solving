def is_rbs(s):

    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs.keys():
            if stack == [] or pairs[i] != stack.pop():                
                return 'no'       
    return 'yes' if stack == [] else 'no'

s = input().strip()
print(is_rbs(s))