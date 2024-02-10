
n = int(input())
answer = 0

for m in range(n):
    s = str(input()).upper()
    char_list = []

    for i in s:
        if char_list and char_list[-1] == i:
            char_list.pop()
        else:
            char_list.append(i)

    if len(char_list) == 0:
        answer += 1

print(answer)



