char = str(input())

max_len = 1
current_len = 1

for i in range(1, len(char)):
    if char[i] == char[i - 1]:
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 1

max_num = max(max_len, current_len)
print(max_num)
    