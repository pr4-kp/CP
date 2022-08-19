import sys
#import io
#import os

# # very fast input
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline
inf = float('inf')
def arr_in():
    return list(map(int, input().split()))

def tup_in():
    return map(int, input().split())

"""
--- Notes ---
Binary search for the min value that makes t items.

Change: make MAX = t * max(K)
"""

def solution():
    n, t = tup_in()
    K = arr_in()

    def makes_t(ind):
        made = 0
        for time_per in K:
            made += ind // time_per
        return t <= made

    MAX = t * max(K)

    left = 0
    right = MAX
    while left + 1 < right:
        mid = left + (right - left) // 2
        if makes_t(mid):
            right = mid
        else:
            left = mid
    
    print(right)

if __name__ == "__main__":
    solution()