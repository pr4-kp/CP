import sys
sys.stdin = open("factory.in","r")
sys.stdout = open("factory.out","w")

def solution():
    n = int(input())
    adj = [set() for i in range(n)]
    for edge in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].add(b)
    fin = []
    for out in range(n):
        if len(adj[out]) == 0:
            fin.append(out)
    if len(fin) > 1:
        print(-1)
    else:
        print(fin[0]+1)


if __name__ == "__main__":
    solution()