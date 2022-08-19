inf = float('inf')
def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        adj = [[] for i in range(n)]

        for ii in range(m): 
            u, v = map(int, input().split())
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        # Graph setup
        unvisited = set(range(n))
        color = list(range(n))
        color[0] = 1
        
        def dfs(s):
            to_visit = [s]
            while to_visit:
                current = to_visit.pop()
                for next in adj[current]:
                    if next in unvisited:
                        color[next] = (not color[current])
                        unvisited.remove(next)
                        to_visit.append(next)

        dfs(0)
        # print(color)
        s = color.count(False)
        if min(s, n - s) == s:
            print(s)
            for ii in range(n):
                if color[ii] == False:
                    print(ii+1, end=' ')
        else:
            print(n - s)
            for ii in range(n):
                if color[ii] == True:
                    print(ii+1, end=' ')



if __name__ == "__main__":
    solution()