# B = input()

# ans=""
# count = 0
# impossible = False

# for i in range(len(B)):
#     if B[i] == "X":
#         count += 1
#         if count == 4:
#             ans += "AAAA"
#             count = 0
#     else:
#         if count == 0:
#             ans += "."
#         elif count == 1:
#             impossible = True
#             break
#         elif count == 2:
#             ans += "BB"
#             count = 0
#             ans += "."
#         elif count == 3:
#             impossible = True
#             break

# if count == 1:
#     impossible = True
# elif count == 2:
#     ans += "BB"
# elif count == 3:
#     impossible: True

# if not impossible:
#     print(ans)
# else:
#     print(-1)
#======================================
# str.replace("XXXX", "AAAA") :  
# 파이썬에서의 replace() 함수는 왼쪽부터 해당하는 문자열을 찾아서 치환해주는 함수입니다.
# 먼저 입력값을 board 변수에 저장합니다. 그리고 replace() 함수를 2번 호출합니다.
# 왼쪽부터 모든 'XXXX'를 'AAAA'로 치환하고, 바뀐 문자열에서 남은 'XX'를 모두 'BB'로 치환합니다.
# 그러면 XXXX와 XX는 모두 사라졌을 것이고, X가 남아있다면 -1을, X가 없다면 바뀐 board를 출력하면 됩니다.

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)

