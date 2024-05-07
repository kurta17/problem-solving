n = int(input())
students = []
for _ in range(n):
    id, score, name = map(str, input().split())
    students.append([int(id), int(score), name])

N = len(students)
for i in range(0, N - 1):
    for j in range(0, N - i - 1):
        if students[j][1] > students[j + 1][1]:
            students[j], students[j + 1] = students[j + 1], students[j]

for i in range(min(3, n)):
    print(students[-i-1][2])

for i in range(n):
    print(students[-i-1][0], end=' ')
print()  