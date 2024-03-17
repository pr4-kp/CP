import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
MOD = int(1e9 + 7)

def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def solution():
    n, x = tup_in()
    c = arr_in()
    dp = [0] * (x + 1)
    if x == 1:
        if 1 in c:
            print(c.count(1))
        else:
            print(0)
    else:
        for coin in c:
            dp[coin] += 1
            for ii in range(x + 1):
                if ii + coin <= x:
                    dp[ii + coin] += dp[ii] % MOD

        print(dp[x] % MOD)

if __name__ == "__main__":
    solution()