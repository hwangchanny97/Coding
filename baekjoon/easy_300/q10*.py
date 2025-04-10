# https://www.acmicpc.net/problem/17626


import math

def dp_four_squares(n):
    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1

    return dp[n]

n = int(input())
print(dp_four_squares(n))
