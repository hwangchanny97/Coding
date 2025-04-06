# from itertools import permutations

# N = int(input())
# A = list(map(int, input().split()))

# max_diff_sum = 0

# for a in permutations(A, N):
#     #print(a)
#     diff_sum = 0
#     for i in range(N-1):
#         diff_sum += abs(a[i]-a[i+1])

#     max_diff_sum = max(max_diff_sum, diff_sum)

# print(max_diff_sum)


from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_sum = 0

for a in permutations(A, N):
    sum = 0
    for i in range(N-1):
        sum = sum + abs(a[i]-a[i+1])

        if sum > max_sum:
            max_sum = sum

print(max_sum)