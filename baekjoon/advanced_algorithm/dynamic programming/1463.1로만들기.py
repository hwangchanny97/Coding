# 1463

N = int(input())

a = [0] * (N+1)     # 길이 N+1, a[N]

a[1] = 0

for i in range(2, N+1):
    a[i] = 1 + a[i-1]   # 언제나 가능한 -1을 하는 경우

    if i % 3 == 0:
        a[i] = min(a[i], 1 + a[i//3])   # 만약 3으로 나누어진다면 a[i]를 이전 a[i]와 (1+a[i//3])과 비교해서 최소값으로 변경 
    if i % 2 == 0:
        a[i] = min(a[i], 1 + a[i//2])


print(a[N])