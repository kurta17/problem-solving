n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

rooms = [0]
for x in a:
    rooms.append(rooms[-1] + x)

dormNumber = 1
for letter in b:
    while rooms[dormNumber] < letter:
        dormNumber += 1
    room_num = letter - rooms[dormNumber - 1]
    print(dormNumber, room_num)



    

