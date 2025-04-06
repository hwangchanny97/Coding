com = int(input())
net = int(input())
graph = [[] for _ in range(com)]

for i in range(net):
    x, y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)

print(graph)