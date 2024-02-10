t = int(input())

for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))

    m.sort()
    my_list = [(m[i], m[2 * n - i - 1]) for i in range(n)]
    
    half_len = sum(abs(my_list[i][0] - my_list[i - 1][0]) + abs(my_list[i][1] - my_list[i - 1][1]) for i in range(1, n))
    half_len += abs(my_list[0][0] - my_list[n - 1][0]) + abs(my_list[0][1] - my_list[n - 1][1])

    print(half_len//2)

    for i in my_list:
        print(i[0], i[1])
    
