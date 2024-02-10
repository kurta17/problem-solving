t = int(input())

for _ in range(t):
    string = input()
    lenstr = len(string)
    if lenstr % 2 == 1:
        print(0)
    else:
        even = 0
        odd = 1
        result = 0
        while True:
            if string[even] != string[odd] and (string[even] == string[odd + 1] or string[even-1] == string[odd]):
                result += 1
            even += 2
            odd += 2
        print(result)





