N, K = map(int, input().split())

def gen(chain):
    if len(chain) == N:
        print(' '.join(map(str, chain)))
        return
    for i in range(1, K + 1):
        chain.append(i)
        gen(chain)
        chain.pop()
        

gen([])

