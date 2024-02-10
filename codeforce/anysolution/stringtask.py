a = input()
mlist = []
for i in a:
    if i not in ("A", "O" , "Y", "E", "U", "I" , "a", "o" , "y", "e", "u", "i"):
        mlist.append(i.lower())
    

result = ".".join(mlist)

print("."+ result)
