import sys
sys.stdin = open("fenceplan.in","r")
sys.stdout = open("fenceplan.out","w")

inf = float('inf')
def solution():
    ans = []
    n, m = map(int, input().split())
    coords = []
    adj = [set() for i in range(n)]

    for ii in range(n): 
        coords.append(list(map(int, input().split())))

    # adj list
    for jj in range(m): 
        edge = list(map(int, input().split()))
        adj[edge[0]-1].add(edge[1]-1)
        adj[edge[1]-1].add(edge[0]-1)

    # run a dfs while keeping track of the max and and min x, y coordinates
    # After that return sum of the diff between x's and diff between y's

    starts = set()
    unvisited = set(range(n))

    def dfs(start):
        xmax = ymax = -inf
        xmin = ymin = inf
        to_visit = [start]
        while to_visit:
            current = to_visit.pop()
            xmax = max(xmax, coords[current][0])
            ymax = max(ymax, coords[current][1])
            xmin = min(xmin, coords[current][0])
            ymin = min(ymin, coords[current][1])

            for nn in adj[current]:
                if nn in unvisited:
                    unvisited.remove(nn)
                    to_visit.append(nn)
        return (xmax-xmin) + (ymax-ymin)

    while unvisited:
        start = unvisited.pop()
        starts.add(start)
        ans.append(dfs(start))
    print(min(ans) * 2)

if __name__ == "__main__":
    solution()