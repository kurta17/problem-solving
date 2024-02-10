t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    left = 0
    move = 1
    result = ""

    while move < n:
        if s[left] == s[move]:
            result += s[move]
            left = move + 1
            move += 1
        move += 1

    print(result)

        
    
    

