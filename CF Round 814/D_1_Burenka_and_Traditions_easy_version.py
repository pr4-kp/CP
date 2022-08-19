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

"""
# --- BEGIN PREFIX SUM ---
"""
- O(n) preprocessing time
- O(1) range sum query
"""
def psum(l, n):
    p = [0]
    for i in range(n):
        p.append(p[-1])
        p[-1] ^= l[i]
    return p
# --- END PREFIX SUM ---

def solution():
    for _ in range(int(input())):
        n = int(input())

if __name__ == "__main__":
    solution()