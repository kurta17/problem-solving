# n = int(input())
# l = list(map(int, input().split()))

# sum_l = [0] * (n + 1)
# for i in range(1,n + 1):
#     sum_l[i] = sum_l[i - 1] + l[i - 1]

# m = int(input())
# print(sum_l)
# for _ in range(m):
#     a, b = map(int, input().split())
#     ans = sum_l[b] - sum_l[a - 1]
#     print(ans)

with open('sum2.in', 'r') as input_file:
    n = int(input_file.readline())
    nums = list(map(int, input_file.readline().split()))

    newnums = [nums[0]] * n
    for i in range(1, n):
        newnums[i] = newnums[i-1] + nums[i]

    m = int(input_file.readline())

    with open('sum2.out', 'w') as output_file:
        for _ in range(m):
            a, b = map(int, input_file.readline().split())
            if a == 1:
                output_file.write(f"{newnums[b-1]}\n")
            else:
                output_file.write(f"{newnums[b-1] - newnums[a-2]}\n")