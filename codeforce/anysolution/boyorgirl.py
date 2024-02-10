a = str(input())
mydict = {}
for i in a:
    if i not in mydict.keys():
        mydict[i] = 1
    else:
        mydict[i] += 1

if len(mydict) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
     