s = input().strip()

char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

even_chars = []
odd_chars = []

for char, freq in char_count.items():
    if freq % 2 == 0:
        even_chars.extend([char] * (freq // 2))
    else:
        odd_chars.append(char * freq)

if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    first_half = "".join(even_chars)
    middle = "".join(odd_chars)
    second_half = first_half[::-1]

    palindrome = first_half + middle + second_half
    print(palindrome)
