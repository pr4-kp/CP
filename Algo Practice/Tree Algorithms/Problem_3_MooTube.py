import sys
sys.stdin = open("mootube.in","r")
sys.stdout = open("mootube.out","w")

inf = float('inf')
ans = 0
def solution():
    global ans
    n, q = map(int, input().split())
    adj = [[] for i in range(n)]
    # Q = [0 for i in range q]
    for ii in range(n-1):
        u, v, r = map(int, input().split())
        adj[u-1].append([v-1, r])
        adj[v-1].append([u-1, r])

    minv = [inf for i in range(n)]
    

    def dfs(node, prev, k):
        global ans
        for a in adj[node]:
            if a[0] != prev:
                # print(node, a)
                minv[a[0]] = min(a[1], minv[node])
                if minv[a[0]] >= k:
                    ans += 1
                    # print("ans", ans)
                    dfs(a[0], node, k)
        return ans

    for ii in range(q):
        ans = 0
        k, v = map(int, input().split())
        print(dfs(v - 1, -1, k))
        
        minv = [inf for i in range(n)]

if __name__ == "__main__":
    solution()