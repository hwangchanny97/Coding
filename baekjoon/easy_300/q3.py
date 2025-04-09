# https://www.acmicpc.net/problem/14916 [거스름돈]

# 틀렸음
# n = int(input())
# min_num = 0
# if n ==1 or n == 3:
#     print(-1)
# elif n % 5 == 2 or n % 5 == 4 or n % 5 == 6 or n % 5 == 8:
#     min_num += (n//5) + ((n - 5*(n//5)) // 2)
#     print(min_num)
# else:
#     min_num += (n//5 -1) + ((n - 5*(n//5-1)) // 2)
#     print(min_num)
# ----------------------------------------------------------
# 그리디 알고리즘
n = int(input())

found = False
for i in range(n//2 + 1):
    if (n-2*i) % 5 == 0:
        print(i+(n-2*i) // 5)
        found = True
        break
if not found:
    print(-1)