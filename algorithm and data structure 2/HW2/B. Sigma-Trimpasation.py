# This is a template for problem Sigma-Trimpazation.

from time import time

# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = False

# Fixed parameters of quantum process:
quantum_a = 7**5
quantum_m = 2**31 - 1

def counting_sort_sum(n, m, q0):
    m_div2 = m // 2
    q = q0

    # generating x data:
    x = [0] * m
    for i in range(n):
        x[q % m] += 1
        q = ((q * quantum_a) % quantum_m)

    # calculating sum:
    res = 0
    i = 0
    for j in range(m):
        for z in range(x[j]):
            res += (i + 1) * (j - m_div2)
            i += 1

    return res



if __name__ == '__main__':
    N, M, q0 = map(int, input().split())
    t = time()
    print(counting_sort_sum(N, M, q0))
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')