import sys
# from math import isqrt
input = sys.stdin.readline
inf = float('inf')

def solution():
    for _ in range(int(input())):
        n = int(input())
        ans = [0 for i in range(n)]
        def recurse(r):
            if r < 0:
                return
            s = (2 * r) ** 0.5
            s *= s
            l = int(s - r)
            recurse(l - 1)
            
            while l <= r:
                ans[l] = r
                ans[r] = l
                l += 1
                r -= 1
        
        recurse(n - 1)
        print(*ans)
if __name__ == "__main__":
    solution()