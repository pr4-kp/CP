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

"""

def solution():
    forest = []
    n, q = tup_in()
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for _ in range(n):
        forest.append(list(input().rstrip('\n')))
    
    for ii in range(1, n + 1):
        for jj in range(1, n + 1):
            dp[ii][jj] = dp[ii-1][jj] + dp[ii][jj-1] - dp[ii-1][jj-1]
            if forest[ii-1][jj-1] == '*':
                dp[ii][jj] += 1

                
    for _ in range(q):
        a, b, c, d = tup_in()
        print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])



if __name__ == "__main__":
    solution()