inf = float('inf')
def solution():
    global ans
    n = int(input())
    adj = [[] for i in range(n)]
    ans = 0

    for ii in range(n-1): 
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    # print(adj)
    def dfs(node, prev, current_dist, current_prob):
        global ans

        if len(adj[node]) == 1 and prev != -1:
            ans += current_dist * current_prob
        else:
            if prev == -1:
                new_prob = current_prob / (len(adj[node]))
            else:
                new_prob = current_prob / (len(adj[node]) - 1)
            for a in adj[node]: 
                if a != prev:
                    # print("dfs from", node, 'to', a, 'prob', new_prob)
                    dfs(a, node, current_dist + 1, new_prob)
        

    dfs(0, -1, 0, 1)
    print(ans)

if __name__ == "__main__":
    solution()