word = input().strip()


if word.isupper() or (word[0].islower() and word[1:].isupper()):
    answer = word.swapcase()
elif len(word) == 1:
    answer = word.upper()
else:
    answer = word

print(answer)
