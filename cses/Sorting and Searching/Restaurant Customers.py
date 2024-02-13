n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append((start, 1))
    times.append((end, -1))

times.sort()
curr_ppl = 0
max_ppl = 0
for t in times:
    curr_ppl += t[1]
    max_ppl = max(max_ppl, curr_ppl)
print(times)
print(max_ppl)
















# n = int(input())

# cos = dict()

# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(a, b + 1):
#         if j in cos:
#             cos[j] += 1
#         else:
#             cos[j] = 1

# sorted_cos = sorted(cos.items(), key=lambda x: x[1], reverse=True)
# print(sorted_cos[0][1])


