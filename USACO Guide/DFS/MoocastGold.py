import sys
sys.stdin = open("moocast.in","r")
sys.stdout = open("moocast.out","w")

def solution():
    n = int(input())
    Cowpos = []
    adj = [set() for i in range(n)]
    ans = []

    for ii in range(n): 
        Cowpos.append(list(map(int, input().split())))
    for num, cow in enumerate(Cowpos):
        for num2, cow2 in enumerate(Cowpos):
            if num != num2 and ((cow2[0] - cow[0])**2 + (cow2[1] - cow[1]) ** 2) <= cow[2]:
                adj[num].add(num2)
    
    
    def dfs(start):
        seen = set([start])
        to_visit = [start]
        visited = [0 for i in range(n)]
        while to_visit:
            current = to_visit.pop()
            for next in adj[current]:
                if not visited[next]:
                    seen.add(next)
                    visited[next] = 1
                    to_visit.append(next)
        return(len(seen))

    for start in range(n):
        ans.append(dfs(start))
    
    print(max(ans))


if __name__ == "__main__":
    solution()