t = int(input())

for _ in range(t):
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())

    len_op = (px ** 2 + py ** 2) ** 0.5
    len_oa = (ax ** 2 + ay ** 2) ** 0.5
    len_ob = (bx ** 2 + by ** 2) ** 0.5
    len_pa = ((ax - px) ** 2 + (ay - py) ** 2) ** 0.5
    len_pb = ((bx - px) ** 2 + (by - py) ** 2) ** 0.5
    len_ba = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    
    minlen = min(len_ba,len_pa,len_pb)
    print(minlen)
  
    