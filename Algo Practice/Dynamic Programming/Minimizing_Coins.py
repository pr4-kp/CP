import sys
# # (optional) very fast input
#import io
#import os

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = 1_000_000_000

def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

def solution():
    _, x = tup_in()
    c = arr_in()
    dp = [inf] * (x + 1)
    dp[0]=0
    for i in range(x):
        # if i == inf:
        #     continue
        for coin in c: 
            if i + coin <= x:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)
    print(dp[x] if dp[x] != inf else -1)

if __name__ == "__main__":
    solution()