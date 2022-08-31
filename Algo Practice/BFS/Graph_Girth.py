import collections
import sys

input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

def solution():
    n, m = tup_in()
    adj = [[] for i in range(n+1)]
    for _ in range(m): 
        u, v = tup_in()
        adj[u].append(v)
        adj[v].append(u)

    girth = inf
    
    for test in range(1, n + 1):
        visited = [False] * (n+1)
        dist = [inf] * (n+1)
        dist[test] = 0
        parent = [0] * (n+1)

        d = collections.deque()
        d.appendleft(test)
        while d: 
            c=d.popleft()
            visited[c]=True
            for a in adj[c]:
                if not visited[a]:
                    dist[a] = dist[c] + 1
                    parent[a] = c
                    d.append(a)
                elif a != parent[c]:
                    girth = min(girth, dist[a] + dist[c] + 1)
                    d.clear()
                    break
    
    if girth == inf:
        print(-1)
    else:
        print(girth)

if __name__ == "__main__":
    solution()