from collections import deque

n,m=map(int,input().split())
g=[[] for _ in range(n+1)]


def bfs(g,vis,count,s):
    q=deque([s])
    vis[s]=True

    while q:
        v=q.popleft()
        for i in g[v]:
            if not vis[i]:
                count[i]=count[v]+1
                q.append(i)
                vis[i]=True
        

ans=[]

for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n):
    vis=[False for _ in range(n+1)]
    count=[0 for _ in range(n+1)]
    bfs(g,vis,count,i+1)
    ans.append(sum(count))

minNum=min(ans)
print(ans.index(minNum)+1)