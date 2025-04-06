# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# # bfs 함수
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# count = 0 # 연결 노드의 수
# visited = [False] * (n+1)
# for i in range(1, n+1):
#     if not visited[i]:
#         bfs(graph, i, visited) # bfs 한 번 끝날 때마다 count+1
#         count += 1

# print(count)

# -------------------------------------
# 나의 풀이

# 도달 가능한 노드를 체크하는 배열을 만든다 (arr).
# 도달 했는지 체크하는 배열을 만든다 (check)).
# ---------------------------------------
# check배열을 확인해서 도달하지 않은거를 선택한다. 모두 도달 했다면 끝낸다.
# 1번 노드부터 시작.
# 1번과 연결된 노드들을 arr에 넣는다. ???
# 그리고 1번은 check[1] = True
# arr에 다음꺼를 꺼내어 반복한다. 
# arr에 없다면 간선 갯수 +1
# --------------------------------------- 반복

# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = list(map(int,input().split())) # 정점의 개수, 간선의 개수

# adj = [[] for _ in range(N)] # 인접 리스트

# for _ in range(M):
#     u, v = list(map(int,input().split()))
#     adj[u-1].append(v-1)
#     adj[v-1].append(u-1)

# visit = [False] * N
# count = 0

# for i in range(N):
#     if visit[i]:
#         continue
    
#     # bfs start
#     count += 1  # found a start point

#     queue = deque([i])
#     visit[i] = True

#     while len(queue) != 0:
#         u = queue.popleft()

#         for v in adj[u]:
#             if not visit[v]:
#                 queue.append(v)
#                 visit[v] = True

# print(count)

import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N+1)]

for i in range(M):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

visit = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if visit[i]:
        continue

    count += 1
    queue = deque([i])
    visit[i] = True

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(count)

