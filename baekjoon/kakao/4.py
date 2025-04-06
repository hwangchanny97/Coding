import sys
input = sys.stdin.readline

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]

# 게임판의 칸들을 차례대로 훑으면서
# 구름이 없는 칸이면 주위에 구름이 몇 개 있는지 세어서 K와 같은지 확인하면 된다.
ans = 0 # 주위에 구름이 K개 있는 칸의 개수

for i in range(N):
    for j in range(N):

        # 구름이 있는 칸이면 깃발을 꽂을 수 없다.
        if M[i][j] == 1:
            continue

        # 상하좌우와 대각선으로 인접한 칸 중 구름이 있는 칸을 찾는다.
        ct = 0 # 주위에 있는 구름이 있는 칸의 개수
        for k in range(8):
            next_i = i + di[k]
            next_j = j + dj[k]

            # 검사하고자 하는 칸이 범위 내이어야 하고 구름이 있어야 한다.
            if 0 <= next_i < N and 0 <= next_j < N and M[next_i][next_j] == 1:
                ct += 1

        # 구름이 있는 칸이 정확하게 K개라면 조건을 만족하는 칸이다.
        if ct == K:
            ans += 1

print(ans)