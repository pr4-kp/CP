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
    n, q = tup_in()
    array = arr_in()
    for _ in range(q):
        l, r = tup_in()
        print(len(set(array[(l - 1):r])))

if __name__ == "__main__":
    solution()