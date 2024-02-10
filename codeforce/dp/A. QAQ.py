qaq = input()
n = len(qaq)

q_count_before = [0] * n

q_count_after = [0] * n

current_q_count = 0
for i in range(n):
    if qaq[i] == 'Q':
        current_q_count += 1
    q_count_before[i] = current_q_count

print(q_count_before)
current_q_count = 0

for i in range(n - 1, -1, -1):
    if qaq[i] == 'Q':
        current_q_count += 1
    q_count_after[i] = current_q_count

total_qaq = 0
for i in range(n):
    if qaq[i] == 'A':
        total_qaq += q_count_before[i] * q_count_after[i]

print(total_qaq)

