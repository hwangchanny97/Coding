# import sys
# A, B, C, M = map(int, sys.stdin.readline().split())
# time = 24
# tired = 0
# job = 0



# if A > M:
#     print(0)
# else:
#     for i in range(24):
#         if A+tired <= 10:
#             tired += A
#             job += B
#             time -= 1
#         else:
#             tired -= C
#             time -= 1
#     print(job)

#=====================
#sys를 이용하여 입력한 경우

# import sys

# A,B,C,M = map(int, sys.stdin.readline().split())

# T = 0
# DW = 0

# for i in range(24):
#   if T > M:
#     print(0)
#   else:
#     if T + A <= M:
#       T += A
#       DW += B
#     else:
#       if T - C >=0:
#         T -= C
#       else:
#         T = 0
# print(DW)

#===========================
import sys
A,B,C,M = map(int, sys.stdin.readline().split())

piro = 0
work = 0
for _ in range(24):
    if piro + A > M:
        piro -= C
        piro = max(0, piro)
    else:
        piro += A
        work += B
print(work)