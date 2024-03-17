from re import A
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
    for _ in range(int(input())):
        n = int(input())
        b = input().rstrip('\n')
        d = 0
        maxd = 0
        all = []
        for ii in range(2 * n):
            if b[ii] == "(":
                d += 1
            else:
                d -= 1
            if d == 0:
                all.append(maxd)
                maxd = 0
            maxd = max(d, maxd)
        ans = sum(all) - len(all) + 1
        print(ans)
            



if __name__ == "__main__":
    solution()