n = int(input())

# Initialize a 2D dp array with all elements set to 0
dp = [[0 for _ in range(5)] for _ in range(n+1)]

# There is one way to form a sequence of length 0 with 0 adenines
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(5):
        # We can always add a C, G, or T
        dp[i][j] = 3 * dp[i-1][j]
        if j > 0:
            # We can add an A if we have not used 4 As yet
            dp[i][j] += dp[i-1][j-1]

# The answer is the sum of the number of sequences of length n with 0 to 4 As
print(sum(dp[n]))