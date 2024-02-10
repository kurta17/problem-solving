s = input().strip()

hello = "hello"
i = 0

for letter in s:
    if i < len(hello) and letter == hello[i]:
        i += 1

if i == len(hello):
    print("YES")  
else:
    print("NO")
# mlist = [1,2,3,3,3,32,2,2,1,1]
# mset = set({5,7,9})
# for i in mlist:
#     mset.add(i)

# print(mset)
