import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---
There are probably 3 ways to sort:
1. by width. So then we can binary search for width very fast
2. by height "
3. by area. But there are plenty of rects with a good area that do not work

none of these are much more efficient than what I was doing
"""

def solution():
    for _ in range(int(input())):
        n, q = tup_in()
        rects = []
        dp = [[] * 1001 for i in range(1001)]
        for _ in range(n):
            rects.append(arr_in())
            
        for _ in range(q):
            ans = 0
            hs, ws, hb, wb = tup_in()
            for a in rects:
                if hs < a[0] < hb and ws < a[1] < wb:
                    ans += a[0] * a[1]
            print(ans)

if __name__ == "__main__":
    solution()