def maxdiff(weights):
    n = len(weights)
    psum = [0] * (n + 1)

    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + weights[i - 1]

    maxdiff = 0

    for k in range(1, n):
        if n % k == 0:
            lmax, lmin = 0, psum[n]

            for i in range(k, n + 1, k):
                truck_weight = psum[i] - psum[i - k]
                lmax = max(lmax, truck_weight)
                lmin = min(lmin, truck_weight)

            maxdiff = max(maxdiff, lmax - lmin)

    return maxdiff

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        weights = list(map(int, input().split()))

        print(maxdiff(weights))
