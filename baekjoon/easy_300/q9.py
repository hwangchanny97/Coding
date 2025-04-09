# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))

low = 0
high = max(H)

answer = -1

while low <= high:
    mid = (low + high) // 2

    total = 0
    for i in range(N):
        if H[i] > mid:
            total += H[i]-mid
    
    if total >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid -1

print(answer)