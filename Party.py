def solution():
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        adj = [set() for i in range(n)]
        friendsInvited = set()
        unhappiness = list(map(int, input().split()))
        dun = {i:unhappiness[i] for i in range(n)}
        cake = m

        for ii in range(m):
            cAdj = list(map(int, input().split()))
            adj[cAdj[0]-1].add(cAdj[1]-1)
            adj[cAdj[1]-1].add(cAdj[0]-1)
        t = 0

        # print(adj)

        for k, v in sorted(dun.items(), key=lambda x: x[1]):
            if cake % 2 == 0:
                break
            else:
                if len(adj[k]) == 0:
                    pass
                else:
                    for xx in adj[k]:
                        adj[xx].remove(k)
                        cake -= 1
                    # print("removed", k, "for", v, "cake now", cake, len(adj[k]))

                    t += v
        ans.append(t)
    [print(a) for a in ans]




if __name__ == "__main__":
    solution()