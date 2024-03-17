import sys
import math
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
    for ii in range(int(input())):
        ans = 0
        n = ii
        for a in range(1, n):
            for b in range(1, n):
                for c in range(1, n):
                    if a + b + c == n:
                        ans += math.gcd(a, b)
        print(ans)



if __name__ == "__main__":
    solution()