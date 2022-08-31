import collections
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
dist = [float('inf')] * (n + 1)
dist[1] = 0

parent = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

bfs_deq = collections.deque()
bfs_deq.appendleft(1)
while bfs_deq:
    cur_node = bfs_deq.popleft()
    for adj_node in graph[cur_node]:
        if dist[adj_node] == float('inf'):
            dist[adj_node] = dist[cur_node] + 1
            parent[adj_node] = cur_node
            bfs_deq.append(adj_node)

if dist[n] == float('inf'):
    print("IMPOSSIBLE")
else:
    back = n
    path = []
    while back != 0:
        path.append(back)
        back = parent[back]

    print(len(path))
    print(*reversed(path))
