num = int(input())

def fact(n,s,k):
    ans = 1
    for i in range(s,n+1,k):
        ans *= i
        ans = ans % (10 ** 9 + 7)
    return ans

answer = 0

for n in range(1,num+1):
    if n % 2 == 0:
        ans = fact(n,2,2)
        answer += ans
    else:
        ans = fact(n,1,2)
        answer += ans

answer = answer % (10 ** 9 + 7)
print(answer)
      
    



