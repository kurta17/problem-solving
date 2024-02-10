mex_dict_add = {0: 1}  
mex_dict_search = {}   
result = []

q = int(input())
queries = [input().split() for _ in range(q)]

for query in queries:
    if query[0] == '+':
        x = int(query[1])
        mex_dict_add[x] = 1
    elif query[0] == '?':
        k = int(query[1])
        if k not in mex_dict_search:
            mex_dict_search[k] = 0
        while mex_dict_search[k] in mex_dict_add:
            mex_dict_search[k] += k
        result.append(mex_dict_search[k])

for i in result:
    print(i)


