def func(a):
    rob1, rob2 = 0,0
    for i in a:
        temp = max(i + rob1, rob2)
        print(temp)
        rob1 = rob2
        print(rob1)
        
        rob2 = temp
        print(rob2)
    return rob2

a = [1,2,3,1]
print(func(a))
