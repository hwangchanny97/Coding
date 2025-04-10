# # https://www.acmicpc.net/problem/2960

# N, K = map(int,input().split())
# num_list = []

# for i in range(2, N+1):     #1. 2 ~ N까지 나열
#     num_list.append(i)

# def is_prime(n):            #2.1 소수인지 판별
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1): 
#         if n % i == 0:
#             return False
#     return True

# def find_smallest_prime(nums):      #2.2 소수 중 가장 작은 수 구함
#     primes = [x for x in nums if is_prime(x)]
#     if primes:
#         return min(primes)
#     else:
#         None
#     #return min(primes) if primes else None

# # smallest_prime = find_smallest_prime(num_list)
# # print(smallest_prime)

# count = 0
# is_bool = True
# while is_bool:
#     smallest_prime = find_smallest_prime(num_list)
    
#     for i in range(1, N//2 + 1):
#         if smallest_prime*i >= N:
#             break
#         erased_num = num_list.pop(smallest_prime*i)
#         count += 1
#         if count == K:
#             is_bool = False
#             ans = erased_num

# print(ans)

N, K = map(int,input().split())
def eratosthenes_kth_removed(N, K):
    is_removed = [False] * (N + 1)
    count = 0

    for i in range(2, N + 1):
        if is_removed[i]:
            continue

        # i는 소수 → i의 배수 지우기
        for j in range(i, N + 1, i):
            if not is_removed[j]:
                is_removed[j] = True
                count += 1

                if count == K:
                    return j

ans = eratosthenes_kth_removed(N,K)
print(ans)