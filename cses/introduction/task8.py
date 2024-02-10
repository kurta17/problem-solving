# n = int(input())
# nlist = [str(i) for i in range(1,n+1)]
# set1 = []
# set2 = []
# total= n*(n+1)//2
# if total % 2 == 0:
#     print("YES")

#     if n % 2 == 0:
#         while len(nlist) != 0:
#             set1.append((nlist[-1]))
#             set1.append((nlist[0]))
#             set2.append((nlist[1]))
#             set2.append((nlist[-2]))
#             nlist = nlist[2:-2]
#         print(len(set1))
#         print(" ".join(set1))
#         print(len(set2))
#         print(" ".join(set2))
#     else:
#         set1.append("1")
#         set1.append("2")
#         set2.append("3")
#         nlist = nlist[3:]
#         while len(nlist) != 0:
#             set1.append((nlist[-1]))
#             set1.append((nlist[0]))
#             set2.append((nlist[1]))
#             set2.append((nlist[-2]))
#             nlist = nlist[2:-2]
#         print(len(set1))
#         print(" ".join(set1))
#         print(len(set2))
#         print(" ".join(set2))

# else:
#     print("NO")

n = int(input())
nlist = [str(i) for i in range(1, n + 1)]
set1 = []
set2 = []
total = n * (n + 1) // 2

if total % 2 == 0:
    print("YES")

    if n % 2 == 0:
        for i in range(n // 2):
            set1.append(nlist.pop())
            set1.append(nlist.pop(0))
            set2.append(nlist.pop(1))
            set2.append(nlist.pop(-2))

        print(len(set1))
        print(" ".join(set1))
        print(len(set2))
        print(" ".join(set2))
    else:
        set1.append("1")
        set1.append("2")
        set2.append("3")
        nlist = nlist[3:]

        for i in range((n - 3) // 2):
            set1.append(nlist.pop())
            set1.append(nlist.pop(0))
            set2.append(nlist.pop(1))
            set2.append(nlist.pop(-2))

        print(len(set1))
        print(" ".join(set1))
        print(len(set2))
        print(" ".join(set2))

else:
    print("NO")

        

    
