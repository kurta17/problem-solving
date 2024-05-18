def sift_down(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= len(data):
        return
    if right >= len(data):
        child_min = left
    else:
        child_min = left if data[left] < data[right] else right
    if data[i] > data[child_min]:
        data[i], data[child_min] = data[child_min], data[i]
        sift_down(data, child_min)


def sift_up(data, i):
    if i == 0:
        return
    parent = (i - 1) // 2
    if data[parent] > data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def insert(data, money, id):
    data.append((money, id))
    sift_up(data, len(data) - 1)


def extract_min(data,i=0):
    data[i], data[-1] = data[-1], data[i]
    res = data.pop()
    if data:
        sift_up(data, i)
        sift_down(data, i)
    return res


n = int(input().strip())
data = []
for _ in range(n):
    operation = input().strip().split()
    if operation[0] == "+":
        id, money = map(int, operation[1:])
        insert(data, -money, id)
    else:    
        print(extract_min(data)[1])