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
        a = arr_in()
        mm = 0
        for ii in range(n - 1):
            mm = max(mm, a[ii]-a[ii+1])
        mm = max(a[n-1] - a[0], mm)
        mm = max(max(a) - a[0], mm)
        mm = max(a[n-1] - min(a), mm)


        print(mm)

if __name__ == "__main__":
    solution()