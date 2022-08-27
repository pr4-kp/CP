import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
MOD = 10 ** 9 + 7
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---

"""

def solution():
    n = int(input())
    dp = [0] * (n + 1)
    # dp[0]=0
    for ii in range(1, min(7, n + 1)):
        dp[ii] = 1
    
    for ii in range(1, n+1): 
        for jj in range(1,7): 
            if ii-jj>0:
                dp[ii] += dp[ii-jj] % MOD
    
    print(dp[-1] % MOD)


if __name__ == "__main__":
    solution()