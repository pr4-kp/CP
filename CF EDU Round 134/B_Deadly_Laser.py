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
if possible - print(n-1 + m-1)
else print -1
"""

def solution():
    for _ in range(int(input())):
        possible = True
        n, m, sx, sy, d = tup_in()
        top_blocked = False
        bottom_blocked = False
        left_blocked = False
        right_blocked = False

        if abs(sx - 1) <= d:
            top_blocked = True
        if abs(n - sx) <= d:
            bottom_blocked = True
        if abs(sy - 1) <= d:
            left_blocked = True
        if abs(m - sy) <= d:
            right_blocked = True

        if top_blocked and bottom_blocked:
            possible = False
        elif top_blocked and left_blocked:
            possible = False
        elif bottom_blocked and right_blocked:
            possible = False
        elif right_blocked and left_blocked:
            possible = False

    
        if possible:
            print(n - 1 + m - 1)
        else:
            print(-1)

if __name__ == "__main__":
    solution()