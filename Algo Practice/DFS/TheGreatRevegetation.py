import sys
sys.stdin = open("revegetate.in","r")
sys.stdout = open("revegetate.out","w")

inf = float('inf')
def solution():
    n, m = map(int, input().split())
    adj = [[] for i in range(n)]
    color = [-1 for i in range(n)]

    for ii in range(m):
        d = input().split()
        adj[int(d[1]) - 1].append([int(d[2]) - 1, d[0]])
        adj[int(d[2]) - 1].append([int(d[1]) - 1, d[0]])

    unvisited = set(range(n))
    k = 0
    starts = []
    poss = True

    def dfs(s):
        to_visit = [s]
        while to_visit:
            current = to_visit.pop()
            for next in adj[current]:
                # test if colors work:

                if color[next[0]] == -1:
                    if next[1] == 'S':
                        color[next[0]] = color[current]
                    else:
                        color[next[0]] = (not color[current])
                elif color[next[0]] == color[current] and next[1] == 'S':
                    pass
                elif color[next[0]] != color[current] and next[1] == 'D':
                    pass
                else:
                    poss = False

                if next[0] in unvisited:
                    unvisited.remove(next[0])
                    to_visit.append(next[0])

    while unvisited and poss:
        start = unvisited.pop()
        color[start] = True
        starts.append(start)
        dfs(start)
    
    if poss:
        print("1" + "0" * (len(starts)))
    else:
        print("0")


if __name__ == "__main__":
    solution()