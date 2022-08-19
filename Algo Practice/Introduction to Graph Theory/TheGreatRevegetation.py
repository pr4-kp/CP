import sys
sys.stdin = open("revegetate.in","r")
sys.stdout = open("revegetate.out","w")

def solution():
    n, m = map(int, input().split())
    test = [0] * n
    adj = [set() for i in range(n)]
    for field in range(m):
        a, b = map(int, input().split())
        # fix indexing
        a -= 1
        b -= 1
        adj[a].add(b)
        adj[b].add(a)
    # print(adj)
    for cColor in range(n):
        allCl = [test[cl] for cl in adj[cColor]]
        for bb in range(1, 5):
            if bb not in allCl:
                change = bb
                break
        test[cColor] = change
    print(''.join(map(str, test)))

if __name__ == "__main__":
    solution()