import random

option1 = 0
option2 = 0
option3 = 0
option4 = 0
 
for _ in range(1000):
    y1 = random.random()
    y2 = random.random()
    y3 = random.random()
    num1 = (y1+y2)/2
    num2 = (y2+y3)/2


    if num1 < 0.5 and num2 < 0.5:
        option1 += 1
    elif num1 > 0.5 and num2 > 0.5:
        option2 += 1
    elif num1 < 0.5 and num2 > 0.5:
        option3 += 1
    elif num1 > 0.5 and num2 < 0.5:
        option4 += 1


print(f"Option 1 (both numbers in pocket 1): {option1}")
print(f"Option 2 (both numbers in pocket 2): {option2}")
print(f"Option 3 (first number in left pocket): {option3}")
print(f"Option 3 (first number in right pocket): {option4}")