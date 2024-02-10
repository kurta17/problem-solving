def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

a = str(input())
b = dict()
k = []

for i in a:
    k.append(i)
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1

summetion = 1
for i in b.values():
    summetion *= factorial(i)

# Calculate the total number of unique permutations
total_permutations = factorial(len(a)) // summetion

# Print the total number of unique permutations
print(total_permutations)

# Sort the list to ensure we start from the lowest lexicographical permutation
k.sort()

# Print the first permutation (the input string sorted in ascending order)
print("".join(k))

while total_permutations > 1:
    # Find the largest index i such that k[i] < k[i + 1]
    for i in range(len(k) - 2, -1, -1):
        if k[i] < k[i + 1]:
            break

    # Find the largest index j greater than i such that k[i] < k[j]
    for j in range(len(k) - 1, i, -1):
        if k[i] < k[j]:
            break

    # Swap the value of k[i] with that of k[j]
    k[i], k[j] = k[j], k[i]

    # Reverse the sequence from k[i + 1] up to and including the final element k[n]
    k[i + 1:] = reversed(k[i + 1:])

    # Print the new permutation
    print("".join(k))

    total_permutations -= 1