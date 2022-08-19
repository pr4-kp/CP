inf = float('inf')
def solution():
    n = int(input())
    P = list(map(int, input().split()))
    adj = [set() for i in range(n)]
    visited = [False for i in range(n)]

    for ii in range(n):
        adj[ii].add(P[ii]-1)
        adj[P[ii]-1].add(ii)

    def dfs(node):
        if visited[node]:
            return
        else:
            visited[node] = True
            for u in adj[node]:
                dfs(u)
    
    starts = []
    ans = 0

    for ii in range(n):
        if not visited[ii]:
            dfs(ii)
            ans += 1
    print(ans)

        


if __name__ == "__main__":
    solution()