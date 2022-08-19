import sys
sys.stdin = open("closing.in","r")
sys.stdout = open("closing.out","w")


def solution():
    n, m = map(int, input().split())
    adj = [set() for i in range(n)]
    for ii in range(m):
        a, b = map(int, input().split())
        adj[a-1].add(b-1)
        adj[b-1].add(a-1)

    # loop here
    unv = set(range(0, n))
    for jj in range(n):
        if jj == 0:
            pass
        else:
            rem = int(input())
            unv.remove(rem-1)
            for adjacent in adj[rem-1]:
                adj[adjacent].remove(rem-1)
        starts = set()
        unvisited = unv.copy()

        def dfs(start):
            to_visit = [start]
            while to_visit:
                current = to_visit.pop()
                for nn in adj[current]:
                    if nn in unvisited:
                        unvisited.remove(nn)
                        to_visit.append(nn)
        
        while unvisited:
            start = unvisited.pop()
            starts.add(start)
            dfs(start)
        
        if len(starts) == 1 or len(starts) == 0:
            print("YES")
        else:
            print("NO")
    int(input())

if __name__ == "__main__":
    solution()