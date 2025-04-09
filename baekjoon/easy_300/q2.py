# https://www.acmicpc.net/problem/1748 [수 이어 쓰기 1]

# 메모리 초과
# N = int(input())
# num_arr = []

# for i in range(1, N+1):
#     num_arr.append(i)

# #print(num_arr)

# new_num = ''.join(map(str,num_arr))
# print(len(new_num))

left = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000
]

right = [
    9,
    99,
    999,
    9999,
    99999,
    999999,
    9999999,
    99999999,
    999999999
]

N = int(input())

sum = 0

for i in range(len(left)):
    if N >= left[i] and N <= right[i]:
        sum += (N-left[i] + 1) * (i + 1)
        break
    else:
        sum += (right[i] - left[i] + 1) * (i + 1)
print(sum)