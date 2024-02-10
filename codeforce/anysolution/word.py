s = str(input())
letterupper = 0
letterlower = 0
for i in s:
    if i.isupper():
        letterupper +=1
    else:
        letterlower +=1
        
if letterupper > letterlower:
    print(s.upper())
else:
    print(s.lower())
