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
    for _ in range(int(input())):
        n = int(input())
        ans = 0
        ans += (n // 6) * 16
        add = [1, 3, 3, 3, 1, 5]
        n %= 6
        i = 0
        while n > 0:
            ans += add[i]
            i += 1
            n -= 1
        print(ans)


if __name__ == "__main__":
    solution()