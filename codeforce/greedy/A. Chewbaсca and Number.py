n = str(input())
ans = []
for i in range(len(n)):
    if i == 0 and n[i] == "9":
        ans.append(n[i])
    elif int(n[i]) > 4:
        ans.append(str(9 - int(n[i]) ))
    else:
        ans.append(n[i])

print("".join(ans))
