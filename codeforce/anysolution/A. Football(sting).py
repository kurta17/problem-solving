n = int(input())
teams = []
for _ in range(n):
    team = str(input())
    teams.append(team)
first = teams[0]
sc1 = 0
sc2 = 0
for i in teams:
    if i == first:
        sc1 += 1
    else:
        second = i
        sc2 += 1
if sc1 > sc2:
    print(first)
else:
    print(second)

