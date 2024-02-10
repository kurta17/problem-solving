def dfs(employee, managers, groups):
    stack = [employee]
    while stack:
        current_employee = stack[-1]
        stack.pop()

        if current_employee not in managers:
            groups[current_employee] = 1
        else:
            superior = managers[current_employee]
            if groups[superior] == -1:
                stack.append(current_employee)
                stack.append(superior)
            else:
                groups[current_employee] = 1 + groups[superior]

n = int(input())
managers = [0] + [int(input()) for _ in range(n)]
groups = [-1] * (n + 1)

for i in range(1, n + 1):
    if groups[i] == -1:
        dfs(i, managers, groups)

result = max(groups)
print(result)
