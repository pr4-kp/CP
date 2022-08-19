inf = float('inf')

def solution():
    n = int(input())
    ans = 0
    adj = [set() for i in range(n)]
    unvisited = set(range(n))
    color = list(range(n))
    color[0] = 1

    for _ in range(n-1):
        edge = list(map(int, input().split()))
        adj[edge[0]-1].add(edge[1]-1)
        adj[edge[1]-1].add(edge[0]-1)

    def dfs(s):
        to_visit = [s]
        while to_visit:
            current = to_visit.pop()
            for next in adj[current]:
                if next in unvisited:
                    color[next] = (not color[current])
                    unvisited.remove(next)
                    to_visit.append(next)
                
    # print(color)
    dfs(0)
    tCt = color.count(True)
    # print(color)
    print(tCt * (n - tCt) - (n - 1))


if __name__ == "__main__":
    solution()