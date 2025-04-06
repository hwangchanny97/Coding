N = int(input())

adj = [[] for _ in range(N)]

for i in range(N-1):
    l, r = list(map(int, input().split()))
    adj[l-1].append(r-1)
    adj[r-1].append(l-1)

visit = [False] * N
parent = [-1] * N


def dfs(u):
    visit[u] = True

    for v in adj[u]:
        if not visit[v]:
            parent[v] = u
            dfs(v) 

dfs(0)
for i in range(1,N):
    print(parent[i]+1)