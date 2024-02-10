n = int(input())
cards = list(map(int, input().split()))

sergey_points = 0
dima_points = 0

left = 0
right = n - 1

turn = 1 #sergey
while left<=right:
    if cards[left] > cards[right]:
        point = cards[left]
        left +=1
    else:
        point = cards[right]
        right -=1
    if turn == 1:
        sergey_points +=point
    else:
        dima_points +=point
    turn = 1 - turn

print(sergey_points, end=" ")
print(dima_points)
