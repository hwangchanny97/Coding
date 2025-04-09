# https://www.acmicpc.net/problem/2417 [정수 제곱근]

# import math

# x = 122333444455555
# result = math.sqrt(x)
# print(int(result)+1)   # 👉 4.0

# ----------------------------------
# 이분탐색 => 탐색 범위 : [1, 2^63]
N = int(input())

low = 0
high = 2**32

ans = -1
while low <= high:
    mid = (low + high) // 2
    if mid**2 < N:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print(ans)