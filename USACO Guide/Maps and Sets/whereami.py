inf = float('inf')

import sys
sys.stdin = open("whereami.in","r")
sys.stdout = open("whereami.out","w")

def solution():
    n = int(input())
    s = input()
    ans = inf
    
    for k in range(1, n):
        unique = set()
        for i in range(n-k+1):
            unique.add(s[i:k+i])
        if len(unique) == n-k+1:
            ans = min(ans, k)
    print(ans)

if __name__ == "__main__":
    solution()