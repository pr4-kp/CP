import sys
sys.stdin = open("planting.in","r")
sys.stdout = open("planting.out","w")
def solution():
    ans = 0
    n = int(input())
    adj = {i:[] for i in range(n)}
    for edge in range(n-1):
        a, b=  map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    for v in adj.values():
        ans = max(ans, len(v))
    print(ans+1)

if __name__ == "__main__":
    solution()