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

def solution():
    for _ in range(int(input())):
        n, q = tup_in()
        dp = [[0]*1001 for i in range(1001)]

        # set rects in array
        for _ in range(n):
            h, w = tup_in()
            dp[h][w] += h * w

        # 2D psum
        for ii in range(1, 1001): 
            for jj in range(1, 1001): 
                dp[ii][jj] += dp[ii - 1][jj] + dp[ii][jj - 1] - dp[ii - 1][jj - 1]
        for _ in range(q):
            hl, wl, hh, wh = tup_in()
            print(dp[hh - 1][wh - 1] - dp[hl][wh - 1] - dp[hh - 1][wl] + dp[hl][wl])
            

if __name__ == "__main__":
    solution()