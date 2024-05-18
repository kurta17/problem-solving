def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def right_circular_shift(s1, s2):
    if len(s1) != len(s2):
        return -1

    combined_string = s1 + s1
    lps = compute_lps(s2)
    n = len(s2)

    i = 0
    j = 0
    while i < len(combined_string):
        if s2[j] == combined_string[i]:
            i += 1
            j += 1

            if j == n:
                return (len(s1) - (i - j)) % n
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

s1 = input().strip()
s2 = input().strip()

result = right_circular_shift(s1, s2)
print(result)
