# from itertools import combinations_with_replacement

# N, K = map(int, input().split())
# k = list(map(int, input().split()))

# max_num = 0

# for a in combinations_with_replacement(k, K):
#     a = list(a)
#     num = int(''.join(map(str, a)))
#     if num > N:
#         continue
#     else:
#         max_num = max(max_num, num)

# print(max_num)


from itertools import product
 
n, k = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(n))
 
while True:
    temp = list(product(arr, repeat=length))  # repeat을 통해 몇개를 뽑을지 설정한다.
    print(temp)
    ex = []
    for i in temp:
        now=int(''.join(i))
        if now <= n:
            ex.append(now)
    if len(ex) >= 1:
        print(max(ex))
        break
    else:
        length -= 1
