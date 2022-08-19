# import sys
# sys.stdin = open("moocast.in","r")
# sys.stdout = open("moocast.out","w")

inf = float('inf')
def solution():
    global adj
    cows = []
    # adj = []
    n = int(input())
    for ii in range(n): 
        c = list(map(int, input().split()))
        cows.append(c)
    
    # STEP 1: Find the max X value
    maxX = 0
    for ii in cows:
        for jj in cows:
            maxX = max(maxX, (ii[0] - jj[0]) ** 2 + (ii[1] - jj[1]) ** 2)

    def make_adj(X):
        adj = [[] for i in range(n)]
        for ii in range(n):
            for jj in range(ii):
                if (cows[ii][0] - cows[jj][0]) ** 2 + (cows[ii][1] - cows[jj][1]) ** 2 <= X:
                    adj[ii].append(jj)
                    adj[jj].append(ii)
        return adj


    # Do a binary search on different values of X

    left = 1
    right = maxX

    while left < right:
        mid = left + (right - left) // 2
        feed_adj = make_adj(mid)

        if dfs(feed_adj, 0) < n:
            left = mid + 1
        else:
            right = mid
    print(mid)



    # print(maxX)


if __name__ == "__main__":
    solution()