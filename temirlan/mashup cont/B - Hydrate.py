import math

A,B,C,D = map(int, input().split())
if D*C -B <=0:
    print(-1)
else:
    if A % (D*C -B) == 0:
      print(A//(D*C -B))
    else:
       print(math.ceil(A/(D*C -B)))

