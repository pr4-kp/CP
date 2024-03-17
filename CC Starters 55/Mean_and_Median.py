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
        x, y = tup_in()
        b = y
        targ = 3 * x - b
        if targ <= 0:
            a = -1000
            c = 1000 + targ
        else:
            a = -1000 + targ 
            c = 1000
        print(a, b, c)

if __name__ == "__main__":
    solution()